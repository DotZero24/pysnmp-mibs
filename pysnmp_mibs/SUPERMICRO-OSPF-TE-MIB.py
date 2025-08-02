_Z='futOspfTeIfBandwidthPriority'
_Y='futOspfTeIfSwDescrMaxBwPriority'
_X='futOspfTeAreaId'
_W='futOspfTeType9LsdbRouterId'
_V='futOspfTeType9LsdbLsid'
_U='futOspfTeType9LsdbIfIndex'
_T='futOspfTeType9LsdbIfIpAddress'
_S='futOspfTeLsdbRouterId'
_R='futOspfTeLsdbLsid'
_Q='futOspfTeLsdbType'
_P='futOspfTeLsdbAreaId'
_O='read-write'
_N='Unsigned32'
_M='thousand bps'
_L='futOspfTeIfDescrId'
_K='futOspfTeIfDescrAddressLessIf'
_J='futOspfTeIfDescrIpAddress'
_I='futOspfTeAddressLessIf'
_H='futOspfTeIfIpAddress'
_G='OctetString'
_F='InterfaceIndex'
_E='Integer32'
_D='not-accessible'
_C='SUPERMICRO-OSPF-TE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
futOspfTe=ModuleIdentity((1,3,6,1,4,1,10876,101,1,72))
if mibBuilder.loadTexts:futOspfTe.setRevisions(('2012-09-05 00:00',))
class AreaID(TextualConvention,IpAddress):status=_A
class RouterID(TextualConvention,IpAddress):status=_A
class InterfaceIndex(TextualConvention,Integer32):status=_A;displayHint='d'
class BandWidth(TextualConvention,Counter64):status=_A;displayHint='d'
class TeLinkPriority(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class TeLinkEncodingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,7,8,9,11)));namedValues=NamedValues(*(('packet',1),('ethernet',2),('ansiEtsiPdh',3),('sdhItuSonetAnsi',5),('digitalWrapper',7),('lambda',8),('fiber',9),('fiberChannel',11)))
_FutOspfTeGeneralGroup_ObjectIdentity=ObjectIdentity
futOspfTeGeneralGroup=_FutOspfTeGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,72,1))
class _FutOspfTeAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FutOspfTeAdminStatus_Type.__name__=_E
_FutOspfTeAdminStatus_Object=MibScalar
futOspfTeAdminStatus=_FutOspfTeAdminStatus_Object((1,3,6,1,4,1,10876,101,1,72,1,1),_FutOspfTeAdminStatus_Type())
futOspfTeAdminStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:futOspfTeAdminStatus.setStatus(_A)
class _FutOspfTeTraceLevel_Type(Integer32):defaultValue=1
_FutOspfTeTraceLevel_Type.__name__=_E
_FutOspfTeTraceLevel_Object=MibScalar
futOspfTeTraceLevel=_FutOspfTeTraceLevel_Object((1,3,6,1,4,1,10876,101,1,72,1,2),_FutOspfTeTraceLevel_Type())
futOspfTeTraceLevel.setMaxAccess(_O)
if mibBuilder.loadTexts:futOspfTeTraceLevel.setStatus(_A)
_FutOspfTeCspfRunCnt_Type=Counter32
_FutOspfTeCspfRunCnt_Object=MibScalar
futOspfTeCspfRunCnt=_FutOspfTeCspfRunCnt_Object((1,3,6,1,4,1,10876,101,1,72,1,3),_FutOspfTeCspfRunCnt_Type())
futOspfTeCspfRunCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeCspfRunCnt.setStatus(_A)
_FutOspfTeLsdbTable_Object=MibTable
futOspfTeLsdbTable=_FutOspfTeLsdbTable_Object((1,3,6,1,4,1,10876,101,1,72,2))
if mibBuilder.loadTexts:futOspfTeLsdbTable.setStatus(_A)
_FutOspfTeLsdbEntry_Object=MibTableRow
futOspfTeLsdbEntry=_FutOspfTeLsdbEntry_Object((1,3,6,1,4,1,10876,101,1,72,2,1))
futOspfTeLsdbEntry.setIndexNames((0,_C,_P),(0,_C,_Q),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:futOspfTeLsdbEntry.setStatus(_A)
_FutOspfTeLsdbAreaId_Type=AreaID
_FutOspfTeLsdbAreaId_Object=MibTableColumn
futOspfTeLsdbAreaId=_FutOspfTeLsdbAreaId_Object((1,3,6,1,4,1,10876,101,1,72,2,1,1),_FutOspfTeLsdbAreaId_Type())
futOspfTeLsdbAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeLsdbAreaId.setStatus(_A)
class _FutOspfTeLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10)));namedValues=NamedValues(*(('routerLSA',1),('networkLSA',2),('type10OpaqueLSA',10)))
_FutOspfTeLsdbType_Type.__name__=_E
_FutOspfTeLsdbType_Object=MibTableColumn
futOspfTeLsdbType=_FutOspfTeLsdbType_Object((1,3,6,1,4,1,10876,101,1,72,2,1,2),_FutOspfTeLsdbType_Type())
futOspfTeLsdbType.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeLsdbType.setStatus(_A)
_FutOspfTeLsdbLsid_Type=IpAddress
_FutOspfTeLsdbLsid_Object=MibTableColumn
futOspfTeLsdbLsid=_FutOspfTeLsdbLsid_Object((1,3,6,1,4,1,10876,101,1,72,2,1,3),_FutOspfTeLsdbLsid_Type())
futOspfTeLsdbLsid.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeLsdbLsid.setStatus(_A)
_FutOspfTeLsdbRouterId_Type=RouterID
_FutOspfTeLsdbRouterId_Object=MibTableColumn
futOspfTeLsdbRouterId=_FutOspfTeLsdbRouterId_Object((1,3,6,1,4,1,10876,101,1,72,2,1,4),_FutOspfTeLsdbRouterId_Type())
futOspfTeLsdbRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeLsdbRouterId.setStatus(_A)
_FutOspfTeLsdbChecksum_Type=Integer32
_FutOspfTeLsdbChecksum_Object=MibTableColumn
futOspfTeLsdbChecksum=_FutOspfTeLsdbChecksum_Object((1,3,6,1,4,1,10876,101,1,72,2,1,5),_FutOspfTeLsdbChecksum_Type())
futOspfTeLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeLsdbChecksum.setStatus(_A)
class _FutOspfTeLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_FutOspfTeLsdbAdvertisement_Type.__name__=_G
_FutOspfTeLsdbAdvertisement_Object=MibTableColumn
futOspfTeLsdbAdvertisement=_FutOspfTeLsdbAdvertisement_Object((1,3,6,1,4,1,10876,101,1,72,2,1,6),_FutOspfTeLsdbAdvertisement_Type())
futOspfTeLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeLsdbAdvertisement.setStatus(_A)
_FutOspfTeType9LsdbTable_Object=MibTable
futOspfTeType9LsdbTable=_FutOspfTeType9LsdbTable_Object((1,3,6,1,4,1,10876,101,1,72,3))
if mibBuilder.loadTexts:futOspfTeType9LsdbTable.setStatus(_A)
_FutOspfTeType9LsdbEntry_Object=MibTableRow
futOspfTeType9LsdbEntry=_FutOspfTeType9LsdbEntry_Object((1,3,6,1,4,1,10876,101,1,72,3,1))
futOspfTeType9LsdbEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_V),(0,_C,_W))
if mibBuilder.loadTexts:futOspfTeType9LsdbEntry.setStatus(_A)
_FutOspfTeType9LsdbIfIpAddress_Type=IpAddress
_FutOspfTeType9LsdbIfIpAddress_Object=MibTableColumn
futOspfTeType9LsdbIfIpAddress=_FutOspfTeType9LsdbIfIpAddress_Object((1,3,6,1,4,1,10876,101,1,72,3,1,1),_FutOspfTeType9LsdbIfIpAddress_Type())
futOspfTeType9LsdbIfIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeType9LsdbIfIpAddress.setStatus(_A)
class _FutOspfTeType9LsdbIfIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FutOspfTeType9LsdbIfIndex_Type.__name__=_F
_FutOspfTeType9LsdbIfIndex_Object=MibTableColumn
futOspfTeType9LsdbIfIndex=_FutOspfTeType9LsdbIfIndex_Object((1,3,6,1,4,1,10876,101,1,72,3,1,2),_FutOspfTeType9LsdbIfIndex_Type())
futOspfTeType9LsdbIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeType9LsdbIfIndex.setStatus(_A)
_FutOspfTeType9LsdbLsid_Type=IpAddress
_FutOspfTeType9LsdbLsid_Object=MibTableColumn
futOspfTeType9LsdbLsid=_FutOspfTeType9LsdbLsid_Object((1,3,6,1,4,1,10876,101,1,72,3,1,3),_FutOspfTeType9LsdbLsid_Type())
futOspfTeType9LsdbLsid.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeType9LsdbLsid.setStatus(_A)
_FutOspfTeType9LsdbRouterId_Type=RouterID
_FutOspfTeType9LsdbRouterId_Object=MibTableColumn
futOspfTeType9LsdbRouterId=_FutOspfTeType9LsdbRouterId_Object((1,3,6,1,4,1,10876,101,1,72,3,1,4),_FutOspfTeType9LsdbRouterId_Type())
futOspfTeType9LsdbRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeType9LsdbRouterId.setStatus(_A)
_FutOspfTeType9LsdbChecksum_Type=Integer32
_FutOspfTeType9LsdbChecksum_Object=MibTableColumn
futOspfTeType9LsdbChecksum=_FutOspfTeType9LsdbChecksum_Object((1,3,6,1,4,1,10876,101,1,72,3,1,5),_FutOspfTeType9LsdbChecksum_Type())
futOspfTeType9LsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeType9LsdbChecksum.setStatus(_A)
class _FutOspfTeType9LsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_FutOspfTeType9LsdbAdvertisement_Type.__name__=_G
_FutOspfTeType9LsdbAdvertisement_Object=MibTableColumn
futOspfTeType9LsdbAdvertisement=_FutOspfTeType9LsdbAdvertisement_Object((1,3,6,1,4,1,10876,101,1,72,3,1,6),_FutOspfTeType9LsdbAdvertisement_Type())
futOspfTeType9LsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeType9LsdbAdvertisement.setStatus(_A)
_FutOspfTeAreaTable_Object=MibTable
futOspfTeAreaTable=_FutOspfTeAreaTable_Object((1,3,6,1,4,1,10876,101,1,72,4))
if mibBuilder.loadTexts:futOspfTeAreaTable.setStatus(_A)
_FutOspfTeAreaEntry_Object=MibTableRow
futOspfTeAreaEntry=_FutOspfTeAreaEntry_Object((1,3,6,1,4,1,10876,101,1,72,4,1))
futOspfTeAreaEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:futOspfTeAreaEntry.setStatus(_A)
_FutOspfTeAreaId_Type=AreaID
_FutOspfTeAreaId_Object=MibTableColumn
futOspfTeAreaId=_FutOspfTeAreaId_Object((1,3,6,1,4,1,10876,101,1,72,4,1,1),_FutOspfTeAreaId_Type())
futOspfTeAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeAreaId.setStatus(_A)
_FutOspfTeAreaLsaCount_Type=Integer32
_FutOspfTeAreaLsaCount_Object=MibTableColumn
futOspfTeAreaLsaCount=_FutOspfTeAreaLsaCount_Object((1,3,6,1,4,1,10876,101,1,72,4,1,2),_FutOspfTeAreaLsaCount_Type())
futOspfTeAreaLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeAreaLsaCount.setStatus(_A)
_FutOspfTeType10AreaCksumSum_Type=Integer32
_FutOspfTeType10AreaCksumSum_Object=MibTableColumn
futOspfTeType10AreaCksumSum=_FutOspfTeType10AreaCksumSum_Object((1,3,6,1,4,1,10876,101,1,72,4,1,3),_FutOspfTeType10AreaCksumSum_Type())
futOspfTeType10AreaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeType10AreaCksumSum.setStatus(_A)
_FutOspfTeType2AreaCksumSum_Type=Integer32
_FutOspfTeType2AreaCksumSum_Object=MibTableColumn
futOspfTeType2AreaCksumSum=_FutOspfTeType2AreaCksumSum_Object((1,3,6,1,4,1,10876,101,1,72,4,1,4),_FutOspfTeType2AreaCksumSum_Type())
futOspfTeType2AreaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeType2AreaCksumSum.setStatus(_A)
_FutOspfTeIfTable_Object=MibTable
futOspfTeIfTable=_FutOspfTeIfTable_Object((1,3,6,1,4,1,10876,101,1,72,5))
if mibBuilder.loadTexts:futOspfTeIfTable.setStatus(_A)
_FutOspfTeIfEntry_Object=MibTableRow
futOspfTeIfEntry=_FutOspfTeIfEntry_Object((1,3,6,1,4,1,10876,101,1,72,5,1))
futOspfTeIfEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:futOspfTeIfEntry.setStatus(_A)
_FutOspfTeIfIpAddress_Type=IpAddress
_FutOspfTeIfIpAddress_Object=MibTableColumn
futOspfTeIfIpAddress=_FutOspfTeIfIpAddress_Object((1,3,6,1,4,1,10876,101,1,72,5,1,1),_FutOspfTeIfIpAddress_Type())
futOspfTeIfIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeIfIpAddress.setStatus(_A)
class _FutOspfTeAddressLessIf_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FutOspfTeAddressLessIf_Type.__name__=_F
_FutOspfTeAddressLessIf_Object=MibTableColumn
futOspfTeAddressLessIf=_FutOspfTeAddressLessIf_Object((1,3,6,1,4,1,10876,101,1,72,5,1,2),_FutOspfTeAddressLessIf_Type())
futOspfTeAddressLessIf.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeAddressLessIf.setStatus(_A)
_FutOspfTeIfAreaId_Type=AreaID
_FutOspfTeIfAreaId_Object=MibTableColumn
futOspfTeIfAreaId=_FutOspfTeIfAreaId_Object((1,3,6,1,4,1,10876,101,1,72,5,1,3),_FutOspfTeIfAreaId_Type())
futOspfTeIfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfAreaId.setStatus(_A)
class _FutOspfTeIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pointToPoint',1),('multiaccess',2)))
_FutOspfTeIfType_Type.__name__=_E
_FutOspfTeIfType_Object=MibTableColumn
futOspfTeIfType=_FutOspfTeIfType_Object((1,3,6,1,4,1,10876,101,1,72,5,1,4),_FutOspfTeIfType_Type())
futOspfTeIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfType.setStatus(_A)
_FutOspfTeIfMetric_Type=Integer32
_FutOspfTeIfMetric_Object=MibTableColumn
futOspfTeIfMetric=_FutOspfTeIfMetric_Object((1,3,6,1,4,1,10876,101,1,72,5,1,5),_FutOspfTeIfMetric_Type())
futOspfTeIfMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfMetric.setStatus(_A)
_FutOspfTeIfMaxBw_Type=BandWidth
_FutOspfTeIfMaxBw_Object=MibTableColumn
futOspfTeIfMaxBw=_FutOspfTeIfMaxBw_Object((1,3,6,1,4,1,10876,101,1,72,5,1,6),_FutOspfTeIfMaxBw_Type())
futOspfTeIfMaxBw.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfMaxBw.setStatus(_A)
_FutOspfTeIfMaxReservBw_Type=BandWidth
_FutOspfTeIfMaxReservBw_Object=MibTableColumn
futOspfTeIfMaxReservBw=_FutOspfTeIfMaxReservBw_Object((1,3,6,1,4,1,10876,101,1,72,5,1,7),_FutOspfTeIfMaxReservBw_Type())
futOspfTeIfMaxReservBw.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfMaxReservBw.setStatus(_A)
_FutOspfTeIfRsrcClassColor_Type=Integer32
_FutOspfTeIfRsrcClassColor_Object=MibTableColumn
futOspfTeIfRsrcClassColor=_FutOspfTeIfRsrcClassColor_Object((1,3,6,1,4,1,10876,101,1,72,5,1,8),_FutOspfTeIfRsrcClassColor_Type())
futOspfTeIfRsrcClassColor.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfRsrcClassColor.setStatus(_A)
class _FutOspfTeIfOperStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('notInService',2),('active',3)))
_FutOspfTeIfOperStat_Type.__name__=_E
_FutOspfTeIfOperStat_Object=MibTableColumn
futOspfTeIfOperStat=_FutOspfTeIfOperStat_Object((1,3,6,1,4,1,10876,101,1,72,5,1,9),_FutOspfTeIfOperStat_Type())
futOspfTeIfOperStat.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfOperStat.setStatus(_A)
_FutOspfTeIfLinkId_Type=IpAddress
_FutOspfTeIfLinkId_Object=MibTableColumn
futOspfTeIfLinkId=_FutOspfTeIfLinkId_Object((1,3,6,1,4,1,10876,101,1,72,5,1,10),_FutOspfTeIfLinkId_Type())
futOspfTeIfLinkId.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfLinkId.setStatus(_A)
_FutOspfTeIfRemoteIpAddr_Type=IpAddress
_FutOspfTeIfRemoteIpAddr_Object=MibTableColumn
futOspfTeIfRemoteIpAddr=_FutOspfTeIfRemoteIpAddr_Object((1,3,6,1,4,1,10876,101,1,72,5,1,11),_FutOspfTeIfRemoteIpAddr_Type())
futOspfTeIfRemoteIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfRemoteIpAddr.setStatus(_A)
class _FutOspfTeIfProtectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('extraTraffic',1),('unprotected',2),('shared',3),('dedicated1For1',4),('dedicated1Plus1',5),('enhanced',6)))
_FutOspfTeIfProtectionType_Type.__name__=_E
_FutOspfTeIfProtectionType_Object=MibTableColumn
futOspfTeIfProtectionType=_FutOspfTeIfProtectionType_Object((1,3,6,1,4,1,10876,101,1,72,5,1,12),_FutOspfTeIfProtectionType_Type())
futOspfTeIfProtectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfProtectionType.setStatus(_A)
_FutOspfTeIfSrlg_Type=OctetString
_FutOspfTeIfSrlg_Object=MibTableColumn
futOspfTeIfSrlg=_FutOspfTeIfSrlg_Object((1,3,6,1,4,1,10876,101,1,72,5,1,13),_FutOspfTeIfSrlg_Type())
futOspfTeIfSrlg.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfSrlg.setStatus(_A)
_FutOspfTeIfDescriptorTable_Object=MibTable
futOspfTeIfDescriptorTable=_FutOspfTeIfDescriptorTable_Object((1,3,6,1,4,1,10876,101,1,72,6))
if mibBuilder.loadTexts:futOspfTeIfDescriptorTable.setStatus(_A)
_FutOspfTeIfDescriptorEntry_Object=MibTableRow
futOspfTeIfDescriptorEntry=_FutOspfTeIfDescriptorEntry_Object((1,3,6,1,4,1,10876,101,1,72,6,1))
futOspfTeIfDescriptorEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:futOspfTeIfDescriptorEntry.setStatus(_A)
_FutOspfTeIfDescrIpAddress_Type=IpAddress
_FutOspfTeIfDescrIpAddress_Object=MibTableColumn
futOspfTeIfDescrIpAddress=_FutOspfTeIfDescrIpAddress_Object((1,3,6,1,4,1,10876,101,1,72,6,1,1),_FutOspfTeIfDescrIpAddress_Type())
futOspfTeIfDescrIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeIfDescrIpAddress.setStatus(_A)
class _FutOspfTeIfDescrAddressLessIf_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FutOspfTeIfDescrAddressLessIf_Type.__name__=_F
_FutOspfTeIfDescrAddressLessIf_Object=MibTableColumn
futOspfTeIfDescrAddressLessIf=_FutOspfTeIfDescrAddressLessIf_Object((1,3,6,1,4,1,10876,101,1,72,6,1,2),_FutOspfTeIfDescrAddressLessIf_Type())
futOspfTeIfDescrAddressLessIf.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeIfDescrAddressLessIf.setStatus(_A)
class _FutOspfTeIfDescrId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FutOspfTeIfDescrId_Type.__name__=_N
_FutOspfTeIfDescrId_Object=MibTableColumn
futOspfTeIfDescrId=_FutOspfTeIfDescrId_Object((1,3,6,1,4,1,10876,101,1,72,6,1,3),_FutOspfTeIfDescrId_Type())
futOspfTeIfDescrId.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeIfDescrId.setStatus(_A)
class _FutOspfTeIfDescrSwithingCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,51,100,150,200)));namedValues=NamedValues(*(('psc1',1),('psc2',2),('psc3',3),('psc4',4),('l2sc',51),('tdm',100),('lsc',150),('fsc',200)))
_FutOspfTeIfDescrSwithingCap_Type.__name__=_E
_FutOspfTeIfDescrSwithingCap_Object=MibTableColumn
futOspfTeIfDescrSwithingCap=_FutOspfTeIfDescrSwithingCap_Object((1,3,6,1,4,1,10876,101,1,72,6,1,4),_FutOspfTeIfDescrSwithingCap_Type())
futOspfTeIfDescrSwithingCap.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfDescrSwithingCap.setStatus(_A)
_FutOspfTeIfDescrEncodingType_Type=TeLinkEncodingType
_FutOspfTeIfDescrEncodingType_Object=MibTableColumn
futOspfTeIfDescrEncodingType=_FutOspfTeIfDescrEncodingType_Object((1,3,6,1,4,1,10876,101,1,72,6,1,5),_FutOspfTeIfDescrEncodingType_Type())
futOspfTeIfDescrEncodingType.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfDescrEncodingType.setStatus(_A)
_FutOspfTeIfDescrMinLSPBandwidth_Type=BandWidth
_FutOspfTeIfDescrMinLSPBandwidth_Object=MibTableColumn
futOspfTeIfDescrMinLSPBandwidth=_FutOspfTeIfDescrMinLSPBandwidth_Object((1,3,6,1,4,1,10876,101,1,72,6,1,6),_FutOspfTeIfDescrMinLSPBandwidth_Type())
futOspfTeIfDescrMinLSPBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfDescrMinLSPBandwidth.setStatus(_A)
if mibBuilder.loadTexts:futOspfTeIfDescrMinLSPBandwidth.setUnits(_M)
_FutOspfTeIfDescrMTU_Type=Integer32
_FutOspfTeIfDescrMTU_Object=MibTableColumn
futOspfTeIfDescrMTU=_FutOspfTeIfDescrMTU_Object((1,3,6,1,4,1,10876,101,1,72,6,1,7),_FutOspfTeIfDescrMTU_Type())
futOspfTeIfDescrMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfDescrMTU.setStatus(_A)
_FutOspfTeIfDescrIndication_Type=Integer32
_FutOspfTeIfDescrIndication_Object=MibTableColumn
futOspfTeIfDescrIndication=_FutOspfTeIfDescrIndication_Object((1,3,6,1,4,1,10876,101,1,72,6,1,8),_FutOspfTeIfDescrIndication_Type())
futOspfTeIfDescrIndication.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfDescrIndication.setStatus(_A)
_FutOspfTeIfSwDescrMaxBwTable_Object=MibTable
futOspfTeIfSwDescrMaxBwTable=_FutOspfTeIfSwDescrMaxBwTable_Object((1,3,6,1,4,1,10876,101,1,72,7))
if mibBuilder.loadTexts:futOspfTeIfSwDescrMaxBwTable.setStatus(_A)
_FutOspfTeIfSwDescrMaxBwEntry_Object=MibTableRow
futOspfTeIfSwDescrMaxBwEntry=_FutOspfTeIfSwDescrMaxBwEntry_Object((1,3,6,1,4,1,10876,101,1,72,7,1))
futOspfTeIfSwDescrMaxBwEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_Y))
if mibBuilder.loadTexts:futOspfTeIfSwDescrMaxBwEntry.setStatus(_A)
_FutOspfTeIfSwDescrMaxBwPriority_Type=TeLinkPriority
_FutOspfTeIfSwDescrMaxBwPriority_Object=MibTableColumn
futOspfTeIfSwDescrMaxBwPriority=_FutOspfTeIfSwDescrMaxBwPriority_Object((1,3,6,1,4,1,10876,101,1,72,7,1,1),_FutOspfTeIfSwDescrMaxBwPriority_Type())
futOspfTeIfSwDescrMaxBwPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeIfSwDescrMaxBwPriority.setStatus(_A)
_FutOspfTeIfSwDescrMaxLSPBandwidth_Type=BandWidth
_FutOspfTeIfSwDescrMaxLSPBandwidth_Object=MibTableColumn
futOspfTeIfSwDescrMaxLSPBandwidth=_FutOspfTeIfSwDescrMaxLSPBandwidth_Object((1,3,6,1,4,1,10876,101,1,72,7,1,2),_FutOspfTeIfSwDescrMaxLSPBandwidth_Type())
futOspfTeIfSwDescrMaxLSPBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfSwDescrMaxLSPBandwidth.setStatus(_A)
if mibBuilder.loadTexts:futOspfTeIfSwDescrMaxLSPBandwidth.setUnits(_M)
_FutOspfTeIfBandwidthTable_Object=MibTable
futOspfTeIfBandwidthTable=_FutOspfTeIfBandwidthTable_Object((1,3,6,1,4,1,10876,101,1,72,8))
if mibBuilder.loadTexts:futOspfTeIfBandwidthTable.setStatus(_A)
_FutOspfTeIfBandwidthEntry_Object=MibTableRow
futOspfTeIfBandwidthEntry=_FutOspfTeIfBandwidthEntry_Object((1,3,6,1,4,1,10876,101,1,72,8,1))
futOspfTeIfBandwidthEntry.setIndexNames((0,_C,_H),(0,_C,_I),(0,_C,_Z))
if mibBuilder.loadTexts:futOspfTeIfBandwidthEntry.setStatus(_A)
_FutOspfTeIfBandwidthPriority_Type=TeLinkPriority
_FutOspfTeIfBandwidthPriority_Object=MibTableColumn
futOspfTeIfBandwidthPriority=_FutOspfTeIfBandwidthPriority_Object((1,3,6,1,4,1,10876,101,1,72,8,1,1),_FutOspfTeIfBandwidthPriority_Type())
futOspfTeIfBandwidthPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfTeIfBandwidthPriority.setStatus(_A)
_FutOspfTeIfUnreservedBandwidth_Type=BandWidth
_FutOspfTeIfUnreservedBandwidth_Object=MibTableColumn
futOspfTeIfUnreservedBandwidth=_FutOspfTeIfUnreservedBandwidth_Object((1,3,6,1,4,1,10876,101,1,72,8,1,2),_FutOspfTeIfUnreservedBandwidth_Type())
futOspfTeIfUnreservedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:futOspfTeIfUnreservedBandwidth.setStatus(_A)
if mibBuilder.loadTexts:futOspfTeIfUnreservedBandwidth.setUnits(_M)
mibBuilder.exportSymbols(_C,**{'AreaID':AreaID,'RouterID':RouterID,_F:InterfaceIndex,'BandWidth':BandWidth,'TeLinkPriority':TeLinkPriority,'TeLinkEncodingType':TeLinkEncodingType,'futOspfTe':futOspfTe,'futOspfTeGeneralGroup':futOspfTeGeneralGroup,'futOspfTeAdminStatus':futOspfTeAdminStatus,'futOspfTeTraceLevel':futOspfTeTraceLevel,'futOspfTeCspfRunCnt':futOspfTeCspfRunCnt,'futOspfTeLsdbTable':futOspfTeLsdbTable,'futOspfTeLsdbEntry':futOspfTeLsdbEntry,_P:futOspfTeLsdbAreaId,_Q:futOspfTeLsdbType,_R:futOspfTeLsdbLsid,_S:futOspfTeLsdbRouterId,'futOspfTeLsdbChecksum':futOspfTeLsdbChecksum,'futOspfTeLsdbAdvertisement':futOspfTeLsdbAdvertisement,'futOspfTeType9LsdbTable':futOspfTeType9LsdbTable,'futOspfTeType9LsdbEntry':futOspfTeType9LsdbEntry,_T:futOspfTeType9LsdbIfIpAddress,_U:futOspfTeType9LsdbIfIndex,_V:futOspfTeType9LsdbLsid,_W:futOspfTeType9LsdbRouterId,'futOspfTeType9LsdbChecksum':futOspfTeType9LsdbChecksum,'futOspfTeType9LsdbAdvertisement':futOspfTeType9LsdbAdvertisement,'futOspfTeAreaTable':futOspfTeAreaTable,'futOspfTeAreaEntry':futOspfTeAreaEntry,_X:futOspfTeAreaId,'futOspfTeAreaLsaCount':futOspfTeAreaLsaCount,'futOspfTeType10AreaCksumSum':futOspfTeType10AreaCksumSum,'futOspfTeType2AreaCksumSum':futOspfTeType2AreaCksumSum,'futOspfTeIfTable':futOspfTeIfTable,'futOspfTeIfEntry':futOspfTeIfEntry,_H:futOspfTeIfIpAddress,_I:futOspfTeAddressLessIf,'futOspfTeIfAreaId':futOspfTeIfAreaId,'futOspfTeIfType':futOspfTeIfType,'futOspfTeIfMetric':futOspfTeIfMetric,'futOspfTeIfMaxBw':futOspfTeIfMaxBw,'futOspfTeIfMaxReservBw':futOspfTeIfMaxReservBw,'futOspfTeIfRsrcClassColor':futOspfTeIfRsrcClassColor,'futOspfTeIfOperStat':futOspfTeIfOperStat,'futOspfTeIfLinkId':futOspfTeIfLinkId,'futOspfTeIfRemoteIpAddr':futOspfTeIfRemoteIpAddr,'futOspfTeIfProtectionType':futOspfTeIfProtectionType,'futOspfTeIfSrlg':futOspfTeIfSrlg,'futOspfTeIfDescriptorTable':futOspfTeIfDescriptorTable,'futOspfTeIfDescriptorEntry':futOspfTeIfDescriptorEntry,_J:futOspfTeIfDescrIpAddress,_K:futOspfTeIfDescrAddressLessIf,_L:futOspfTeIfDescrId,'futOspfTeIfDescrSwithingCap':futOspfTeIfDescrSwithingCap,'futOspfTeIfDescrEncodingType':futOspfTeIfDescrEncodingType,'futOspfTeIfDescrMinLSPBandwidth':futOspfTeIfDescrMinLSPBandwidth,'futOspfTeIfDescrMTU':futOspfTeIfDescrMTU,'futOspfTeIfDescrIndication':futOspfTeIfDescrIndication,'futOspfTeIfSwDescrMaxBwTable':futOspfTeIfSwDescrMaxBwTable,'futOspfTeIfSwDescrMaxBwEntry':futOspfTeIfSwDescrMaxBwEntry,_Y:futOspfTeIfSwDescrMaxBwPriority,'futOspfTeIfSwDescrMaxLSPBandwidth':futOspfTeIfSwDescrMaxLSPBandwidth,'futOspfTeIfBandwidthTable':futOspfTeIfBandwidthTable,'futOspfTeIfBandwidthEntry':futOspfTeIfBandwidthEntry,_Z:futOspfTeIfBandwidthPriority,'futOspfTeIfUnreservedBandwidth':futOspfTeIfUnreservedBandwidth})