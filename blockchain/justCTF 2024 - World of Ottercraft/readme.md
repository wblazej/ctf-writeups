`solve.mode`:

```rust
module solve::solve {

    // [*] Import dependencies
    use challenge::Otter::{Self, OTTER, enter_tavern, buy_sword, checkout, find_a_monster, 
        bring_it_on, return_home, get_the_reward, buy_flag, buy_shield};

    public fun solve(
        _board: &mut Otter::QuestBoard,
        _vault: &mut Otter::Vault<OTTER>,
        _player: &mut Otter::Player,
        _ctx: &mut TxContext
    ) {
        let mut ticket = enter_tavern(_player);

        buy_sword(_player, &mut ticket);
        checkout(ticket, _player, _ctx, _vault, _board);

        let mut i = 0;

        while (i < 10) {
            find_a_monster(_board, _player);
            i = i + 1;
        };

        bring_it_on(_board, _player, 0);
        return_home(_board, _player);

        get_the_reward(_vault, _board, _player, _ctx);
        
        let mut j = 0;

        while (j < 9) {
            let mut second_ticket = enter_tavern(_player);
            buy_shield(_player, &mut second_ticket);
            get_the_reward(_vault, _board, _player, _ctx);
            checkout(second_ticket, _player, _ctx, _vault, _board);
            j = j + 1;
        };

        let mut final_ticket = enter_tavern(_player);
        buy_flag(&mut final_ticket, _player);
        checkout(final_ticket, _player, _ctx, _vault, _board);
    }

}
```
