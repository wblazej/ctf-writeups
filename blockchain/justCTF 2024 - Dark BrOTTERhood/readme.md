`solve.move`:

```rust
module solve::solve {

    // [*] Import dependencies
    use sui::random::Random;
    use challenge::Otter::{OTTER, Vault, QuestBoard, Player, find_a_monster, 
        fight_monster, return_home, get_the_reward, buy_flag, prove, buy_sword};

    #[allow(lint(public_random))]
    public entry fun solve(
        vault: &mut Vault<OTTER>,
        board: &mut QuestBoard,
        player: &mut Player,
        r: &Random,
        ctx: &mut TxContext,
    ) {
        buy_sword(vault, player, ctx);
        find_a_monster(board, r, ctx);
        fight_monster(board, player, 0);
        return_home(board, 0);
        
        let mut i = 0;
        while (i < 100) {
            find_a_monster(board, r, ctx);
            get_the_reward(vault, board, player, 0, ctx);
            i = i + 1;
        };

        let flag = buy_flag(vault, player, ctx);
        prove(board, flag);
    }
    
}
```
