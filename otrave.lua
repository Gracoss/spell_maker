-- SpellCreator generated.
local baseDamage = xxxx --Base Damage of the Spell
local levelMult = xxxx --Multiplier for the level
local magiclvlMult = xxxx --Multiplier for Magic Level
local offset = xxxx --This adds randomness to the formula. NO RNG = 1

local combat1_Brush = Combat()
combat1_Brush:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_DRAWBLOOD)
combat1_Brush:setParameter(COMBAT_PARAM_TYPE, COMBAT_PHYSICALDAMAGE)
combat1_Brush:setArea(createCombatArea({
{1, 0, 0, 0},
{1, 1, 0, 0},
{1, 0, 1, 2},
{1, 0, 1, 0},
{1, 1, 0, 0},
{1, 0, 0, 0}
}))

function getDmg_combat1_Brush(cid, level, maglevel)
	return baseDamage + math.pow(level, levelMult) + math.pow(maglevel, magiclvlMult) + math.random(level + offset)
end
combat1_Brush:setCallback(CALLBACK_PARAM_LEVELMAGICVALUE, "getDmg_combat1_Brush")

local combat2_Brush = Combat()
combat2_Brush:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_DRAWBLOOD)
combat2_Brush:setParameter(COMBAT_PARAM_TYPE, COMBAT_PHYSICALDAMAGE)
combat2_Brush:setArea(createCombatArea({
{0, 0, 0, 0, 1},
{0, 0, 0, 1, 1},
{0, 0, 1, 0, 1},
{0, 1, 0, 0, 1},
{0, 1, 0, 0, 1},
{2, 1, 0, 0, 1},
{0, 1, 0, 0, 1},
{0, 0, 1, 0, 1},
{0, 0, 0, 1, 1},
{0, 0, 0, 0, 1}
}))

function getDmg_combat2_Brush(cid, level, maglevel)
	return baseDamage + math.pow(level, levelMult) + math.pow(maglevel, magiclvlMult) + math.random(level + offset)
end
combat2_Brush:setCallback(CALLBACK_PARAM_LEVELMAGICVALUE, "getDmg_combat2_Brush")

-- =============== CORE FUNCTIONS ===============
local function RunPart(c,cid,var,dirList,dirEmitPos) -- Part
	if (Creature(cid):isCreature(cid)) then
		c:execute(cid, var)
		if (dirList ~= nil) then -- Emit distance effects
			local i = 2;
			while (i < #dirList) do
				dirEmitPos:sendDistanceEffect({x=dirEmitPos.x-dirList[i],y=dirEmitPos.y-dirList[i+1],z=dirEmitPos.z},dirList[1])
				i = i + 2
			end
		end
	end
end

local spell = Spell("instant")

function spell.onCastSpell(creature, var)
	local startPos = creature:getPosition(cid)
	local creatureId = creature:getId()
	RunPart(combat2_Brush, creatureId, var, startPos)
	addEvent(RunPart, 100 * 1, combat1_Brush, creatureId, var, startPos)
	return true
end

-- Spell properties
spell:group("attack", "focus")
spell:id(654)
spell:name("otrave")
spell:words("otra")
spell:level(1000)
spell:mana(100)
spell:isPremium(true)
spell:isSelfTarget(false)
spell:cooldown(1)
spell:groupCooldown(1)
spell:needLearn(false)
spell:vocation("druid;true", "elder druid;true", "knight;true", "elite knight;true", "sorcerer;true", "master sorcerer;true", "paladin;true", "royal paladin;true")
spell:register()
