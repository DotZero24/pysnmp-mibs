_F='read-write'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkArpInspectionMIBObjects,=mibBuilder.importSymbols('TPLINK-ARP-INSPECTION-MIB','tplinkArpInspectionMIBObjects')
_TpArpDefend_ObjectIdentity=ObjectIdentity
tpArpDefend=_TpArpDefend_ObjectIdentity((1,3,6,1,4,1,11863,6,28,1,2))
_TpArpDefendConfig_ObjectIdentity=ObjectIdentity
tpArpDefendConfig=_TpArpDefendConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,28,1,2,1))
_TpArpDefendConfigTable_Object=MibTable
tpArpDefendConfigTable=_TpArpDefendConfigTable_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1))
if mibBuilder.loadTexts:tpArpDefendConfigTable.setStatus(_A)
_TpArpDefendConfigEntry_Object=MibTableRow
tpArpDefendConfigEntry=_TpArpDefendConfigEntry_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1,1))
tpArpDefendConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:tpArpDefendConfigEntry.setStatus(_A)
_TpArpDefendConfigPort_Type=OctetString
_TpArpDefendConfigPort_Object=MibTableColumn
tpArpDefendConfigPort=_TpArpDefendConfigPort_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1,1,1),_TpArpDefendConfigPort_Type())
tpArpDefendConfigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpArpDefendConfigPort.setStatus(_A)
class _TpArpDefendConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_TpArpDefendConfigEnable_Type.__name__=_E
_TpArpDefendConfigEnable_Object=MibTableColumn
tpArpDefendConfigEnable=_TpArpDefendConfigEnable_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1,1,2),_TpArpDefendConfigEnable_Type())
tpArpDefendConfigEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:tpArpDefendConfigEnable.setStatus(_A)
_TpArpDefendConfigRate_Type=Integer32
_TpArpDefendConfigRate_Object=MibTableColumn
tpArpDefendConfigRate=_TpArpDefendConfigRate_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1,1,3),_TpArpDefendConfigRate_Type())
tpArpDefendConfigRate.setMaxAccess(_F)
if mibBuilder.loadTexts:tpArpDefendConfigRate.setStatus(_A)
_TpArpDefendConfigState_Type=OctetString
_TpArpDefendConfigState_Object=MibTableColumn
tpArpDefendConfigState=_TpArpDefendConfigState_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1,1,4),_TpArpDefendConfigState_Type())
tpArpDefendConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:tpArpDefendConfigState.setStatus(_A)
_TpArpDefendConfigPortLag_Type=OctetString
_TpArpDefendConfigPortLag_Object=MibTableColumn
tpArpDefendConfigPortLag=_TpArpDefendConfigPortLag_Object((1,3,6,1,4,1,11863,6,28,1,2,1,1,1,5),_TpArpDefendConfigPortLag_Type())
tpArpDefendConfigPortLag.setMaxAccess(_B)
if mibBuilder.loadTexts:tpArpDefendConfigPortLag.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-ARP-DEFEND-MIB',**{'tpArpDefend':tpArpDefend,'tpArpDefendConfig':tpArpDefendConfig,'tpArpDefendConfigTable':tpArpDefendConfigTable,'tpArpDefendConfigEntry':tpArpDefendConfigEntry,'tpArpDefendConfigPort':tpArpDefendConfigPort,'tpArpDefendConfigEnable':tpArpDefendConfigEnable,'tpArpDefendConfigRate':tpArpDefendConfigRate,'tpArpDefendConfigState':tpArpDefendConfigState,'tpArpDefendConfigPortLag':tpArpDefendConfigPortLag})