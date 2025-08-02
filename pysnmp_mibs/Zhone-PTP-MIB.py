_a='zhonePtpConfigAcceptableMaster2'
_Z='zhonePtpConfigAcceptableMaster1'
_Y='zhonePtpConfigDomain1MS'
_X='zhonePtpConfigDomain2M'
_W='zhonePtpStatusMacAddress'
_V='zhonePtpStatusTxMode'
_U='zhonePtpConfigRowStatus'
_T='zhonePtpConfigPriority2'
_S='zhonePtpConfigPriority1'
_R='zhonePtpConfigVariance'
_Q='zhonePtpConfigClockAccuracy'
_P='zhonePtpConfigClockStratum'
_O='zhonePtpConfigTimeSource'
_N='zhonePtpConfigDelayReqInterval'
_M='zhonePtpConfigAnnounceInterval'
_L='zhonePtpConfigSyncMsgInterval'
_K='zhonePtpConfigIpIfIndex'
_J='zhonePtpConfigClockMode'
_I='00000000'
_H='zhonePtpConfigIfIndex'
_G='IpAddress'
_F='read-only'
_E='Unsigned32'
_D='Integer32'
_C='read-create'
_B='Zhone-PTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_G,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
zhoneGroups,zhoneModules,zhonePtp,zhoneShelfSlotGroup=mibBuilder.importSymbols('Zhone','zhoneGroups','zhoneModules','zhonePtp','zhoneShelfSlotGroup')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
zhonePtpModule=ModuleIdentity((1,3,6,1,4,1,5504,6,119))
if mibBuilder.loadTexts:zhonePtpModule.setRevisions(('2013-05-09 15:15','2012-01-13 14:50'))
_ZhonePtpObjectID_ObjectIdentity=ObjectIdentity
zhonePtpObjectID=_ZhonePtpObjectID_ObjectIdentity((1,3,6,1,4,1,5504,4,17,1))
_ZhonePtpConfigTable_Object=MibTable
zhonePtpConfigTable=_ZhonePtpConfigTable_Object((1,3,6,1,4,1,5504,4,17,1,1))
if mibBuilder.loadTexts:zhonePtpConfigTable.setStatus(_A)
_ZhonePtpConfigEntry_Object=MibTableRow
zhonePtpConfigEntry=_ZhonePtpConfigEntry_Object((1,3,6,1,4,1,5504,4,17,1,1,1))
zhonePtpConfigEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:zhonePtpConfigEntry.setStatus(_A)
_ZhonePtpConfigIfIndex_Type=InterfaceIndex
_ZhonePtpConfigIfIndex_Object=MibTableColumn
zhonePtpConfigIfIndex=_ZhonePtpConfigIfIndex_Object((1,3,6,1,4,1,5504,4,17,1,1,1,1),_ZhonePtpConfigIfIndex_Type())
zhonePtpConfigIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zhonePtpConfigIfIndex.setStatus(_A)
class _ZhonePtpConfigClockMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('master',1),('slave',2),('boundary',3),('transparent',4),('forward',5)))
_ZhonePtpConfigClockMode_Type.__name__=_D
_ZhonePtpConfigClockMode_Object=MibTableColumn
zhonePtpConfigClockMode=_ZhonePtpConfigClockMode_Object((1,3,6,1,4,1,5504,4,17,1,1,1,2),_ZhonePtpConfigClockMode_Type())
zhonePtpConfigClockMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigClockMode.setStatus(_A)
class _ZhonePtpConfigSyncMsgInterval_Type(Integer32):defaultValue=-5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_ZhonePtpConfigSyncMsgInterval_Type.__name__=_D
_ZhonePtpConfigSyncMsgInterval_Object=MibTableColumn
zhonePtpConfigSyncMsgInterval=_ZhonePtpConfigSyncMsgInterval_Object((1,3,6,1,4,1,5504,4,17,1,1,1,3),_ZhonePtpConfigSyncMsgInterval_Type())
zhonePtpConfigSyncMsgInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigSyncMsgInterval.setStatus(_A)
class _ZhonePtpConfigAnnounceInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_ZhonePtpConfigAnnounceInterval_Type.__name__=_D
_ZhonePtpConfigAnnounceInterval_Object=MibTableColumn
zhonePtpConfigAnnounceInterval=_ZhonePtpConfigAnnounceInterval_Object((1,3,6,1,4,1,5504,4,17,1,1,1,4),_ZhonePtpConfigAnnounceInterval_Type())
zhonePtpConfigAnnounceInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigAnnounceInterval.setStatus(_A)
class _ZhonePtpConfigDelayReqInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_ZhonePtpConfigDelayReqInterval_Type.__name__=_D
_ZhonePtpConfigDelayReqInterval_Object=MibTableColumn
zhonePtpConfigDelayReqInterval=_ZhonePtpConfigDelayReqInterval_Object((1,3,6,1,4,1,5504,4,17,1,1,1,5),_ZhonePtpConfigDelayReqInterval_Type())
zhonePtpConfigDelayReqInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigDelayReqInterval.setStatus(_A)
class _ZhonePtpConfigDomain1MS_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZhonePtpConfigDomain1MS_Type.__name__=_E
_ZhonePtpConfigDomain1MS_Object=MibTableColumn
zhonePtpConfigDomain1MS=_ZhonePtpConfigDomain1MS_Object((1,3,6,1,4,1,5504,4,17,1,1,1,6),_ZhonePtpConfigDomain1MS_Type())
zhonePtpConfigDomain1MS.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigDomain1MS.setStatus(_A)
class _ZhonePtpConfigVariance_Type(Unsigned32):defaultValue=32767;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZhonePtpConfigVariance_Type.__name__=_E
_ZhonePtpConfigVariance_Object=MibTableColumn
zhonePtpConfigVariance=_ZhonePtpConfigVariance_Object((1,3,6,1,4,1,5504,4,17,1,1,1,7),_ZhonePtpConfigVariance_Type())
zhonePtpConfigVariance.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigVariance.setStatus(_A)
class _ZhonePtpConfigPriority1_Type(Unsigned32):defaultValue=128;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZhonePtpConfigPriority1_Type.__name__=_E
_ZhonePtpConfigPriority1_Object=MibTableColumn
zhonePtpConfigPriority1=_ZhonePtpConfigPriority1_Object((1,3,6,1,4,1,5504,4,17,1,1,1,8),_ZhonePtpConfigPriority1_Type())
zhonePtpConfigPriority1.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigPriority1.setStatus(_A)
class _ZhonePtpConfigPriority2_Type(Unsigned32):defaultValue=128;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZhonePtpConfigPriority2_Type.__name__=_E
_ZhonePtpConfigPriority2_Object=MibTableColumn
zhonePtpConfigPriority2=_ZhonePtpConfigPriority2_Object((1,3,6,1,4,1,5504,4,17,1,1,1,9),_ZhonePtpConfigPriority2_Type())
zhonePtpConfigPriority2.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigPriority2.setStatus(_A)
class _ZhonePtpConfigDomain2M_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZhonePtpConfigDomain2M_Type.__name__=_D
_ZhonePtpConfigDomain2M_Object=MibTableColumn
zhonePtpConfigDomain2M=_ZhonePtpConfigDomain2M_Object((1,3,6,1,4,1,5504,4,17,1,1,1,10),_ZhonePtpConfigDomain2M_Type())
zhonePtpConfigDomain2M.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigDomain2M.setStatus(_A)
_ZhonePtpConfigRowStatus_Type=ZhoneRowStatus
_ZhonePtpConfigRowStatus_Object=MibTableColumn
zhonePtpConfigRowStatus=_ZhonePtpConfigRowStatus_Object((1,3,6,1,4,1,5504,4,17,1,1,1,11),_ZhonePtpConfigRowStatus_Type())
zhonePtpConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigRowStatus.setStatus(_A)
_ZhonePtpConfigIpIfIndex_Type=InterfaceIndex
_ZhonePtpConfigIpIfIndex_Object=MibTableColumn
zhonePtpConfigIpIfIndex=_ZhonePtpConfigIpIfIndex_Object((1,3,6,1,4,1,5504,4,17,1,1,1,12),_ZhonePtpConfigIpIfIndex_Type())
zhonePtpConfigIpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigIpIfIndex.setStatus(_A)
class _ZhonePtpConfigAcceptableMaster1_Type(IpAddress):defaultHexValue=_I
_ZhonePtpConfigAcceptableMaster1_Type.__name__=_G
_ZhonePtpConfigAcceptableMaster1_Object=MibTableColumn
zhonePtpConfigAcceptableMaster1=_ZhonePtpConfigAcceptableMaster1_Object((1,3,6,1,4,1,5504,4,17,1,1,1,13),_ZhonePtpConfigAcceptableMaster1_Type())
zhonePtpConfigAcceptableMaster1.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigAcceptableMaster1.setStatus(_A)
class _ZhonePtpConfigAcceptableMaster2_Type(IpAddress):defaultHexValue=_I
_ZhonePtpConfigAcceptableMaster2_Type.__name__=_G
_ZhonePtpConfigAcceptableMaster2_Object=MibTableColumn
zhonePtpConfigAcceptableMaster2=_ZhonePtpConfigAcceptableMaster2_Object((1,3,6,1,4,1,5504,4,17,1,1,1,14),_ZhonePtpConfigAcceptableMaster2_Type())
zhonePtpConfigAcceptableMaster2.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePtpConfigAcceptableMaster2.setStatus(_A)
_ZhonePtpStatusTable_Object=MibTable
zhonePtpStatusTable=_ZhonePtpStatusTable_Object((1,3,6,1,4,1,5504,4,17,1,2))
if mibBuilder.loadTexts:zhonePtpStatusTable.setStatus(_A)
_ZhonePtpStatusEntry_Object=MibTableRow
zhonePtpStatusEntry=_ZhonePtpStatusEntry_Object((1,3,6,1,4,1,5504,4,17,1,2,1))
zhonePtpStatusEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:zhonePtpStatusEntry.setStatus(_A)
_ZhonePtpStatusMacAddress_Type=MacAddress
_ZhonePtpStatusMacAddress_Object=MibTableColumn
zhonePtpStatusMacAddress=_ZhonePtpStatusMacAddress_Object((1,3,6,1,4,1,5504,4,17,1,2,1,1),_ZhonePtpStatusMacAddress_Type())
zhonePtpStatusMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:zhonePtpStatusMacAddress.setStatus(_A)
class _ZhonePtpConfigTimeSource_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('atom',1),('gps',2),('radio',3),('ptp',4),('ntp',5),('handSet',6),('other',7),('internalOscillator',8)))
_ZhonePtpConfigTimeSource_Type.__name__=_D
_ZhonePtpConfigTimeSource_Object=MibTableColumn
zhonePtpConfigTimeSource=_ZhonePtpConfigTimeSource_Object((1,3,6,1,4,1,5504,4,17,1,2,1,2),_ZhonePtpConfigTimeSource_Type())
zhonePtpConfigTimeSource.setMaxAccess(_F)
if mibBuilder.loadTexts:zhonePtpConfigTimeSource.setStatus(_A)
class _ZhonePtpConfigClockStratum_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('force',1),('primaryReference',2),('secondaryReference',3),('bestClockStratumThatCanBeSlave',4),('stratum3',5),('stratum4',6),('defaultStratum',7)))
_ZhonePtpConfigClockStratum_Type.__name__=_D
_ZhonePtpConfigClockStratum_Object=MibTableColumn
zhonePtpConfigClockStratum=_ZhonePtpConfigClockStratum_Object((1,3,6,1,4,1,5504,4,17,1,2,1,3),_ZhonePtpConfigClockStratum_Type())
zhonePtpConfigClockStratum.setMaxAccess(_F)
if mibBuilder.loadTexts:zhonePtpConfigClockStratum.setStatus(_A)
class _ZhonePtpConfigClockAccuracy_Type(Integer32):defaultValue=19;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('nSec25',1),('nSec100',2),('nSec250',3),('uSec1',4),('uSec2point5',5),('uSec10',6),('uSec25',7),('uSec100',8),('uSec250',9),('mSec1',10),('mSec2point5',11),('mSec10',12),('mSec25',13),('mSec100',14),('mSec250',15),('sec1',16),('sec10',17),('gT10S',18),('accUnknown',19)))
_ZhonePtpConfigClockAccuracy_Type.__name__=_D
_ZhonePtpConfigClockAccuracy_Object=MibTableColumn
zhonePtpConfigClockAccuracy=_ZhonePtpConfigClockAccuracy_Object((1,3,6,1,4,1,5504,4,17,1,2,1,4),_ZhonePtpConfigClockAccuracy_Type())
zhonePtpConfigClockAccuracy.setMaxAccess(_F)
if mibBuilder.loadTexts:zhonePtpConfigClockAccuracy.setStatus(_A)
class _ZhonePtpStatusTxMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standard',1),('uniOnly',2),('multiOnly',3)))
_ZhonePtpStatusTxMode_Type.__name__=_D
_ZhonePtpStatusTxMode_Object=MibTableColumn
zhonePtpStatusTxMode=_ZhonePtpStatusTxMode_Object((1,3,6,1,4,1,5504,4,17,1,2,1,5),_ZhonePtpStatusTxMode_Type())
zhonePtpStatusTxMode.setMaxAccess(_F)
if mibBuilder.loadTexts:zhonePtpStatusTxMode.setStatus(_A)
zhonePtpGroup=ObjectGroup((1,3,6,1,4,1,5504,9,1,52))
zhonePtpGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:zhonePtpGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zhonePtpObjectID':zhonePtpObjectID,'zhonePtpConfigTable':zhonePtpConfigTable,'zhonePtpConfigEntry':zhonePtpConfigEntry,_H:zhonePtpConfigIfIndex,_J:zhonePtpConfigClockMode,_L:zhonePtpConfigSyncMsgInterval,_M:zhonePtpConfigAnnounceInterval,_N:zhonePtpConfigDelayReqInterval,_Y:zhonePtpConfigDomain1MS,_R:zhonePtpConfigVariance,_S:zhonePtpConfigPriority1,_T:zhonePtpConfigPriority2,_X:zhonePtpConfigDomain2M,_U:zhonePtpConfigRowStatus,_K:zhonePtpConfigIpIfIndex,_Z:zhonePtpConfigAcceptableMaster1,_a:zhonePtpConfigAcceptableMaster2,'zhonePtpStatusTable':zhonePtpStatusTable,'zhonePtpStatusEntry':zhonePtpStatusEntry,_W:zhonePtpStatusMacAddress,_O:zhonePtpConfigTimeSource,_P:zhonePtpConfigClockStratum,_Q:zhonePtpConfigClockAccuracy,_V:zhonePtpStatusTxMode,'zhonePtpModule':zhonePtpModule,'zhonePtpGroup':zhonePtpGroup})