# Information related to modding Trails of Cold Steel

## Effects

Magic (i.e. arts and crafts), items, and quartzes have effects (for example: damage, healing, status effects) associated with them.
Some effects only work when applied to items, some only work on quartzes, and some work "everywhere".
Effects can have up to three parameters (two in CS1).
Some effect IDs and their functions also change from one game to the next.

We attempt to document the effects and their parameters in these tables:

- [effects for CS1](cs1_effects.csv)
- [effects for CS2](cs2_effects.csv)
- [effects for CS3](cs3_effects.csv)

If you notice a mistake or find anything new, please file an issue or prepare a pull request.

For effects that inflict status ailments:

- The first parameter is the activation chance in percent (before target resistance).
  In CS3 and later, if this value is 1000, target resistance is ignored and the effect is guaranteed to take effect (e.g. absolute delay on Gaius' S-Craft)
- The second parameter is the number of turns.
  If the value is zero, a fallback value will be used (depends on the ailment).

For effects that inflict stat buffs and debuffs:

- The first parameter is the added/subtracted amount in percent.
  In CS3 and later, some values are special: 999991, 999992, and 999993 describe (S), (M), and (L) buffs/debuffs, respectively.
- The second parameter is the number of turns
- The third value is the chance in percent (before target resistance, only for debuffs)

## Battle scripts

Battle scripts (under `scripts/battle`) contain a list of actions available to the enemy (`ActionTable`) and a list of priorities (`AlgoTable`).
On an enemy's turn, the game goes through the `AlgoTable` entries in order.
When an action is possible (e.g. the enemy is not sealed), a precondition in the `AlgoTable` is checked (e.g. turn count greater than some value).
If the condition is true, the enemy makes that move with some probability (also listed in the `AlgoTable`).
Otherwise the game continues checking the next action.
Some conditions can also make a character act out of turn order.

The `AlgoTable` also contains different target priorities (distinct from target type of the move), for example "target the closest party member".

- Reverie:
  - [known conditions and condition parameters](./reverie-algotable-conditions.csv)
  - [turn bonus ids for condition 3](./reverie-algotable-atbonus.csv)
  - [status bitflags for condition 8/9](./reverie-algotable-status.csv)
  - [known target priorities](./reverie-algotable-target-priorities.csv)
