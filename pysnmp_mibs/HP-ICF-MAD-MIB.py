_M='hpicfMadLacpAggStatisticsGroup'
_L='hpicfMadLacpAggConfigGroup'
_K='hpicfMadPassthroughLacpAggPDUsDropped'
_J='hpicfMadPassthroughLacpAggPDUsTx'
_I='hpicfMadPassthroughLacpAggPDUsRx'
_H='hpicfMadPassthroughLacpAggAdminStatus'
_G='hpicfMadLacpAggPortIndex'
_F='not-accessible'
_E='hpicfMadLacpAggTrunkId'
_D='read-only'
_C='Integer32'
_B='HP-ICF-MAD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfMadMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,95))
if mibBuilder.loadTexts:hpicfMadMIB.setRevisions(('2012-12-12 00:00',))
_HpicfMadNotifications_ObjectIdentity=ObjectIdentity
hpicfMadNotifications=_HpicfMadNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,95,0))
_HpicfMadObjects_ObjectIdentity=ObjectIdentity
hpicfMadObjects=_HpicfMadObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,95,1))
_HpicfMadLacpAggObjects_ObjectIdentity=ObjectIdentity
hpicfMadLacpAggObjects=_HpicfMadLacpAggObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1))
_HpicfMadLacpAggTable_Object=MibTable
hpicfMadLacpAggTable=_HpicfMadLacpAggTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1,1))
if mibBuilder.loadTexts:hpicfMadLacpAggTable.setStatus(_A)
_HpicfMadLacpAggEntry_Object=MibTableRow
hpicfMadLacpAggEntry=_HpicfMadLacpAggEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1,1,1))
hpicfMadLacpAggEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpicfMadLacpAggEntry.setStatus(_A)
class _HpicfMadLacpAggTrunkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfMadLacpAggTrunkId_Type.__name__=_C
_HpicfMadLacpAggTrunkId_Object=MibTableColumn
hpicfMadLacpAggTrunkId=_HpicfMadLacpAggTrunkId_Object((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1,1,1,1),_HpicfMadLacpAggTrunkId_Type())
hpicfMadLacpAggTrunkId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfMadLacpAggTrunkId.setStatus(_A)
class _HpicfMadPassthroughLacpAggAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpicfMadPassthroughLacpAggAdminStatus_Type.__name__=_C
_HpicfMadPassthroughLacpAggAdminStatus_Object=MibTableColumn
hpicfMadPassthroughLacpAggAdminStatus=_HpicfMadPassthroughLacpAggAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1,1,1,2),_HpicfMadPassthroughLacpAggAdminStatus_Type())
hpicfMadPassthroughLacpAggAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfMadPassthroughLacpAggAdminStatus.setStatus(_A)
_HpicfMadLacpAggPortStatsTable_Object=MibTable
hpicfMadLacpAggPortStatsTable=_HpicfMadLacpAggPortStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1,2))
if mibBuilder.loadTexts:hpicfMadLacpAggPortStatsTable.setStatus(_A)
_HpicfMadLacpAggPortStatsEntry_Object=MibTableRow
hpicfMadLacpAggPortStatsEntry=_HpicfMadLacpAggPortStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1,2,1))
hpicfMadLacpAggPortStatsEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpicfMadLacpAggPortStatsEntry.setStatus(_A)
_HpicfMadLacpAggPortIndex_Type=InterfaceIndex
_HpicfMadLacpAggPortIndex_Object=MibTableColumn
hpicfMadLacpAggPortIndex=_HpicfMadLacpAggPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1,2,1,1),_HpicfMadLacpAggPortIndex_Type())
hpicfMadLacpAggPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfMadLacpAggPortIndex.setStatus(_A)
_HpicfMadPassthroughLacpAggPDUsRx_Type=Counter32
_HpicfMadPassthroughLacpAggPDUsRx_Object=MibTableColumn
hpicfMadPassthroughLacpAggPDUsRx=_HpicfMadPassthroughLacpAggPDUsRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1,2,1,2),_HpicfMadPassthroughLacpAggPDUsRx_Type())
hpicfMadPassthroughLacpAggPDUsRx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMadPassthroughLacpAggPDUsRx.setStatus(_A)
_HpicfMadPassthroughLacpAggPDUsTx_Type=Counter32
_HpicfMadPassthroughLacpAggPDUsTx_Object=MibTableColumn
hpicfMadPassthroughLacpAggPDUsTx=_HpicfMadPassthroughLacpAggPDUsTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1,2,1,3),_HpicfMadPassthroughLacpAggPDUsTx_Type())
hpicfMadPassthroughLacpAggPDUsTx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMadPassthroughLacpAggPDUsTx.setStatus(_A)
_HpicfMadPassthroughLacpAggPDUsDropped_Type=Counter32
_HpicfMadPassthroughLacpAggPDUsDropped_Object=MibTableColumn
hpicfMadPassthroughLacpAggPDUsDropped=_HpicfMadPassthroughLacpAggPDUsDropped_Object((1,3,6,1,4,1,11,2,14,11,5,1,95,1,1,2,1,4),_HpicfMadPassthroughLacpAggPDUsDropped_Type())
hpicfMadPassthroughLacpAggPDUsDropped.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMadPassthroughLacpAggPDUsDropped.setStatus(_A)
_HpicfMadConformance_ObjectIdentity=ObjectIdentity
hpicfMadConformance=_HpicfMadConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,95,2))
_HpicfMadLacpAggGoups_ObjectIdentity=ObjectIdentity
hpicfMadLacpAggGoups=_HpicfMadLacpAggGoups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,95,2,1))
_HpicfMadLacpAggCompliances_ObjectIdentity=ObjectIdentity
hpicfMadLacpAggCompliances=_HpicfMadLacpAggCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,95,2,2))
hpicfMadLacpAggConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,95,2,1,1))
hpicfMadLacpAggConfigGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:hpicfMadLacpAggConfigGroup.setStatus(_A)
hpicfMadLacpAggStatisticsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,95,2,1,2))
hpicfMadLacpAggStatisticsGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:hpicfMadLacpAggStatisticsGroup.setStatus(_A)
hpicfMadLacpAggCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,95,2,2,1))
hpicfMadLacpAggCompliance1.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:hpicfMadLacpAggCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfMadMIB':hpicfMadMIB,'hpicfMadNotifications':hpicfMadNotifications,'hpicfMadObjects':hpicfMadObjects,'hpicfMadLacpAggObjects':hpicfMadLacpAggObjects,'hpicfMadLacpAggTable':hpicfMadLacpAggTable,'hpicfMadLacpAggEntry':hpicfMadLacpAggEntry,_E:hpicfMadLacpAggTrunkId,_H:hpicfMadPassthroughLacpAggAdminStatus,'hpicfMadLacpAggPortStatsTable':hpicfMadLacpAggPortStatsTable,'hpicfMadLacpAggPortStatsEntry':hpicfMadLacpAggPortStatsEntry,_G:hpicfMadLacpAggPortIndex,_I:hpicfMadPassthroughLacpAggPDUsRx,_J:hpicfMadPassthroughLacpAggPDUsTx,_K:hpicfMadPassthroughLacpAggPDUsDropped,'hpicfMadConformance':hpicfMadConformance,'hpicfMadLacpAggGoups':hpicfMadLacpAggGoups,_L:hpicfMadLacpAggConfigGroup,_M:hpicfMadLacpAggStatisticsGroup,'hpicfMadLacpAggCompliances':hpicfMadLacpAggCompliances,'hpicfMadLacpAggCompliance1':hpicfMadLacpAggCompliance1})