_Q='tpVrrpStatsVid'
_P='tpVrrpStatsVrid'
_O='tpVrrpTrackInterface'
_N='tpVrrpTrackVid'
_M='tpVrrpTrackVrid'
_L='tpVrrpVirtualIpAddress'
_K='tpVrrpVirtualIpVid'
_J='tpVrrpVirtualIpVrid'
_I='tpVrrpVid'
_H='tpVrrpVrid'
_G='interfacevlan'
_F='routedport'
_E='read-create'
_D='TPLINK-VRRP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkVrrpMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,65))
if mibBuilder.loadTexts:tplinkVrrpMIB.setRevisions(('2012-12-13 00:00',))
_TplinkVrrpMIBObjects_ObjectIdentity=ObjectIdentity
tplinkVrrpMIBObjects=_TplinkVrrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,65,1))
_TpVrrpGlobalCtrl_ObjectIdentity=ObjectIdentity
tpVrrpGlobalCtrl=_TpVrrpGlobalCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,65,1,1))
_TpVrrpGlobalCtrlTable_Object=MibTable
tpVrrpGlobalCtrlTable=_TpVrrpGlobalCtrlTable_Object((1,3,6,1,4,1,11863,6,65,1,1,1))
if mibBuilder.loadTexts:tpVrrpGlobalCtrlTable.setStatus(_A)
_TpVrrpGlobalCtrlEntry_Object=MibTableRow
tpVrrpGlobalCtrlEntry=_TpVrrpGlobalCtrlEntry_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1))
tpVrrpGlobalCtrlEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:tpVrrpGlobalCtrlEntry.setStatus(_A)
class _TpVrrpVrid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpVrrpVrid_Type.__name__=_C
_TpVrrpVrid_Object=MibTableColumn
tpVrrpVrid=_TpVrrpVrid_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,1),_TpVrrpVrid_Type())
tpVrrpVrid.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpVrid.setStatus(_A)
_TpVrrpVid_Type=Integer32
_TpVrrpVid_Object=MibTableColumn
tpVrrpVid=_TpVrrpVid_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,2),_TpVrrpVid_Type())
tpVrrpVid.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpVid.setStatus(_A)
class _TpVrrpIntfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpVrrpIntfStatus_Type.__name__=_C
_TpVrrpIntfStatus_Object=MibTableColumn
tpVrrpIntfStatus=_TpVrrpIntfStatus_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,3),_TpVrrpIntfStatus_Type())
tpVrrpIntfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpIntfStatus.setStatus(_A)
_TpVrrpInterfaceIP_Type=IpAddress
_TpVrrpInterfaceIP_Object=MibTableColumn
tpVrrpInterfaceIP=_TpVrrpInterfaceIP_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,4),_TpVrrpInterfaceIP_Type())
tpVrrpInterfaceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpInterfaceIP.setStatus(_A)
_TpVrrpMacAddress_Type=OctetString
_TpVrrpMacAddress_Object=MibTableColumn
tpVrrpMacAddress=_TpVrrpMacAddress_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,5),_TpVrrpMacAddress_Type())
tpVrrpMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpMacAddress.setStatus(_A)
_TpVrrpDescription_Type=OctetString
_TpVrrpDescription_Object=MibTableColumn
tpVrrpDescription=_TpVrrpDescription_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,6),_TpVrrpDescription_Type())
tpVrrpDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpDescription.setStatus(_A)
_TpVrrpPrimaryVirtualIp_Type=IpAddress
_TpVrrpPrimaryVirtualIp_Object=MibTableColumn
tpVrrpPrimaryVirtualIp=_TpVrrpPrimaryVirtualIp_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,7),_TpVrrpPrimaryVirtualIp_Type())
tpVrrpPrimaryVirtualIp.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpPrimaryVirtualIp.setStatus(_A)
class _TpVrrpRunPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpVrrpRunPriority_Type.__name__=_C
_TpVrrpRunPriority_Object=MibTableColumn
tpVrrpRunPriority=_TpVrrpRunPriority_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,8),_TpVrrpRunPriority_Type())
tpVrrpRunPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpRunPriority.setStatus(_A)
class _TpVrrpConfigPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpVrrpConfigPriority_Type.__name__=_C
_TpVrrpConfigPriority_Object=MibTableColumn
tpVrrpConfigPriority=_TpVrrpConfigPriority_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,9),_TpVrrpConfigPriority_Type())
tpVrrpConfigPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpConfigPriority.setStatus(_A)
class _TpVrrpAdvertisement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpVrrpAdvertisement_Type.__name__=_C
_TpVrrpAdvertisement_Object=MibTableColumn
tpVrrpAdvertisement=_TpVrrpAdvertisement_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,10),_TpVrrpAdvertisement_Type())
tpVrrpAdvertisement.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpAdvertisement.setStatus(_A)
class _TpVrrpPreeptMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('enable',0),('disable',1)))
_TpVrrpPreeptMode_Type.__name__=_C
_TpVrrpPreeptMode_Object=MibTableColumn
tpVrrpPreeptMode=_TpVrrpPreeptMode_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,11),_TpVrrpPreeptMode_Type())
tpVrrpPreeptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpPreeptMode.setStatus(_A)
class _TpVrrpTimeDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpVrrpTimeDelay_Type.__name__=_C
_TpVrrpTimeDelay_Object=MibTableColumn
tpVrrpTimeDelay=_TpVrrpTimeDelay_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,12),_TpVrrpTimeDelay_Type())
tpVrrpTimeDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpTimeDelay.setStatus(_A)
class _TpVrrpAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),('simple',1),('md5',2)))
_TpVrrpAuthType_Type.__name__=_C
_TpVrrpAuthType_Object=MibTableColumn
tpVrrpAuthType=_TpVrrpAuthType_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,13),_TpVrrpAuthType_Type())
tpVrrpAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpAuthType.setStatus(_A)
_TpVrrpKey_Type=OctetString
_TpVrrpKey_Object=MibTableColumn
tpVrrpKey=_TpVrrpKey_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,14),_TpVrrpKey_Type())
tpVrrpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpKey.setStatus(_A)
class _TpVrrpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('initialize',0),('backup',1),('master',2)))
_TpVrrpState_Type.__name__=_C
_TpVrrpState_Object=MibTableColumn
tpVrrpState=_TpVrrpState_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,15),_TpVrrpState_Type())
tpVrrpState.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpState.setStatus(_A)
_TpVrrpStatus_Type=TPRowStatus
_TpVrrpStatus_Object=MibTableColumn
tpVrrpStatus=_TpVrrpStatus_Object((1,3,6,1,4,1,11863,6,65,1,1,1,1,16),_TpVrrpStatus_Type())
tpVrrpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpStatus.setStatus(_A)
_TpVrrpVirtualIpCtrl_ObjectIdentity=ObjectIdentity
tpVrrpVirtualIpCtrl=_TpVrrpVirtualIpCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,65,1,2))
_TpVrrpVirtualIpCtrlTable_Object=MibTable
tpVrrpVirtualIpCtrlTable=_TpVrrpVirtualIpCtrlTable_Object((1,3,6,1,4,1,11863,6,65,1,2,1))
if mibBuilder.loadTexts:tpVrrpVirtualIpCtrlTable.setStatus(_A)
_TpVrrpVirtualIpCtrlEntry_Object=MibTableRow
tpVrrpVirtualIpCtrlEntry=_TpVrrpVirtualIpCtrlEntry_Object((1,3,6,1,4,1,11863,6,65,1,2,1,1))
tpVrrpVirtualIpCtrlEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:tpVrrpVirtualIpCtrlEntry.setStatus(_A)
class _TpVrrpVirtualIpVrid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpVrrpVirtualIpVrid_Type.__name__=_C
_TpVrrpVirtualIpVrid_Object=MibTableColumn
tpVrrpVirtualIpVrid=_TpVrrpVirtualIpVrid_Object((1,3,6,1,4,1,11863,6,65,1,2,1,1,1),_TpVrrpVirtualIpVrid_Type())
tpVrrpVirtualIpVrid.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpVirtualIpVrid.setStatus(_A)
_TpVrrpVirtualIpVid_Type=Integer32
_TpVrrpVirtualIpVid_Object=MibTableColumn
tpVrrpVirtualIpVid=_TpVrrpVirtualIpVid_Object((1,3,6,1,4,1,11863,6,65,1,2,1,1,2),_TpVrrpVirtualIpVid_Type())
tpVrrpVirtualIpVid.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpVirtualIpVid.setStatus(_A)
class _TpVrrpVirtualIpintfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpVrrpVirtualIpintfStatus_Type.__name__=_C
_TpVrrpVirtualIpintfStatus_Object=MibTableColumn
tpVrrpVirtualIpintfStatus=_TpVrrpVirtualIpintfStatus_Object((1,3,6,1,4,1,11863,6,65,1,2,1,1,3),_TpVrrpVirtualIpintfStatus_Type())
tpVrrpVirtualIpintfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpVirtualIpintfStatus.setStatus(_A)
_TpVrrpVirtualIpAddress_Type=IpAddress
_TpVrrpVirtualIpAddress_Object=MibTableColumn
tpVrrpVirtualIpAddress=_TpVrrpVirtualIpAddress_Object((1,3,6,1,4,1,11863,6,65,1,2,1,1,4),_TpVrrpVirtualIpAddress_Type())
tpVrrpVirtualIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpVirtualIpAddress.setStatus(_A)
_TpVrrpVirtualIpStatus_Type=TPRowStatus
_TpVrrpVirtualIpStatus_Object=MibTableColumn
tpVrrpVirtualIpStatus=_TpVrrpVirtualIpStatus_Object((1,3,6,1,4,1,11863,6,65,1,2,1,1,5),_TpVrrpVirtualIpStatus_Type())
tpVrrpVirtualIpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpVirtualIpStatus.setStatus(_A)
_TpVrrpTrackCtrl_ObjectIdentity=ObjectIdentity
tpVrrpTrackCtrl=_TpVrrpTrackCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,65,1,3))
_TpVrrpTrackCtrlTable_Object=MibTable
tpVrrpTrackCtrlTable=_TpVrrpTrackCtrlTable_Object((1,3,6,1,4,1,11863,6,65,1,3,1))
if mibBuilder.loadTexts:tpVrrpTrackCtrlTable.setStatus(_A)
_TpVrrpTrackCtrlEntry_Object=MibTableRow
tpVrrpTrackCtrlEntry=_TpVrrpTrackCtrlEntry_Object((1,3,6,1,4,1,11863,6,65,1,3,1,1))
tpVrrpTrackCtrlEntry.setIndexNames((0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:tpVrrpTrackCtrlEntry.setStatus(_A)
class _TpVrrpTrackVrid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpVrrpTrackVrid_Type.__name__=_C
_TpVrrpTrackVrid_Object=MibTableColumn
tpVrrpTrackVrid=_TpVrrpTrackVrid_Object((1,3,6,1,4,1,11863,6,65,1,3,1,1,1),_TpVrrpTrackVrid_Type())
tpVrrpTrackVrid.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpTrackVrid.setStatus(_A)
_TpVrrpTrackVid_Type=Integer32
_TpVrrpTrackVid_Object=MibTableColumn
tpVrrpTrackVid=_TpVrrpTrackVid_Object((1,3,6,1,4,1,11863,6,65,1,3,1,1,2),_TpVrrpTrackVid_Type())
tpVrrpTrackVid.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpTrackVid.setStatus(_A)
class _TpVrrpTrackIntfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpVrrpTrackIntfStatus_Type.__name__=_C
_TpVrrpTrackIntfStatus_Object=MibTableColumn
tpVrrpTrackIntfStatus=_TpVrrpTrackIntfStatus_Object((1,3,6,1,4,1,11863,6,65,1,3,1,1,3),_TpVrrpTrackIntfStatus_Type())
tpVrrpTrackIntfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpTrackIntfStatus.setStatus(_A)
_TpVrrpTrackInterface_Type=Integer32
_TpVrrpTrackInterface_Object=MibTableColumn
tpVrrpTrackInterface=_TpVrrpTrackInterface_Object((1,3,6,1,4,1,11863,6,65,1,3,1,1,4),_TpVrrpTrackInterface_Type())
tpVrrpTrackInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpTrackInterface.setStatus(_A)
class _TpVrrpTrackIntfTrackedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpVrrpTrackIntfTrackedStatus_Type.__name__=_C
_TpVrrpTrackIntfTrackedStatus_Object=MibTableColumn
tpVrrpTrackIntfTrackedStatus=_TpVrrpTrackIntfTrackedStatus_Object((1,3,6,1,4,1,11863,6,65,1,3,1,1,5),_TpVrrpTrackIntfTrackedStatus_Type())
tpVrrpTrackIntfTrackedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpTrackIntfTrackedStatus.setStatus(_A)
class _TpVrrpTrackPriortiy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TpVrrpTrackPriortiy_Type.__name__=_C
_TpVrrpTrackPriortiy_Object=MibTableColumn
tpVrrpTrackPriortiy=_TpVrrpTrackPriortiy_Object((1,3,6,1,4,1,11863,6,65,1,3,1,1,6),_TpVrrpTrackPriortiy_Type())
tpVrrpTrackPriortiy.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpTrackPriortiy.setStatus(_A)
class _TpVrrpLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_TpVrrpLinkState_Type.__name__=_C
_TpVrrpLinkState_Object=MibTableColumn
tpVrrpLinkState=_TpVrrpLinkState_Object((1,3,6,1,4,1,11863,6,65,1,3,1,1,7),_TpVrrpLinkState_Type())
tpVrrpLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpLinkState.setStatus(_A)
_TpVrrpTrackStatus_Type=TPRowStatus
_TpVrrpTrackStatus_Object=MibTableColumn
tpVrrpTrackStatus=_TpVrrpTrackStatus_Object((1,3,6,1,4,1,11863,6,65,1,3,1,1,8),_TpVrrpTrackStatus_Type())
tpVrrpTrackStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpVrrpTrackStatus.setStatus(_A)
_TpVrrpStatistics_ObjectIdentity=ObjectIdentity
tpVrrpStatistics=_TpVrrpStatistics_ObjectIdentity((1,3,6,1,4,1,11863,6,65,1,4))
_TpVrrpChecksumErrors_Type=Integer32
_TpVrrpChecksumErrors_Object=MibScalar
tpVrrpChecksumErrors=_TpVrrpChecksumErrors_Object((1,3,6,1,4,1,11863,6,65,1,4,1),_TpVrrpChecksumErrors_Type())
tpVrrpChecksumErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpChecksumErrors.setStatus(_A)
_TpVrrpVersionErrors_Type=Integer32
_TpVrrpVersionErrors_Object=MibScalar
tpVrrpVersionErrors=_TpVrrpVersionErrors_Object((1,3,6,1,4,1,11863,6,65,1,4,2),_TpVrrpVersionErrors_Type())
tpVrrpVersionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpVersionErrors.setStatus(_A)
_TpVrrpVridErrors_Type=Integer32
_TpVrrpVridErrors_Object=MibScalar
tpVrrpVridErrors=_TpVrrpVridErrors_Object((1,3,6,1,4,1,11863,6,65,1,4,3),_TpVrrpVridErrors_Type())
tpVrrpVridErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpVridErrors.setStatus(_A)
_TpVrrpStatsTable_Object=MibTable
tpVrrpStatsTable=_TpVrrpStatsTable_Object((1,3,6,1,4,1,11863,6,65,1,4,4))
if mibBuilder.loadTexts:tpVrrpStatsTable.setStatus(_A)
_TpVrrpStatsEntry_Object=MibTableRow
tpVrrpStatsEntry=_TpVrrpStatsEntry_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1))
tpVrrpStatsEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:tpVrrpStatsEntry.setStatus(_A)
_TpVrrpStatsVrid_Type=Integer32
_TpVrrpStatsVrid_Object=MibTableColumn
tpVrrpStatsVrid=_TpVrrpStatsVrid_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,1),_TpVrrpStatsVrid_Type())
tpVrrpStatsVrid.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpStatsVrid.setStatus(_A)
_TpVrrpStatsVid_Type=Integer32
_TpVrrpStatsVid_Object=MibTableColumn
tpVrrpStatsVid=_TpVrrpStatsVid_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,2),_TpVrrpStatsVid_Type())
tpVrrpStatsVid.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpStatsVid.setStatus(_A)
class _TpVrrpStatsIntfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpVrrpStatsIntfStatus_Type.__name__=_C
_TpVrrpStatsIntfStatus_Object=MibTableColumn
tpVrrpStatsIntfStatus=_TpVrrpStatsIntfStatus_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,3),_TpVrrpStatsIntfStatus_Type())
tpVrrpStatsIntfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpStatsIntfStatus.setStatus(_A)
_TpVrrpChecksumErr_Type=Integer32
_TpVrrpChecksumErr_Object=MibTableColumn
tpVrrpChecksumErr=_TpVrrpChecksumErr_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,4),_TpVrrpChecksumErr_Type())
tpVrrpChecksumErr.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpChecksumErr.setStatus(_A)
_TpVrrpVersionErr_Type=Integer32
_TpVrrpVersionErr_Object=MibTableColumn
tpVrrpVersionErr=_TpVrrpVersionErr_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,5),_TpVrrpVersionErr_Type())
tpVrrpVersionErr.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpVersionErr.setStatus(_A)
_TpVrrpStatsBecomeMaster_Type=Integer32
_TpVrrpStatsBecomeMaster_Object=MibTableColumn
tpVrrpStatsBecomeMaster=_TpVrrpStatsBecomeMaster_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,6),_TpVrrpStatsBecomeMaster_Type())
tpVrrpStatsBecomeMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVrrpStatsBecomeMaster.setStatus(_A)
_TpvrrpStatsAdvertiseRcvd_Type=Integer32
_TpvrrpStatsAdvertiseRcvd_Object=MibTableColumn
tpvrrpStatsAdvertiseRcvd=_TpvrrpStatsAdvertiseRcvd_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,7),_TpvrrpStatsAdvertiseRcvd_Type())
tpvrrpStatsAdvertiseRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsAdvertiseRcvd.setStatus(_A)
_TpvrrpStatsAdvertiseSent_Type=Integer32
_TpvrrpStatsAdvertiseSent_Object=MibTableColumn
tpvrrpStatsAdvertiseSent=_TpvrrpStatsAdvertiseSent_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,8),_TpvrrpStatsAdvertiseSent_Type())
tpvrrpStatsAdvertiseSent.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsAdvertiseSent.setStatus(_A)
_TpvrrpStatsAdvertiseIntervalErrors_Type=Integer32
_TpvrrpStatsAdvertiseIntervalErrors_Object=MibTableColumn
tpvrrpStatsAdvertiseIntervalErrors=_TpvrrpStatsAdvertiseIntervalErrors_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,9),_TpvrrpStatsAdvertiseIntervalErrors_Type())
tpvrrpStatsAdvertiseIntervalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsAdvertiseIntervalErrors.setStatus(_A)
_TpvrrpStatsAuthFailures_Type=Integer32
_TpvrrpStatsAuthFailures_Object=MibTableColumn
tpvrrpStatsAuthFailures=_TpvrrpStatsAuthFailures_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,10),_TpvrrpStatsAuthFailures_Type())
tpvrrpStatsAuthFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsAuthFailures.setStatus(_A)
_TpvrrpStatsIpTtlErrors_Type=Integer32
_TpvrrpStatsIpTtlErrors_Object=MibTableColumn
tpvrrpStatsIpTtlErrors=_TpvrrpStatsIpTtlErrors_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,11),_TpvrrpStatsIpTtlErrors_Type())
tpvrrpStatsIpTtlErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsIpTtlErrors.setStatus(_A)
_TpvrrpStatsPriorityZeroPktsRcvd_Type=Integer32
_TpvrrpStatsPriorityZeroPktsRcvd_Object=MibTableColumn
tpvrrpStatsPriorityZeroPktsRcvd=_TpvrrpStatsPriorityZeroPktsRcvd_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,12),_TpvrrpStatsPriorityZeroPktsRcvd_Type())
tpvrrpStatsPriorityZeroPktsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsPriorityZeroPktsRcvd.setStatus(_A)
_TpvrrpStatsPriorityZeroPktsSent_Type=Integer32
_TpvrrpStatsPriorityZeroPktsSent_Object=MibTableColumn
tpvrrpStatsPriorityZeroPktsSent=_TpvrrpStatsPriorityZeroPktsSent_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,13),_TpvrrpStatsPriorityZeroPktsSent_Type())
tpvrrpStatsPriorityZeroPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsPriorityZeroPktsSent.setStatus(_A)
_TpvrrpStatsInvalidTypePktsRcvd_Type=Integer32
_TpvrrpStatsInvalidTypePktsRcvd_Object=MibTableColumn
tpvrrpStatsInvalidTypePktsRcvd=_TpvrrpStatsInvalidTypePktsRcvd_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,14),_TpvrrpStatsInvalidTypePktsRcvd_Type())
tpvrrpStatsInvalidTypePktsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsInvalidTypePktsRcvd.setStatus(_A)
_TpvrrpStatsAddressListErrors_Type=Integer32
_TpvrrpStatsAddressListErrors_Object=MibTableColumn
tpvrrpStatsAddressListErrors=_TpvrrpStatsAddressListErrors_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,15),_TpvrrpStatsAddressListErrors_Type())
tpvrrpStatsAddressListErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsAddressListErrors.setStatus(_A)
_TpvrrpStatsInvalidAuthType_Type=Integer32
_TpvrrpStatsInvalidAuthType_Object=MibTableColumn
tpvrrpStatsInvalidAuthType=_TpvrrpStatsInvalidAuthType_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,16),_TpvrrpStatsInvalidAuthType_Type())
tpvrrpStatsInvalidAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsInvalidAuthType.setStatus(_A)
_TpvrrpStatsAuthTypeMismatch_Type=Integer32
_TpvrrpStatsAuthTypeMismatch_Object=MibTableColumn
tpvrrpStatsAuthTypeMismatch=_TpvrrpStatsAuthTypeMismatch_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,17),_TpvrrpStatsAuthTypeMismatch_Type())
tpvrrpStatsAuthTypeMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsAuthTypeMismatch.setStatus(_A)
_TpvrrpStatsPacketLengthErrors_Type=Integer32
_TpvrrpStatsPacketLengthErrors_Object=MibTableColumn
tpvrrpStatsPacketLengthErrors=_TpvrrpStatsPacketLengthErrors_Object((1,3,6,1,4,1,11863,6,65,1,4,4,1,18),_TpvrrpStatsPacketLengthErrors_Type())
tpvrrpStatsPacketLengthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tpvrrpStatsPacketLengthErrors.setStatus(_A)
class _TpvrrpStatsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('clear',0),('active',1)))
_TpvrrpStatsClear_Type.__name__=_C
_TpvrrpStatsClear_Object=MibScalar
tpvrrpStatsClear=_TpvrrpStatsClear_Object((1,3,6,1,4,1,11863,6,65,1,4,5),_TpvrrpStatsClear_Type())
tpvrrpStatsClear.setMaxAccess('read-write')
if mibBuilder.loadTexts:tpvrrpStatsClear.setStatus(_A)
_TplinkVrrpNotifications_ObjectIdentity=ObjectIdentity
tplinkVrrpNotifications=_TplinkVrrpNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,65,2))
mibBuilder.exportSymbols(_D,**{'tplinkVrrpMIB':tplinkVrrpMIB,'tplinkVrrpMIBObjects':tplinkVrrpMIBObjects,'tpVrrpGlobalCtrl':tpVrrpGlobalCtrl,'tpVrrpGlobalCtrlTable':tpVrrpGlobalCtrlTable,'tpVrrpGlobalCtrlEntry':tpVrrpGlobalCtrlEntry,_H:tpVrrpVrid,_I:tpVrrpVid,'tpVrrpIntfStatus':tpVrrpIntfStatus,'tpVrrpInterfaceIP':tpVrrpInterfaceIP,'tpVrrpMacAddress':tpVrrpMacAddress,'tpVrrpDescription':tpVrrpDescription,'tpVrrpPrimaryVirtualIp':tpVrrpPrimaryVirtualIp,'tpVrrpRunPriority':tpVrrpRunPriority,'tpVrrpConfigPriority':tpVrrpConfigPriority,'tpVrrpAdvertisement':tpVrrpAdvertisement,'tpVrrpPreeptMode':tpVrrpPreeptMode,'tpVrrpTimeDelay':tpVrrpTimeDelay,'tpVrrpAuthType':tpVrrpAuthType,'tpVrrpKey':tpVrrpKey,'tpVrrpState':tpVrrpState,'tpVrrpStatus':tpVrrpStatus,'tpVrrpVirtualIpCtrl':tpVrrpVirtualIpCtrl,'tpVrrpVirtualIpCtrlTable':tpVrrpVirtualIpCtrlTable,'tpVrrpVirtualIpCtrlEntry':tpVrrpVirtualIpCtrlEntry,_J:tpVrrpVirtualIpVrid,_K:tpVrrpVirtualIpVid,'tpVrrpVirtualIpintfStatus':tpVrrpVirtualIpintfStatus,_L:tpVrrpVirtualIpAddress,'tpVrrpVirtualIpStatus':tpVrrpVirtualIpStatus,'tpVrrpTrackCtrl':tpVrrpTrackCtrl,'tpVrrpTrackCtrlTable':tpVrrpTrackCtrlTable,'tpVrrpTrackCtrlEntry':tpVrrpTrackCtrlEntry,_M:tpVrrpTrackVrid,_N:tpVrrpTrackVid,'tpVrrpTrackIntfStatus':tpVrrpTrackIntfStatus,_O:tpVrrpTrackInterface,'tpVrrpTrackIntfTrackedStatus':tpVrrpTrackIntfTrackedStatus,'tpVrrpTrackPriortiy':tpVrrpTrackPriortiy,'tpVrrpLinkState':tpVrrpLinkState,'tpVrrpTrackStatus':tpVrrpTrackStatus,'tpVrrpStatistics':tpVrrpStatistics,'tpVrrpChecksumErrors':tpVrrpChecksumErrors,'tpVrrpVersionErrors':tpVrrpVersionErrors,'tpVrrpVridErrors':tpVrrpVridErrors,'tpVrrpStatsTable':tpVrrpStatsTable,'tpVrrpStatsEntry':tpVrrpStatsEntry,_P:tpVrrpStatsVrid,_Q:tpVrrpStatsVid,'tpVrrpStatsIntfStatus':tpVrrpStatsIntfStatus,'tpVrrpChecksumErr':tpVrrpChecksumErr,'tpVrrpVersionErr':tpVrrpVersionErr,'tpVrrpStatsBecomeMaster':tpVrrpStatsBecomeMaster,'tpvrrpStatsAdvertiseRcvd':tpvrrpStatsAdvertiseRcvd,'tpvrrpStatsAdvertiseSent':tpvrrpStatsAdvertiseSent,'tpvrrpStatsAdvertiseIntervalErrors':tpvrrpStatsAdvertiseIntervalErrors,'tpvrrpStatsAuthFailures':tpvrrpStatsAuthFailures,'tpvrrpStatsIpTtlErrors':tpvrrpStatsIpTtlErrors,'tpvrrpStatsPriorityZeroPktsRcvd':tpvrrpStatsPriorityZeroPktsRcvd,'tpvrrpStatsPriorityZeroPktsSent':tpvrrpStatsPriorityZeroPktsSent,'tpvrrpStatsInvalidTypePktsRcvd':tpvrrpStatsInvalidTypePktsRcvd,'tpvrrpStatsAddressListErrors':tpvrrpStatsAddressListErrors,'tpvrrpStatsInvalidAuthType':tpvrrpStatsInvalidAuthType,'tpvrrpStatsAuthTypeMismatch':tpvrrpStatsAuthTypeMismatch,'tpvrrpStatsPacketLengthErrors':tpvrrpStatsPacketLengthErrors,'tpvrrpStatsClear':tpvrrpStatsClear,'tplinkVrrpNotifications':tplinkVrrpNotifications})