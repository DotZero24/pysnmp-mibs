_H='brcmIptvChanId'
_G='BRCM-IPTV-MIB'
_F='Integer32'
_E='read-write'
_D='DisplayString'
_C='Unsigned32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtMIBObjects,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtMIBObjects')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
brcmIptvMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,13))
if mibBuilder.loadTexts:brcmIptvMgmt.setRevisions(('2009-08-22 00:00',))
_IptvMgmtBase_ObjectIdentity=ObjectIdentity
iptvMgmtBase=_IptvMgmtBase_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,13,1))
_BrcmIptvChannelInfo_ObjectIdentity=ObjectIdentity
brcmIptvChannelInfo=_BrcmIptvChannelInfo_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,13,1,1))
class _BrcmIptvChannelTableDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrcmIptvChannelTableDescr_Type.__name__=_D
_BrcmIptvChannelTableDescr_Object=MibScalar
brcmIptvChannelTableDescr=_BrcmIptvChannelTableDescr_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,1),_BrcmIptvChannelTableDescr_Type())
brcmIptvChannelTableDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:brcmIptvChannelTableDescr.setStatus(_A)
_BrcmIptvChannelTableLastChange_Type=TimeTicks
_BrcmIptvChannelTableLastChange_Object=MibScalar
brcmIptvChannelTableLastChange=_BrcmIptvChannelTableLastChange_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,2),_BrcmIptvChannelTableLastChange_Type())
brcmIptvChannelTableLastChange.setMaxAccess('read-only')
if mibBuilder.loadTexts:brcmIptvChannelTableLastChange.setStatus(_A)
class _BrcmIptvChannelTableNotificationInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_BrcmIptvChannelTableNotificationInterval_Type.__name__=_F
_BrcmIptvChannelTableNotificationInterval_Object=MibScalar
brcmIptvChannelTableNotificationInterval=_BrcmIptvChannelTableNotificationInterval_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,3),_BrcmIptvChannelTableNotificationInterval_Type())
brcmIptvChannelTableNotificationInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:brcmIptvChannelTableNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:brcmIptvChannelTableNotificationInterval.setUnits('seconds')
_BrcmIptvChannelTableNotifyNow_Type=TruthValue
_BrcmIptvChannelTableNotifyNow_Object=MibScalar
brcmIptvChannelTableNotifyNow=_BrcmIptvChannelTableNotifyNow_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,4),_BrcmIptvChannelTableNotifyNow_Type())
brcmIptvChannelTableNotifyNow.setMaxAccess(_E)
if mibBuilder.loadTexts:brcmIptvChannelTableNotifyNow.setStatus(_A)
_BrcmIptvChannelTable_Object=MibTable
brcmIptvChannelTable=_BrcmIptvChannelTable_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5))
if mibBuilder.loadTexts:brcmIptvChannelTable.setStatus(_A)
_BrcmIptvChannelEntry_Object=MibTableRow
brcmIptvChannelEntry=_BrcmIptvChannelEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1))
brcmIptvChannelEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:brcmIptvChannelEntry.setStatus(_A)
class _BrcmIptvChanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrcmIptvChanId_Type.__name__=_C
_BrcmIptvChanId_Object=MibTableColumn
brcmIptvChanId=_BrcmIptvChanId_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,1),_BrcmIptvChanId_Type())
brcmIptvChanId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:brcmIptvChanId.setStatus(_A)
class _BrcmIptvChanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_BrcmIptvChanName_Type.__name__=_D
_BrcmIptvChanName_Object=MibTableColumn
brcmIptvChanName=_BrcmIptvChanName_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,2),_BrcmIptvChanName_Type())
brcmIptvChanName.setMaxAccess(_B)
if mibBuilder.loadTexts:brcmIptvChanName.setStatus(_A)
_BrcmIptvChanFreq_Type=Unsigned32
_BrcmIptvChanFreq_Object=MibTableColumn
brcmIptvChanFreq=_BrcmIptvChanFreq_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,3),_BrcmIptvChanFreq_Type())
brcmIptvChanFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:brcmIptvChanFreq.setStatus(_A)
class _BrcmIptvChanVideoPid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_BrcmIptvChanVideoPid_Type.__name__=_C
_BrcmIptvChanVideoPid_Object=MibTableColumn
brcmIptvChanVideoPid=_BrcmIptvChanVideoPid_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,4),_BrcmIptvChanVideoPid_Type())
brcmIptvChanVideoPid.setMaxAccess(_B)
if mibBuilder.loadTexts:brcmIptvChanVideoPid.setStatus(_A)
class _BrcmIptvChanAudioPid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_BrcmIptvChanAudioPid_Type.__name__=_C
_BrcmIptvChanAudioPid_Object=MibTableColumn
brcmIptvChanAudioPid=_BrcmIptvChanAudioPid_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,5),_BrcmIptvChanAudioPid_Type())
brcmIptvChanAudioPid.setMaxAccess(_B)
if mibBuilder.loadTexts:brcmIptvChanAudioPid.setStatus(_A)
class _BrcmIptvChanSecondaryAudioPid_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_BrcmIptvChanSecondaryAudioPid_Type.__name__=_C
_BrcmIptvChanSecondaryAudioPid_Object=MibTableColumn
brcmIptvChanSecondaryAudioPid=_BrcmIptvChanSecondaryAudioPid_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,6),_BrcmIptvChanSecondaryAudioPid_Type())
brcmIptvChanSecondaryAudioPid.setMaxAccess(_B)
if mibBuilder.loadTexts:brcmIptvChanSecondaryAudioPid.setStatus(_A)
class _BrcmIptvChanPmtPid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_BrcmIptvChanPmtPid_Type.__name__=_C
_BrcmIptvChanPmtPid_Object=MibTableColumn
brcmIptvChanPmtPid=_BrcmIptvChanPmtPid_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,7),_BrcmIptvChanPmtPid_Type())
brcmIptvChanPmtPid.setMaxAccess(_B)
if mibBuilder.loadTexts:brcmIptvChanPmtPid.setStatus(_A)
_BrcmIptvChanMcastGroupAddrType_Type=InetAddressType
_BrcmIptvChanMcastGroupAddrType_Object=MibTableColumn
brcmIptvChanMcastGroupAddrType=_BrcmIptvChanMcastGroupAddrType_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,8),_BrcmIptvChanMcastGroupAddrType_Type())
brcmIptvChanMcastGroupAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:brcmIptvChanMcastGroupAddrType.setStatus(_A)
_BrcmIptvChanMcastGroupAddr_Type=InetAddress
_BrcmIptvChanMcastGroupAddr_Object=MibTableColumn
brcmIptvChanMcastGroupAddr=_BrcmIptvChanMcastGroupAddr_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,9),_BrcmIptvChanMcastGroupAddr_Type())
brcmIptvChanMcastGroupAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:brcmIptvChanMcastGroupAddr.setStatus(_A)
_BrcmIptvChanPort_Type=Unsigned32
_BrcmIptvChanPort_Object=MibTableColumn
brcmIptvChanPort=_BrcmIptvChanPort_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,10),_BrcmIptvChanPort_Type())
brcmIptvChanPort.setMaxAccess(_B)
if mibBuilder.loadTexts:brcmIptvChanPort.setStatus(_A)
_BrcmIptvChanRowStatus_Type=RowStatus
_BrcmIptvChanRowStatus_Object=MibTableColumn
brcmIptvChanRowStatus=_BrcmIptvChanRowStatus_Object((1,3,6,1,4,1,4413,2,2,2,1,13,1,1,5,1,11),_BrcmIptvChanRowStatus_Type())
brcmIptvChanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brcmIptvChanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'brcmIptvMgmt':brcmIptvMgmt,'iptvMgmtBase':iptvMgmtBase,'brcmIptvChannelInfo':brcmIptvChannelInfo,'brcmIptvChannelTableDescr':brcmIptvChannelTableDescr,'brcmIptvChannelTableLastChange':brcmIptvChannelTableLastChange,'brcmIptvChannelTableNotificationInterval':brcmIptvChannelTableNotificationInterval,'brcmIptvChannelTableNotifyNow':brcmIptvChannelTableNotifyNow,'brcmIptvChannelTable':brcmIptvChannelTable,'brcmIptvChannelEntry':brcmIptvChannelEntry,_H:brcmIptvChanId,'brcmIptvChanName':brcmIptvChanName,'brcmIptvChanFreq':brcmIptvChanFreq,'brcmIptvChanVideoPid':brcmIptvChanVideoPid,'brcmIptvChanAudioPid':brcmIptvChanAudioPid,'brcmIptvChanSecondaryAudioPid':brcmIptvChanSecondaryAudioPid,'brcmIptvChanPmtPid':brcmIptvChanPmtPid,'brcmIptvChanMcastGroupAddrType':brcmIptvChanMcastGroupAddrType,'brcmIptvChanMcastGroupAddr':brcmIptvChanMcastGroupAddr,'brcmIptvChanPort':brcmIptvChanPort,'brcmIptvChanRowStatus':brcmIptvChanRowStatus})