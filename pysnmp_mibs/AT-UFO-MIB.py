_G='atUfoAlarmState'
_F='atUfoCurrentState'
_E='atUfoPreviousState'
_D='atUfoVlanId'
_C='read-only'
_B='AT-UFO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
atUfo=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,605))
if mibBuilder.loadTexts:atUfo.setRevisions(('2018-09-20 00:00',))
_AtUfoTraps_ObjectIdentity=ObjectIdentity
atUfoTraps=_AtUfoTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,605,0))
_AtUfoTrapVariables_ObjectIdentity=ObjectIdentity
atUfoTrapVariables=_AtUfoTrapVariables_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,605,1))
_AtUfoVlanId_Type=Integer32
_AtUfoVlanId_Object=MibScalar
atUfoVlanId=_AtUfoVlanId_Object((1,3,6,1,4,1,207,8,4,4,4,605,1,1),_AtUfoVlanId_Type())
atUfoVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:atUfoVlanId.setStatus(_A)
_AtUfoPreviousState_Type=TruthValue
_AtUfoPreviousState_Object=MibScalar
atUfoPreviousState=_AtUfoPreviousState_Object((1,3,6,1,4,1,207,8,4,4,4,605,1,2),_AtUfoPreviousState_Type())
atUfoPreviousState.setMaxAccess(_C)
if mibBuilder.loadTexts:atUfoPreviousState.setStatus(_A)
_AtUfoCurrentState_Type=TruthValue
_AtUfoCurrentState_Object=MibScalar
atUfoCurrentState=_AtUfoCurrentState_Object((1,3,6,1,4,1,207,8,4,4,4,605,1,3),_AtUfoCurrentState_Type())
atUfoCurrentState.setMaxAccess(_C)
if mibBuilder.loadTexts:atUfoCurrentState.setStatus(_A)
_AtUfoAlarmState_Type=TruthValue
_AtUfoAlarmState_Object=MibScalar
atUfoAlarmState=_AtUfoAlarmState_Object((1,3,6,1,4,1,207,8,4,4,4,605,1,4),_AtUfoAlarmState_Type())
atUfoAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:atUfoAlarmState.setStatus(_A)
atUfoVlanBlackHoleTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,605,0,1))
atUfoVlanBlackHoleTrap.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:atUfoVlanBlackHoleTrap.setStatus(_A)
atUfoBlackHoleAlarmTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,605,0,2))
atUfoBlackHoleAlarmTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:atUfoBlackHoleAlarmTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'atUfo':atUfo,'atUfoTraps':atUfoTraps,'atUfoVlanBlackHoleTrap':atUfoVlanBlackHoleTrap,'atUfoBlackHoleAlarmTrap':atUfoBlackHoleAlarmTrap,'atUfoTrapVariables':atUfoTrapVariables,_D:atUfoVlanId,_E:atUfoPreviousState,_F:atUfoCurrentState,_G:atUfoAlarmState})