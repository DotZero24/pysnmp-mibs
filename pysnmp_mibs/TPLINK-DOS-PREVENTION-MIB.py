_H='read-only'
_G='tpDosDefendListIndex'
_F='TPLINK-DOS-PREVENTION-MIB'
_E='read-write'
_D='enable'
_C='disable'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkDosPreventionMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,30))
if mibBuilder.loadTexts:tplinkDosPreventionMIB.setRevisions(('2012-12-13 09:30',))
_TplinkDosPreventionMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDosPreventionMIBObjects=_TplinkDosPreventionMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,30,1))
_TpDosDefendGlobalConfig_ObjectIdentity=ObjectIdentity
tpDosDefendGlobalConfig=_TpDosDefendGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,30,1,1))
class _TpDosDefendGlobalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_TpDosDefendGlobalEnable_Type.__name__=_B
_TpDosDefendGlobalEnable_Object=MibScalar
tpDosDefendGlobalEnable=_TpDosDefendGlobalEnable_Object((1,3,6,1,4,1,11863,6,30,1,1,1),_TpDosDefendGlobalEnable_Type())
tpDosDefendGlobalEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:tpDosDefendGlobalEnable.setStatus(_A)
_TpDosDefendList_ObjectIdentity=ObjectIdentity
tpDosDefendList=_TpDosDefendList_ObjectIdentity((1,3,6,1,4,1,11863,6,30,1,2))
_TpDosDefendListTable_Object=MibTable
tpDosDefendListTable=_TpDosDefendListTable_Object((1,3,6,1,4,1,11863,6,30,1,2,1))
if mibBuilder.loadTexts:tpDosDefendListTable.setStatus(_A)
_TpDosDefendListEntry_Object=MibTableRow
tpDosDefendListEntry=_TpDosDefendListEntry_Object((1,3,6,1,4,1,11863,6,30,1,2,1,1))
tpDosDefendListEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:tpDosDefendListEntry.setStatus(_A)
_TpDosDefendListIndex_Type=Integer32
_TpDosDefendListIndex_Object=MibTableColumn
tpDosDefendListIndex=_TpDosDefendListIndex_Object((1,3,6,1,4,1,11863,6,30,1,2,1,1,1),_TpDosDefendListIndex_Type())
tpDosDefendListIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:tpDosDefendListIndex.setStatus(_A)
_TpDosDefendListType_Type=OctetString
_TpDosDefendListType_Object=MibTableColumn
tpDosDefendListType=_TpDosDefendListType_Object((1,3,6,1,4,1,11863,6,30,1,2,1,1,2),_TpDosDefendListType_Type())
tpDosDefendListType.setMaxAccess(_H)
if mibBuilder.loadTexts:tpDosDefendListType.setStatus(_A)
class _TpDosDefendListEntryEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),(_D,1)))
_TpDosDefendListEntryEnable_Type.__name__=_B
_TpDosDefendListEntryEnable_Object=MibTableColumn
tpDosDefendListEntryEnable=_TpDosDefendListEntryEnable_Object((1,3,6,1,4,1,11863,6,30,1,2,1,1,3),_TpDosDefendListEntryEnable_Type())
tpDosDefendListEntryEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:tpDosDefendListEntryEnable.setStatus(_A)
_TplinkDosPreventionNotifications_ObjectIdentity=ObjectIdentity
tplinkDosPreventionNotifications=_TplinkDosPreventionNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,30,2))
mibBuilder.exportSymbols(_F,**{'tplinkDosPreventionMIB':tplinkDosPreventionMIB,'tplinkDosPreventionMIBObjects':tplinkDosPreventionMIBObjects,'tpDosDefendGlobalConfig':tpDosDefendGlobalConfig,'tpDosDefendGlobalEnable':tpDosDefendGlobalEnable,'tpDosDefendList':tpDosDefendList,'tpDosDefendListTable':tpDosDefendListTable,'tpDosDefendListEntry':tpDosDefendListEntry,_G:tpDosDefendListIndex,'tpDosDefendListType':tpDosDefendListType,'tpDosDefendListEntryEnable':tpDosDefendListEntryEnable,'tplinkDosPreventionNotifications':tplinkDosPreventionNotifications})