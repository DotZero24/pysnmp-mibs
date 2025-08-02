_I='trapAdapterActivityCause'
_H='trapCauseDirection'
_G='trapTeamName'
_F='trapAdapterName'
_E='NotificationType'
_D='Integer32'
_C='mandatory'
_B='read-only'
_A='QLGC-QLASPTrap-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Qlogic_ObjectIdentity=ObjectIdentity
qlogic=_Qlogic_ObjectIdentity((1,3,6,1,4,1,3873))
_Enet_ObjectIdentity=ObjectIdentity
enet=_Enet_ObjectIdentity((1,3,6,1,4,1,3873,1))
_Qlasp_ObjectIdentity=ObjectIdentity
qlasp=_Qlasp_ObjectIdentity((1,3,6,1,4,1,3873,1,2))
_QlaspConfig_ObjectIdentity=ObjectIdentity
qlaspConfig=_QlaspConfig_ObjectIdentity((1,3,6,1,4,1,3873,1,2,1))
_QlaspStat_ObjectIdentity=ObjectIdentity
qlaspStat=_QlaspStat_ObjectIdentity((1,3,6,1,4,1,3873,1,2,2))
_QlaspTrap_ObjectIdentity=ObjectIdentity
qlaspTrap=_QlaspTrap_ObjectIdentity((1,3,6,1,4,1,3873,1,2,3))
_TrapAdapterName_Type=DisplayString
_TrapAdapterName_Object=MibScalar
trapAdapterName=_TrapAdapterName_Object((1,3,6,1,4,1,3873,1,2,3,1),_TrapAdapterName_Type())
trapAdapterName.setMaxAccess(_B)
if mibBuilder.loadTexts:trapAdapterName.setStatus(_C)
_TrapTeamName_Type=DisplayString
_TrapTeamName_Object=MibScalar
trapTeamName=_TrapTeamName_Object((1,3,6,1,4,1,3873,1,2,3,2),_TrapTeamName_Type())
trapTeamName.setMaxAccess(_B)
if mibBuilder.loadTexts:trapTeamName.setStatus(_C)
class _TrapCauseDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adapterActive',1),('adapterInactive',2)))
_TrapCauseDirection_Type.__name__=_D
_TrapCauseDirection_Object=MibScalar
trapCauseDirection=_TrapCauseDirection_Object((1,3,6,1,4,1,3873,1,2,3,3),_TrapCauseDirection_Type())
trapCauseDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:trapCauseDirection.setStatus(_C)
class _TrapAdapterActivityCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('linkChange',2),('adapterEnabledOrDisabled',3),('adapterAddedOrRemoved',4)))
_TrapAdapterActivityCause_Type.__name__=_D
_TrapAdapterActivityCause_Object=MibScalar
trapAdapterActivityCause=_TrapAdapterActivityCause_Object((1,3,6,1,4,1,3873,1,2,3,4),_TrapAdapterActivityCause_Type())
trapAdapterActivityCause.setMaxAccess(_B)
if mibBuilder.loadTexts:trapAdapterActivityCause.setStatus(_C)
failoverEvent=NotificationType((1,3,6,1,4,1,3873,1,2,3,0,1))
failoverEvent.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:failoverEvent.setStatus('')
mibBuilder.exportSymbols(_A,**{'qlogic':qlogic,'enet':enet,'qlasp':qlasp,'qlaspConfig':qlaspConfig,'qlaspStat':qlaspStat,'qlaspTrap':qlaspTrap,'failoverEvent':failoverEvent,_F:trapAdapterName,_G:trapTeamName,_H:trapCauseDirection,_I:trapAdapterActivityCause})