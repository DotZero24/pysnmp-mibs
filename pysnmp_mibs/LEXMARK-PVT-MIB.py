_d='faxIndex'
_c='prtgenStatPrinterIndex'
_b='prtgenPrinterIndex'
_a='lextrapDestIndex'
_Z='printer'
_Y='lexhdwrPortTableIndex'
_X='lexhttpLinkTableIndex'
_W='noReset'
_V='lextcpNPAPserverIndex'
_U='individual'
_T='multiplexed'
_S='lexipxTrapIndex'
_R='lexipxConnSrvrIndex'
_Q='lexipxPrefSrvrIndex'
_P='lexipxPortInfoIndex'
_O='opsysCurrentJobEntryIndex'
_N='NotificationType'
_M='on'
_L='enabled'
_K='disabled'
_J='off'
_I='OctetString'
_H='prtgenStatusIRC'
_G='unknown'
_F='LEXMARK-PVT-MIB'
_E='DisplayString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_N,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Lexmark_ObjectIdentity=ObjectIdentity
lexmark=_Lexmark_ObjectIdentity((1,3,6,1,4,1,641))
_Adapter_ObjectIdentity=ObjectIdentity
adapter=_Adapter_ObjectIdentity((1,3,6,1,4,1,641,1))
_Opsys_ObjectIdentity=ObjectIdentity
opsys=_Opsys_ObjectIdentity((1,3,6,1,4,1,641,1,1))
class _OpsysCodeRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OpsysCodeRev_Type.__name__=_E
_OpsysCodeRev_Object=MibScalar
opsysCodeRev=_OpsysCodeRev_Object((1,3,6,1,4,1,641,1,1,1),_OpsysCodeRev_Type())
opsysCodeRev.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysCodeRev.setStatus(_A)
class _OpsysJobTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_OpsysJobTimeout_Type.__name__=_C
_OpsysJobTimeout_Object=MibScalar
opsysJobTimeout=_OpsysJobTimeout_Object((1,3,6,1,4,1,641,1,1,2),_OpsysJobTimeout_Type())
opsysJobTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:opsysJobTimeout.setStatus(_A)
class _OpsysCurrentJob_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OpsysCurrentJob_Type.__name__=_E
_OpsysCurrentJob_Object=MibScalar
opsysCurrentJob=_OpsysCurrentJob_Object((1,3,6,1,4,1,641,1,1,3),_OpsysCurrentJob_Type())
opsysCurrentJob.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysCurrentJob.setStatus(_A)
_OpsysRAMSize_Type=Integer32
_OpsysRAMSize_Object=MibScalar
opsysRAMSize=_OpsysRAMSize_Object((1,3,6,1,4,1,641,1,1,4),_OpsysRAMSize_Type())
opsysRAMSize.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysRAMSize.setStatus(_A)
_OpsysNVRAMSize_Type=Integer32
_OpsysNVRAMSize_Object=MibScalar
opsysNVRAMSize=_OpsysNVRAMSize_Object((1,3,6,1,4,1,641,1,1,5),_OpsysNVRAMSize_Type())
opsysNVRAMSize.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysNVRAMSize.setStatus(_A)
_OpsysROMSize_Type=Integer32
_OpsysROMSize_Object=MibScalar
opsysROMSize=_OpsysROMSize_Object((1,3,6,1,4,1,641,1,1,6),_OpsysROMSize_Type())
opsysROMSize.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysROMSize.setStatus(_A)
class _OpsysROMType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OpsysROMType_Type.__name__=_E
_OpsysROMType_Object=MibScalar
opsysROMType=_OpsysROMType_Object((1,3,6,1,4,1,641,1,1,7),_OpsysROMType_Type())
opsysROMType.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysROMType.setStatus(_A)
class _OpsysProtocols_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OpsysProtocols_Type.__name__=_C
_OpsysProtocols_Object=MibScalar
opsysProtocols=_OpsysProtocols_Object((1,3,6,1,4,1,641,1,1,8),_OpsysProtocols_Type())
opsysProtocols.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysProtocols.setStatus(_A)
_OpsysTimeToReset_Type=Integer32
_OpsysTimeToReset_Object=MibScalar
opsysTimeToReset=_OpsysTimeToReset_Object((1,3,6,1,4,1,641,1,1,9),_OpsysTimeToReset_Type())
opsysTimeToReset.setMaxAccess(_D)
if mibBuilder.loadTexts:opsysTimeToReset.setStatus(_A)
class _OpsysCardPartNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OpsysCardPartNo_Type.__name__=_E
_OpsysCardPartNo_Object=MibScalar
opsysCardPartNo=_OpsysCardPartNo_Object((1,3,6,1,4,1,641,1,1,10),_OpsysCardPartNo_Type())
opsysCardPartNo.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysCardPartNo.setStatus(_A)
class _OpsysCardEC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OpsysCardEC_Type.__name__=_E
_OpsysCardEC_Object=MibScalar
opsysCardEC=_OpsysCardEC_Object((1,3,6,1,4,1,641,1,1,11),_OpsysCardEC_Type())
opsysCardEC.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysCardEC.setStatus(_A)
_OpsysCurrentJobTable_Object=MibTable
opsysCurrentJobTable=_OpsysCurrentJobTable_Object((1,3,6,1,4,1,641,1,1,12))
if mibBuilder.loadTexts:opsysCurrentJobTable.setStatus(_A)
_OpsysCurrentJobEntry_Object=MibTableRow
opsysCurrentJobEntry=_OpsysCurrentJobEntry_Object((1,3,6,1,4,1,641,1,1,12,1))
opsysCurrentJobEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:opsysCurrentJobEntry.setStatus(_A)
class _OpsysCurrentJobEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OpsysCurrentJobEntryIndex_Type.__name__=_C
_OpsysCurrentJobEntryIndex_Object=MibTableColumn
opsysCurrentJobEntryIndex=_OpsysCurrentJobEntryIndex_Object((1,3,6,1,4,1,641,1,1,12,1,1),_OpsysCurrentJobEntryIndex_Type())
opsysCurrentJobEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysCurrentJobEntryIndex.setStatus(_A)
class _OpsysCurrentJobString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OpsysCurrentJobString_Type.__name__=_E
_OpsysCurrentJobString_Object=MibTableColumn
opsysCurrentJobString=_OpsysCurrentJobString_Object((1,3,6,1,4,1,641,1,1,12,1,2),_OpsysCurrentJobString_Type())
opsysCurrentJobString.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysCurrentJobString.setStatus(_A)
class _OpsysDeviceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_OpsysDeviceType_Type.__name__=_I
_OpsysDeviceType_Object=MibScalar
opsysDeviceType=_OpsysDeviceType_Object((1,3,6,1,4,1,641,1,1,13),_OpsysDeviceType_Type())
opsysDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysDeviceType.setStatus(_A)
class _OpsysAdapterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_OpsysAdapterName_Type.__name__=_I
_OpsysAdapterName_Object=MibScalar
opsysAdapterName=_OpsysAdapterName_Object((1,3,6,1,4,1,641,1,1,14),_OpsysAdapterName_Type())
opsysAdapterName.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysAdapterName.setStatus(_A)
class _OpsysAdapterCapabilities_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_OpsysAdapterCapabilities_Type.__name__=_I
_OpsysAdapterCapabilities_Object=MibScalar
opsysAdapterCapabilities=_OpsysAdapterCapabilities_Object((1,3,6,1,4,1,641,1,1,15),_OpsysAdapterCapabilities_Type())
opsysAdapterCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:opsysAdapterCapabilities.setStatus(_A)
_Lexlink_ObjectIdentity=ObjectIdentity
lexlink=_Lexlink_ObjectIdentity((1,3,6,1,4,1,641,1,2))
class _LexlinkActivated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_M,2)))
_LexlinkActivated_Type.__name__=_C
_LexlinkActivated_Object=MibScalar
lexlinkActivated=_LexlinkActivated_Object((1,3,6,1,4,1,641,1,2,1),_LexlinkActivated_Type())
lexlinkActivated.setMaxAccess(_D)
if mibBuilder.loadTexts:lexlinkActivated.setStatus(_A)
class _LexlinkNickname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_LexlinkNickname_Type.__name__=_E
_LexlinkNickname_Object=MibScalar
lexlinkNickname=_LexlinkNickname_Object((1,3,6,1,4,1,641,1,2,2),_LexlinkNickname_Type())
lexlinkNickname.setMaxAccess(_D)
if mibBuilder.loadTexts:lexlinkNickname.setStatus(_A)
_Lexipx_ObjectIdentity=ObjectIdentity
lexipx=_Lexipx_ObjectIdentity((1,3,6,1,4,1,641,1,3))
class _LexipxActivated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_M,2)))
_LexipxActivated_Type.__name__=_C
_LexipxActivated_Object=MibScalar
lexipxActivated=_LexipxActivated_Object((1,3,6,1,4,1,641,1,3,1),_LexipxActivated_Type())
lexipxActivated.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxActivated.setStatus(_A)
class _LexipxLoginName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,43))
_LexipxLoginName_Type.__name__=_E
_LexipxLoginName_Object=MibScalar
lexipxLoginName=_LexipxLoginName_Object((1,3,6,1,4,1,641,1,3,2),_LexipxLoginName_Type())
lexipxLoginName.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxLoginName.setStatus(_A)
class _LexipxNetNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_LexipxNetNumber_Type.__name__=_E
_LexipxNetNumber_Object=MibScalar
lexipxNetNumber=_LexipxNetNumber_Object((1,3,6,1,4,1,641,1,3,3),_LexipxNetNumber_Type())
lexipxNetNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxNetNumber.setStatus(_A)
class _LexipxSAPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_M,2)))
_LexipxSAPMode_Type.__name__=_C
_LexipxSAPMode_Object=MibScalar
lexipxSAPMode=_LexipxSAPMode_Object((1,3,6,1,4,1,641,1,3,4),_LexipxSAPMode_Type())
lexipxSAPMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxSAPMode.setStatus(_A)
class _LexipxServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pserver',1),('rprinter',2)))
_LexipxServerMode_Type.__name__=_C
_LexipxServerMode_Object=MibScalar
lexipxServerMode=_LexipxServerMode_Object((1,3,6,1,4,1,641,1,3,5),_LexipxServerMode_Type())
lexipxServerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxServerMode.setStatus(_A)
_LexipxNumPorts_Type=Integer32
_LexipxNumPorts_Object=MibScalar
lexipxNumPorts=_LexipxNumPorts_Object((1,3,6,1,4,1,641,1,3,6),_LexipxNumPorts_Type())
lexipxNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxNumPorts.setStatus(_A)
_LexipxPortInfoTable_Object=MibTable
lexipxPortInfoTable=_LexipxPortInfoTable_Object((1,3,6,1,4,1,641,1,3,7))
if mibBuilder.loadTexts:lexipxPortInfoTable.setStatus(_A)
_LexipxPortInfoEntry_Object=MibTableRow
lexipxPortInfoEntry=_LexipxPortInfoEntry_Object((1,3,6,1,4,1,641,1,3,7,1))
lexipxPortInfoEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:lexipxPortInfoEntry.setStatus(_A)
class _LexipxPortInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LexipxPortInfoIndex_Type.__name__=_C
_LexipxPortInfoIndex_Object=MibTableColumn
lexipxPortInfoIndex=_LexipxPortInfoIndex_Object((1,3,6,1,4,1,641,1,3,7,1,1),_LexipxPortInfoIndex_Type())
lexipxPortInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxPortInfoIndex.setStatus(_A)
class _LexipxPortInfoPollIntvl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_LexipxPortInfoPollIntvl_Type.__name__=_C
_LexipxPortInfoPollIntvl_Object=MibTableColumn
lexipxPortInfoPollIntvl=_LexipxPortInfoPollIntvl_Object((1,3,6,1,4,1,641,1,3,7,1,2),_LexipxPortInfoPollIntvl_Type())
lexipxPortInfoPollIntvl.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxPortInfoPollIntvl.setStatus(_A)
class _LexipxPortInfoEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LexipxPortInfoEnable_Type.__name__=_C
_LexipxPortInfoEnable_Object=MibTableColumn
lexipxPortInfoEnable=_LexipxPortInfoEnable_Object((1,3,6,1,4,1,641,1,3,7,1,3),_LexipxPortInfoEnable_Type())
lexipxPortInfoEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxPortInfoEnable.setStatus(_A)
class _LexipxPortInfoBannerPage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('postscript',2),('ascii',3)))
_LexipxPortInfoBannerPage_Type.__name__=_C
_LexipxPortInfoBannerPage_Object=MibTableColumn
lexipxPortInfoBannerPage=_LexipxPortInfoBannerPage_Object((1,3,6,1,4,1,641,1,3,7,1,4),_LexipxPortInfoBannerPage_Type())
lexipxPortInfoBannerPage.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxPortInfoBannerPage.setStatus(_A)
_LexipxNumPrefServers_Type=Integer32
_LexipxNumPrefServers_Object=MibScalar
lexipxNumPrefServers=_LexipxNumPrefServers_Object((1,3,6,1,4,1,641,1,3,8),_LexipxNumPrefServers_Type())
lexipxNumPrefServers.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxNumPrefServers.setStatus(_A)
_LexipxPrefSrvrTable_Object=MibTable
lexipxPrefSrvrTable=_LexipxPrefSrvrTable_Object((1,3,6,1,4,1,641,1,3,9))
if mibBuilder.loadTexts:lexipxPrefSrvrTable.setStatus(_A)
_LexipxPrefSrvrEntry_Object=MibTableRow
lexipxPrefSrvrEntry=_LexipxPrefSrvrEntry_Object((1,3,6,1,4,1,641,1,3,9,1))
lexipxPrefSrvrEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:lexipxPrefSrvrEntry.setStatus(_A)
class _LexipxPrefSrvrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LexipxPrefSrvrIndex_Type.__name__=_C
_LexipxPrefSrvrIndex_Object=MibTableColumn
lexipxPrefSrvrIndex=_LexipxPrefSrvrIndex_Object((1,3,6,1,4,1,641,1,3,9,1,1),_LexipxPrefSrvrIndex_Type())
lexipxPrefSrvrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxPrefSrvrIndex.setStatus(_A)
class _LexipxPrefSrvrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_LexipxPrefSrvrName_Type.__name__=_E
_LexipxPrefSrvrName_Object=MibTableColumn
lexipxPrefSrvrName=_LexipxPrefSrvrName_Object((1,3,6,1,4,1,641,1,3,9,1,2),_LexipxPrefSrvrName_Type())
lexipxPrefSrvrName.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxPrefSrvrName.setStatus(_A)
_LexipxConnSrvrTable_Object=MibTable
lexipxConnSrvrTable=_LexipxConnSrvrTable_Object((1,3,6,1,4,1,641,1,3,10))
if mibBuilder.loadTexts:lexipxConnSrvrTable.setStatus(_A)
_LexipxConnSrvrEntry_Object=MibTableRow
lexipxConnSrvrEntry=_LexipxConnSrvrEntry_Object((1,3,6,1,4,1,641,1,3,10,1))
lexipxConnSrvrEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:lexipxConnSrvrEntry.setStatus(_A)
class _LexipxConnSrvrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LexipxConnSrvrIndex_Type.__name__=_C
_LexipxConnSrvrIndex_Object=MibTableColumn
lexipxConnSrvrIndex=_LexipxConnSrvrIndex_Object((1,3,6,1,4,1,641,1,3,10,1,1),_LexipxConnSrvrIndex_Type())
lexipxConnSrvrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxConnSrvrIndex.setStatus(_A)
class _LexipxConnSrvrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LexipxConnSrvrName_Type.__name__=_E
_LexipxConnSrvrName_Object=MibTableColumn
lexipxConnSrvrName=_LexipxConnSrvrName_Object((1,3,6,1,4,1,641,1,3,10,1,2),_LexipxConnSrvrName_Type())
lexipxConnSrvrName.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxConnSrvrName.setStatus(_A)
class _LexipxConnSrvrNet_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_LexipxConnSrvrNet_Type.__name__=_E
_LexipxConnSrvrNet_Object=MibTableColumn
lexipxConnSrvrNet=_LexipxConnSrvrNet_Object((1,3,6,1,4,1,641,1,3,10,1,3),_LexipxConnSrvrNet_Type())
lexipxConnSrvrNet.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxConnSrvrNet.setStatus(_A)
class _LexipxConnSrvrNode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_LexipxConnSrvrNode_Type.__name__=_E
_LexipxConnSrvrNode_Object=MibTableColumn
lexipxConnSrvrNode=_LexipxConnSrvrNode_Object((1,3,6,1,4,1,641,1,3,10,1,4),_LexipxConnSrvrNode_Type())
lexipxConnSrvrNode.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxConnSrvrNode.setStatus(_A)
class _LexipxConnSrvrConnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LexipxConnSrvrConnNum_Type.__name__=_C
_LexipxConnSrvrConnNum_Object=MibTableColumn
lexipxConnSrvrConnNum=_LexipxConnSrvrConnNum_Object((1,3,6,1,4,1,641,1,3,10,1,5),_LexipxConnSrvrConnNum_Type())
lexipxConnSrvrConnNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxConnSrvrConnNum.setStatus(_A)
class _LexipxConnSrvrConnId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LexipxConnSrvrConnId_Type.__name__=_C
_LexipxConnSrvrConnId_Object=MibTableColumn
lexipxConnSrvrConnId=_LexipxConnSrvrConnId_Object((1,3,6,1,4,1,641,1,3,10,1,6),_LexipxConnSrvrConnId_Type())
lexipxConnSrvrConnId.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxConnSrvrConnId.setStatus(_A)
class _LexipxConnSrvrPSConnID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LexipxConnSrvrPSConnID_Type.__name__=_C
_LexipxConnSrvrPSConnID_Object=MibTableColumn
lexipxConnSrvrPSConnID=_LexipxConnSrvrPSConnID_Object((1,3,6,1,4,1,641,1,3,10,1,7),_LexipxConnSrvrPSConnID_Type())
lexipxConnSrvrPSConnID.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxConnSrvrPSConnID.setStatus(_A)
class _LexipxFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LexipxFrameType_Type.__name__=_C
_LexipxFrameType_Object=MibScalar
lexipxFrameType=_LexipxFrameType_Object((1,3,6,1,4,1,641,1,3,11),_LexipxFrameType_Type())
lexipxFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxFrameType.setStatus(_A)
_LexipxTrapTable_Object=MibTable
lexipxTrapTable=_LexipxTrapTable_Object((1,3,6,1,4,1,641,1,3,12))
if mibBuilder.loadTexts:lexipxTrapTable.setStatus(_A)
_LexipxTrapEntry_Object=MibTableRow
lexipxTrapEntry=_LexipxTrapEntry_Object((1,3,6,1,4,1,641,1,3,12,1))
lexipxTrapEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:lexipxTrapEntry.setStatus(_A)
class _LexipxTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LexipxTrapIndex_Type.__name__=_C
_LexipxTrapIndex_Object=MibTableColumn
lexipxTrapIndex=_LexipxTrapIndex_Object((1,3,6,1,4,1,641,1,3,12,1,1),_LexipxTrapIndex_Type())
lexipxTrapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lexipxTrapIndex.setStatus(_A)
class _LexipxTrapMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LexipxTrapMask_Type.__name__=_C
_LexipxTrapMask_Object=MibTableColumn
lexipxTrapMask=_LexipxTrapMask_Object((1,3,6,1,4,1,641,1,3,12,1,2),_LexipxTrapMask_Type())
lexipxTrapMask.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxTrapMask.setStatus(_A)
class _LexipxTrapNetworkAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_LexipxTrapNetworkAddress_Type.__name__=_I
_LexipxTrapNetworkAddress_Object=MibTableColumn
lexipxTrapNetworkAddress=_LexipxTrapNetworkAddress_Object((1,3,6,1,4,1,641,1,3,12,1,3),_LexipxTrapNetworkAddress_Type())
lexipxTrapNetworkAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxTrapNetworkAddress.setStatus(_A)
class _LexipxTrapNodeAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_LexipxTrapNodeAddress_Type.__name__=_I
_LexipxTrapNodeAddress_Object=MibTableColumn
lexipxTrapNodeAddress=_LexipxTrapNodeAddress_Object((1,3,6,1,4,1,641,1,3,12,1,4),_LexipxTrapNodeAddress_Type())
lexipxTrapNodeAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxTrapNodeAddress.setStatus(_A)
class _LexipxTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_LexipxTrapType_Type.__name__=_C
_LexipxTrapType_Object=MibScalar
lexipxTrapType=_LexipxTrapType_Object((1,3,6,1,4,1,641,1,3,13),_LexipxTrapType_Type())
lexipxTrapType.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxTrapType.setStatus(_A)
class _LexipxGSQ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_LexipxGSQ_Type.__name__=_C
_LexipxGSQ_Object=MibScalar
lexipxGSQ=_LexipxGSQ_Object((1,3,6,1,4,1,641,1,3,14),_LexipxGSQ_Type())
lexipxGSQ.setMaxAccess(_D)
if mibBuilder.loadTexts:lexipxGSQ.setStatus(_A)
_Lextalk_ObjectIdentity=ObjectIdentity
lextalk=_Lextalk_ObjectIdentity((1,3,6,1,4,1,641,1,4))
class _LextalkActivated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_M,2)))
_LextalkActivated_Type.__name__=_C
_LextalkActivated_Object=MibScalar
lextalkActivated=_LextalkActivated_Object((1,3,6,1,4,1,641,1,4,1),_LextalkActivated_Type())
lextalkActivated.setMaxAccess(_D)
if mibBuilder.loadTexts:lextalkActivated.setStatus(_A)
class _LextalkAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_LextalkAddress_Type.__name__=_E
_LextalkAddress_Object=MibScalar
lextalkAddress=_LextalkAddress_Object((1,3,6,1,4,1,641,1,4,2),_LextalkAddress_Type())
lextalkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lextalkAddress.setStatus(_A)
class _LextalkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LextalkName_Type.__name__=_E
_LextalkName_Object=MibScalar
lextalkName=_LextalkName_Object((1,3,6,1,4,1,641,1,4,3),_LextalkName_Type())
lextalkName.setMaxAccess(_B)
if mibBuilder.loadTexts:lextalkName.setStatus(_A)
class _LextalkZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LextalkZone_Type.__name__=_E
_LextalkZone_Object=MibScalar
lextalkZone=_LextalkZone_Object((1,3,6,1,4,1,641,1,4,4),_LextalkZone_Type())
lextalkZone.setMaxAccess(_B)
if mibBuilder.loadTexts:lextalkZone.setStatus(_A)
class _LextalkType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LextalkType_Type.__name__=_E
_LextalkType_Object=MibScalar
lextalkType=_LextalkType_Object((1,3,6,1,4,1,641,1,4,5),_LextalkType_Type())
lextalkType.setMaxAccess(_B)
if mibBuilder.loadTexts:lextalkType.setStatus(_A)
_Lextcp_ObjectIdentity=ObjectIdentity
lextcp=_Lextcp_ObjectIdentity((1,3,6,1,4,1,641,1,5))
class _LextcpActivated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_M,2)))
_LextcpActivated_Type.__name__=_C
_LextcpActivated_Object=MibScalar
lextcpActivated=_LextcpActivated_Object((1,3,6,1,4,1,641,1,5,1),_LextcpActivated_Type())
lextcpActivated.setMaxAccess(_D)
if mibBuilder.loadTexts:lextcpActivated.setStatus(_A)
class _LextcpBootpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LextcpBootpEnable_Type.__name__=_C
_LextcpBootpEnable_Object=MibScalar
lextcpBootpEnable=_LextcpBootpEnable_Object((1,3,6,1,4,1,641,1,5,2),_LextcpBootpEnable_Type())
lextcpBootpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lextcpBootpEnable.setStatus(_A)
_LextcpAddressServ_Type=IpAddress
_LextcpAddressServ_Object=MibScalar
lextcpAddressServ=_LextcpAddressServ_Object((1,3,6,1,4,1,641,1,5,3),_LextcpAddressServ_Type())
lextcpAddressServ.setMaxAccess(_B)
if mibBuilder.loadTexts:lextcpAddressServ.setStatus(_A)
_LextcpNumNPAPservers_Type=Integer32
_LextcpNumNPAPservers_Object=MibScalar
lextcpNumNPAPservers=_LextcpNumNPAPservers_Object((1,3,6,1,4,1,641,1,5,4),_LextcpNumNPAPservers_Type())
lextcpNumNPAPservers.setMaxAccess(_B)
if mibBuilder.loadTexts:lextcpNumNPAPservers.setStatus(_A)
_LextcpNPAPserversTable_Object=MibTable
lextcpNPAPserversTable=_LextcpNPAPserversTable_Object((1,3,6,1,4,1,641,1,5,5))
if mibBuilder.loadTexts:lextcpNPAPserversTable.setStatus(_A)
_LextcpNPAPserversEntry_Object=MibTableRow
lextcpNPAPserversEntry=_LextcpNPAPserversEntry_Object((1,3,6,1,4,1,641,1,5,5,1))
lextcpNPAPserversEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:lextcpNPAPserversEntry.setStatus(_A)
class _LextcpNPAPserverIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LextcpNPAPserverIndex_Type.__name__=_C
_LextcpNPAPserverIndex_Object=MibTableColumn
lextcpNPAPserverIndex=_LextcpNPAPserverIndex_Object((1,3,6,1,4,1,641,1,5,5,1,1),_LextcpNPAPserverIndex_Type())
lextcpNPAPserverIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lextcpNPAPserverIndex.setStatus(_A)
_LextcpNPAPserverAddress_Type=IpAddress
_LextcpNPAPserverAddress_Object=MibTableColumn
lextcpNPAPserverAddress=_LextcpNPAPserverAddress_Object((1,3,6,1,4,1,641,1,5,5,1,2),_LextcpNPAPserverAddress_Type())
lextcpNPAPserverAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lextcpNPAPserverAddress.setStatus(_A)
_Lexhttp_ObjectIdentity=ObjectIdentity
lexhttp=_Lexhttp_ObjectIdentity((1,3,6,1,4,1,641,1,5,6))
class _LexhttpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LexhttpEnable_Type.__name__=_C
_LexhttpEnable_Object=MibScalar
lexhttpEnable=_LexhttpEnable_Object((1,3,6,1,4,1,641,1,5,6,1),_LexhttpEnable_Type())
lexhttpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhttpEnable.setStatus(_A)
class _LexhttpNumLinks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LexhttpNumLinks_Type.__name__=_C
_LexhttpNumLinks_Object=MibScalar
lexhttpNumLinks=_LexhttpNumLinks_Object((1,3,6,1,4,1,641,1,5,6,2),_LexhttpNumLinks_Type())
lexhttpNumLinks.setMaxAccess(_B)
if mibBuilder.loadTexts:lexhttpNumLinks.setStatus(_A)
class _LexhttpBytesRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LexhttpBytesRemaining_Type.__name__=_C
_LexhttpBytesRemaining_Object=MibScalar
lexhttpBytesRemaining=_LexhttpBytesRemaining_Object((1,3,6,1,4,1,641,1,5,6,3),_LexhttpBytesRemaining_Type())
lexhttpBytesRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:lexhttpBytesRemaining.setStatus(_A)
class _LexhttpResetLinks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),('reset',2)))
_LexhttpResetLinks_Type.__name__=_C
_LexhttpResetLinks_Object=MibScalar
lexhttpResetLinks=_LexhttpResetLinks_Object((1,3,6,1,4,1,641,1,5,6,4),_LexhttpResetLinks_Type())
lexhttpResetLinks.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhttpResetLinks.setStatus(_A)
_LexhttpLinkTable_Object=MibTable
lexhttpLinkTable=_LexhttpLinkTable_Object((1,3,6,1,4,1,641,1,5,6,5))
if mibBuilder.loadTexts:lexhttpLinkTable.setStatus(_A)
_LexhttpLinkTableEntry_Object=MibTableRow
lexhttpLinkTableEntry=_LexhttpLinkTableEntry_Object((1,3,6,1,4,1,641,1,5,6,5,1))
lexhttpLinkTableEntry.setIndexNames((0,_F,_X))
if mibBuilder.loadTexts:lexhttpLinkTableEntry.setStatus(_A)
class _LexhttpLinkTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LexhttpLinkTableIndex_Type.__name__=_C
_LexhttpLinkTableIndex_Object=MibTableColumn
lexhttpLinkTableIndex=_LexhttpLinkTableIndex_Object((1,3,6,1,4,1,641,1,5,6,5,1,1),_LexhttpLinkTableIndex_Type())
lexhttpLinkTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lexhttpLinkTableIndex.setStatus(_A)
class _LexhttpLinkTableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('linkOff',1),('customOn',2),('useDefault',3),('defaultOff',4),('defaultOn',5),('eraseCustom',6)))
_LexhttpLinkTableStatus_Type.__name__=_C
_LexhttpLinkTableStatus_Object=MibTableColumn
lexhttpLinkTableStatus=_LexhttpLinkTableStatus_Object((1,3,6,1,4,1,641,1,5,6,5,1,2),_LexhttpLinkTableStatus_Type())
lexhttpLinkTableStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhttpLinkTableStatus.setStatus(_A)
class _LexhttpLinkTableLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LexhttpLinkTableLabel_Type.__name__=_E
_LexhttpLinkTableLabel_Object=MibTableColumn
lexhttpLinkTableLabel=_LexhttpLinkTableLabel_Object((1,3,6,1,4,1,641,1,5,6,5,1,3),_LexhttpLinkTableLabel_Type())
lexhttpLinkTableLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhttpLinkTableLabel.setStatus(_A)
class _LexhttpLinkTableURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LexhttpLinkTableURL_Type.__name__=_E
_LexhttpLinkTableURL_Object=MibTableColumn
lexhttpLinkTableURL=_LexhttpLinkTableURL_Object((1,3,6,1,4,1,641,1,5,6,5,1,4),_LexhttpLinkTableURL_Type())
lexhttpLinkTableURL.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhttpLinkTableURL.setStatus(_A)
class _LexhttpConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LexhttpConfigEnable_Type.__name__=_C
_LexhttpConfigEnable_Object=MibScalar
lexhttpConfigEnable=_LexhttpConfigEnable_Object((1,3,6,1,4,1,641,1,5,6,6),_LexhttpConfigEnable_Type())
lexhttpConfigEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhttpConfigEnable.setStatus('obsolete')
_Lexdhcp_ObjectIdentity=ObjectIdentity
lexdhcp=_Lexdhcp_ObjectIdentity((1,3,6,1,4,1,641,1,5,7))
class _LexdhcpDhcpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LexdhcpDhcpEnable_Type.__name__=_C
_LexdhcpDhcpEnable_Object=MibScalar
lexdhcpDhcpEnable=_LexdhcpDhcpEnable_Object((1,3,6,1,4,1,641,1,5,7,1),_LexdhcpDhcpEnable_Type())
lexdhcpDhcpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lexdhcpDhcpEnable.setStatus(_A)
class _LexdhcpRarpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_LexdhcpRarpEnable_Type.__name__=_C
_LexdhcpRarpEnable_Object=MibScalar
lexdhcpRarpEnable=_LexdhcpRarpEnable_Object((1,3,6,1,4,1,641,1,5,7,2),_LexdhcpRarpEnable_Type())
lexdhcpRarpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lexdhcpRarpEnable.setStatus(_A)
class _LexdhcpAddressSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('manual',1),('dhcp',2),('bootp',3),('rarp',4)))
_LexdhcpAddressSource_Type.__name__=_C
_LexdhcpAddressSource_Object=MibScalar
lexdhcpAddressSource=_LexdhcpAddressSource_Object((1,3,6,1,4,1,641,1,5,7,3),_LexdhcpAddressSource_Type())
lexdhcpAddressSource.setMaxAccess(_B)
if mibBuilder.loadTexts:lexdhcpAddressSource.setStatus(_A)
class _LexdhcpWinsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unregistered',1),('registered',2),('pending',3),('rejected',4)))
_LexdhcpWinsStatus_Type.__name__=_C
_LexdhcpWinsStatus_Object=MibScalar
lexdhcpWinsStatus=_LexdhcpWinsStatus_Object((1,3,6,1,4,1,641,1,5,7,4),_LexdhcpWinsStatus_Type())
lexdhcpWinsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lexdhcpWinsStatus.setStatus(_A)
_LexdhcpWinsServer_Type=IpAddress
_LexdhcpWinsServer_Object=MibScalar
lexdhcpWinsServer=_LexdhcpWinsServer_Object((1,3,6,1,4,1,641,1,5,7,5),_LexdhcpWinsServer_Type())
lexdhcpWinsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:lexdhcpWinsServer.setStatus(_A)
class _LexdhcpHostname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_LexdhcpHostname_Type.__name__=_E
_LexdhcpHostname_Object=MibScalar
lexdhcpHostname=_LexdhcpHostname_Object((1,3,6,1,4,1,641,1,5,7,6),_LexdhcpHostname_Type())
lexdhcpHostname.setMaxAccess(_D)
if mibBuilder.loadTexts:lexdhcpHostname.setStatus(_A)
_LexdhcpLeaseLength_Type=Integer32
_LexdhcpLeaseLength_Object=MibScalar
lexdhcpLeaseLength=_LexdhcpLeaseLength_Object((1,3,6,1,4,1,641,1,5,7,7),_LexdhcpLeaseLength_Type())
lexdhcpLeaseLength.setMaxAccess(_B)
if mibBuilder.loadTexts:lexdhcpLeaseLength.setStatus(_A)
_LexdhcpTimetoExpire_Type=Integer32
_LexdhcpTimetoExpire_Object=MibScalar
lexdhcpTimetoExpire=_LexdhcpTimetoExpire_Object((1,3,6,1,4,1,641,1,5,7,8),_LexdhcpTimetoExpire_Type())
lexdhcpTimetoExpire.setMaxAccess(_B)
if mibBuilder.loadTexts:lexdhcpTimetoExpire.setStatus(_A)
_LexdhcpDNSServer_Type=IpAddress
_LexdhcpDNSServer_Object=MibScalar
lexdhcpDNSServer=_LexdhcpDNSServer_Object((1,3,6,1,4,1,641,1,5,7,9),_LexdhcpDNSServer_Type())
lexdhcpDNSServer.setMaxAccess(_D)
if mibBuilder.loadTexts:lexdhcpDNSServer.setStatus(_A)
_Lexhdwr_ObjectIdentity=ObjectIdentity
lexhdwr=_Lexhdwr_ObjectIdentity((1,3,6,1,4,1,641,1,6))
class _LexhdwrNumPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LexhdwrNumPorts_Type.__name__=_C
_LexhdwrNumPorts_Object=MibScalar
lexhdwrNumPorts=_LexhdwrNumPorts_Object((1,3,6,1,4,1,641,1,6,1),_LexhdwrNumPorts_Type())
lexhdwrNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:lexhdwrNumPorts.setStatus(_A)
_LexhdwrPortTable_Object=MibTable
lexhdwrPortTable=_LexhdwrPortTable_Object((1,3,6,1,4,1,641,1,6,2))
if mibBuilder.loadTexts:lexhdwrPortTable.setStatus(_A)
_LexhdwrPortTableEntry_Object=MibTableRow
lexhdwrPortTableEntry=_LexhdwrPortTableEntry_Object((1,3,6,1,4,1,641,1,6,2,1))
lexhdwrPortTableEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:lexhdwrPortTableEntry.setStatus(_A)
class _LexhdwrPortTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LexhdwrPortTableIndex_Type.__name__=_C
_LexhdwrPortTableIndex_Object=MibTableColumn
lexhdwrPortTableIndex=_LexhdwrPortTableIndex_Object((1,3,6,1,4,1,641,1,6,2,1,1),_LexhdwrPortTableIndex_Type())
lexhdwrPortTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lexhdwrPortTableIndex.setStatus(_A)
class _LexhdwrPortTableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('internal',1),('parallel',2),('serial',3)))
_LexhdwrPortTableType_Type.__name__=_C
_LexhdwrPortTableType_Object=MibTableColumn
lexhdwrPortTableType=_LexhdwrPortTableType_Object((1,3,6,1,4,1,641,1,6,2,1,2),_LexhdwrPortTableType_Type())
lexhdwrPortTableType.setMaxAccess(_B)
if mibBuilder.loadTexts:lexhdwrPortTableType.setStatus(_A)
_LexhdwrPortTableParm1_Type=Integer32
_LexhdwrPortTableParm1_Object=MibTableColumn
lexhdwrPortTableParm1=_LexhdwrPortTableParm1_Object((1,3,6,1,4,1,641,1,6,2,1,3),_LexhdwrPortTableParm1_Type())
lexhdwrPortTableParm1.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhdwrPortTableParm1.setStatus(_A)
_LexhdwrPortTableParm2_Type=Integer32
_LexhdwrPortTableParm2_Object=MibTableColumn
lexhdwrPortTableParm2=_LexhdwrPortTableParm2_Object((1,3,6,1,4,1,641,1,6,2,1,4),_LexhdwrPortTableParm2_Type())
lexhdwrPortTableParm2.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhdwrPortTableParm2.setStatus(_A)
_LexhdwrPortTableParm3_Type=Integer32
_LexhdwrPortTableParm3_Object=MibTableColumn
lexhdwrPortTableParm3=_LexhdwrPortTableParm3_Object((1,3,6,1,4,1,641,1,6,2,1,5),_LexhdwrPortTableParm3_Type())
lexhdwrPortTableParm3.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhdwrPortTableParm3.setStatus(_A)
_LexhdwrPortTableParm4_Type=Integer32
_LexhdwrPortTableParm4_Object=MibTableColumn
lexhdwrPortTableParm4=_LexhdwrPortTableParm4_Object((1,3,6,1,4,1,641,1,6,2,1,6),_LexhdwrPortTableParm4_Type())
lexhdwrPortTableParm4.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhdwrPortTableParm4.setStatus(_A)
_LexhdwrPortTableParm5_Type=Integer32
_LexhdwrPortTableParm5_Object=MibTableColumn
lexhdwrPortTableParm5=_LexhdwrPortTableParm5_Object((1,3,6,1,4,1,641,1,6,2,1,7),_LexhdwrPortTableParm5_Type())
lexhdwrPortTableParm5.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhdwrPortTableParm5.setStatus(_A)
_LexhdwrPortTableParm6_Type=Integer32
_LexhdwrPortTableParm6_Object=MibTableColumn
lexhdwrPortTableParm6=_LexhdwrPortTableParm6_Object((1,3,6,1,4,1,641,1,6,2,1,8),_LexhdwrPortTableParm6_Type())
lexhdwrPortTableParm6.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhdwrPortTableParm6.setStatus(_A)
class _LexhdwrPortTableParm7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_M,2),('auto',3)))
_LexhdwrPortTableParm7_Type.__name__=_C
_LexhdwrPortTableParm7_Object=MibTableColumn
lexhdwrPortTableParm7=_LexhdwrPortTableParm7_Object((1,3,6,1,4,1,641,1,6,2,1,9),_LexhdwrPortTableParm7_Type())
lexhdwrPortTableParm7.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhdwrPortTableParm7.setStatus(_A)
class _LexhdwrPortTableParm8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('npapInactive',1),('npapActive',2)))
_LexhdwrPortTableParm8_Type.__name__=_C
_LexhdwrPortTableParm8_Object=MibTableColumn
lexhdwrPortTableParm8=_LexhdwrPortTableParm8_Object((1,3,6,1,4,1,641,1,6,2,1,10),_LexhdwrPortTableParm8_Type())
lexhdwrPortTableParm8.setMaxAccess(_B)
if mibBuilder.loadTexts:lexhdwrPortTableParm8.setStatus(_A)
class _LexhdwrPortTableParm9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),('fax',2)))
_LexhdwrPortTableParm9_Type.__name__=_C
_LexhdwrPortTableParm9_Object=MibTableColumn
lexhdwrPortTableParm9=_LexhdwrPortTableParm9_Object((1,3,6,1,4,1,641,1,6,2,1,11),_LexhdwrPortTableParm9_Type())
lexhdwrPortTableParm9.setMaxAccess(_D)
if mibBuilder.loadTexts:lexhdwrPortTableParm9.setStatus(_A)
_Lexmac_ObjectIdentity=ObjectIdentity
lexmac=_Lexmac_ObjectIdentity((1,3,6,1,4,1,641,1,7))
class _LexmacType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LexmacType_Type.__name__=_E
_LexmacType_Object=MibScalar
lexmacType=_LexmacType_Object((1,3,6,1,4,1,641,1,7,1),_LexmacType_Type())
lexmacType.setMaxAccess(_B)
if mibBuilder.loadTexts:lexmacType.setStatus(_A)
_LexmacSpeed_Type=Gauge32
_LexmacSpeed_Object=MibScalar
lexmacSpeed=_LexmacSpeed_Object((1,3,6,1,4,1,641,1,7,2),_LexmacSpeed_Type())
lexmacSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:lexmacSpeed.setStatus(_A)
class _LexmacConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('aui',1),('bnc',2),('stp',3),('utp',4)))
_LexmacConnType_Type.__name__=_C
_LexmacConnType_Object=MibScalar
lexmacConnType=_LexmacConnType_Object((1,3,6,1,4,1,641,1,7,3),_LexmacConnType_Type())
lexmacConnType.setMaxAccess(_B)
if mibBuilder.loadTexts:lexmacConnType.setStatus(_A)
_LexmacUAA_Type=PhysAddress
_LexmacUAA_Object=MibScalar
lexmacUAA=_LexmacUAA_Object((1,3,6,1,4,1,641,1,7,4),_LexmacUAA_Type())
lexmacUAA.setMaxAccess(_B)
if mibBuilder.loadTexts:lexmacUAA.setStatus(_A)
_LexmacLAA_Type=PhysAddress
_LexmacLAA_Object=MibScalar
lexmacLAA=_LexmacLAA_Object((1,3,6,1,4,1,641,1,7,5),_LexmacLAA_Type())
lexmacLAA.setMaxAccess(_B)
if mibBuilder.loadTexts:lexmacLAA.setStatus(_A)
_Lextrap_ObjectIdentity=ObjectIdentity
lextrap=_Lextrap_ObjectIdentity((1,3,6,1,4,1,641,1,8))
_LextrapDestNum_Type=Integer32
_LextrapDestNum_Object=MibScalar
lextrapDestNum=_LextrapDestNum_Object((1,3,6,1,4,1,641,1,8,1),_LextrapDestNum_Type())
lextrapDestNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lextrapDestNum.setStatus(_A)
_LextrapDestTable_Object=MibTable
lextrapDestTable=_LextrapDestTable_Object((1,3,6,1,4,1,641,1,8,2))
if mibBuilder.loadTexts:lextrapDestTable.setStatus(_A)
_LextrapDestEntry_Object=MibTableRow
lextrapDestEntry=_LextrapDestEntry_Object((1,3,6,1,4,1,641,1,8,2,1))
lextrapDestEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:lextrapDestEntry.setStatus(_A)
class _LextrapDestIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LextrapDestIndex_Type.__name__=_C
_LextrapDestIndex_Object=MibTableColumn
lextrapDestIndex=_LextrapDestIndex_Object((1,3,6,1,4,1,641,1,8,2,1,1),_LextrapDestIndex_Type())
lextrapDestIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lextrapDestIndex.setStatus(_A)
_LextrapDestIPAddr_Type=IpAddress
_LextrapDestIPAddr_Object=MibTableColumn
lextrapDestIPAddr=_LextrapDestIPAddr_Object((1,3,6,1,4,1,641,1,8,2,1,2),_LextrapDestIPAddr_Type())
lextrapDestIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:lextrapDestIPAddr.setStatus(_A)
class _LextrapDestMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LextrapDestMask_Type.__name__=_C
_LextrapDestMask_Object=MibTableColumn
lextrapDestMask=_LextrapDestMask_Object((1,3,6,1,4,1,641,1,8,2,1,3),_LextrapDestMask_Type())
lextrapDestMask.setMaxAccess(_D)
if mibBuilder.loadTexts:lextrapDestMask.setStatus(_A)
class _LextrapIPTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_LextrapIPTrapType_Type.__name__=_C
_LextrapIPTrapType_Object=MibScalar
lextrapIPTrapType=_LextrapIPTrapType_Object((1,3,6,1,4,1,641,1,8,3),_LextrapIPTrapType_Type())
lextrapIPTrapType.setMaxAccess(_D)
if mibBuilder.loadTexts:lextrapIPTrapType.setStatus(_A)
_Time_ObjectIdentity=ObjectIdentity
time=_Time_ObjectIdentity((1,3,6,1,4,1,641,1,9))
class _TimeReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),('reset',2)))
_TimeReset_Type.__name__=_C
_TimeReset_Object=MibScalar
timeReset=_TimeReset_Object((1,3,6,1,4,1,641,1,9,1),_TimeReset_Type())
timeReset.setMaxAccess(_D)
if mibBuilder.loadTexts:timeReset.setStatus(_A)
class _TimeSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ntp',2),('netware',3)))
_TimeSource_Type.__name__=_C
_TimeSource_Object=MibScalar
timeSource=_TimeSource_Object((1,3,6,1,4,1,641,1,9,2),_TimeSource_Type())
timeSource.setMaxAccess(_D)
if mibBuilder.loadTexts:timeSource.setStatus(_A)
class _TimeUTCOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-720,720))
_TimeUTCOffset_Type.__name__=_C
_TimeUTCOffset_Object=MibScalar
timeUTCOffset=_TimeUTCOffset_Object((1,3,6,1,4,1,641,1,9,3),_TimeUTCOffset_Type())
timeUTCOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:timeUTCOffset.setStatus(_A)
class _TimeDSTEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_TimeDSTEnable_Type.__name__=_C
_TimeDSTEnable_Object=MibScalar
timeDSTEnable=_TimeDSTEnable_Object((1,3,6,1,4,1,641,1,9,4),_TimeDSTEnable_Type())
timeDSTEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:timeDSTEnable.setStatus(_A)
class _TimeDSTStartDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_TimeDSTStartDate_Type.__name__=_I
_TimeDSTStartDate_Object=MibScalar
timeDSTStartDate=_TimeDSTStartDate_Object((1,3,6,1,4,1,641,1,9,5),_TimeDSTStartDate_Type())
timeDSTStartDate.setMaxAccess(_B)
if mibBuilder.loadTexts:timeDSTStartDate.setStatus(_A)
class _TimeDSTEndDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_TimeDSTEndDate_Type.__name__=_I
_TimeDSTEndDate_Object=MibScalar
timeDSTEndDate=_TimeDSTEndDate_Object((1,3,6,1,4,1,641,1,9,6),_TimeDSTEndDate_Type())
timeDSTEndDate.setMaxAccess(_B)
if mibBuilder.loadTexts:timeDSTEndDate.setStatus(_A)
class _TimeDSTOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_TimeDSTOffset_Type.__name__=_C
_TimeDSTOffset_Object=MibScalar
timeDSTOffset=_TimeDSTOffset_Object((1,3,6,1,4,1,641,1,9,7),_TimeDSTOffset_Type())
timeDSTOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:timeDSTOffset.setStatus(_A)
_TimeServerAddress_Type=IpAddress
_TimeServerAddress_Object=MibScalar
timeServerAddress=_TimeServerAddress_Object((1,3,6,1,4,1,641,1,9,8),_TimeServerAddress_Type())
timeServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:timeServerAddress.setStatus(_A)
class _TimeServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_TimeServerName_Type.__name__=_E
_TimeServerName_Object=MibScalar
timeServerName=_TimeServerName_Object((1,3,6,1,4,1,641,1,9,9),_TimeServerName_Type())
timeServerName.setMaxAccess(_D)
if mibBuilder.loadTexts:timeServerName.setStatus(_A)
_Printer_ObjectIdentity=ObjectIdentity
printer=_Printer_ObjectIdentity((1,3,6,1,4,1,641,2))
_Prtgen_ObjectIdentity=ObjectIdentity
prtgen=_Prtgen_ObjectIdentity((1,3,6,1,4,1,641,2,1))
_PrtgenNumber_Type=Integer32
_PrtgenNumber_Object=MibScalar
prtgenNumber=_PrtgenNumber_Object((1,3,6,1,4,1,641,2,1,1),_PrtgenNumber_Type())
prtgenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenNumber.setStatus(_A)
_PrtgenInfoTable_Object=MibTable
prtgenInfoTable=_PrtgenInfoTable_Object((1,3,6,1,4,1,641,2,1,2))
if mibBuilder.loadTexts:prtgenInfoTable.setStatus(_A)
_PrtgenInfoEntry_Object=MibTableRow
prtgenInfoEntry=_PrtgenInfoEntry_Object((1,3,6,1,4,1,641,2,1,2,1))
prtgenInfoEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:prtgenInfoEntry.setStatus(_A)
class _PrtgenPrinterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PrtgenPrinterIndex_Type.__name__=_C
_PrtgenPrinterIndex_Object=MibTableColumn
prtgenPrinterIndex=_PrtgenPrinterIndex_Object((1,3,6,1,4,1,641,2,1,2,1,1),_PrtgenPrinterIndex_Type())
prtgenPrinterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenPrinterIndex.setStatus(_A)
class _PrtgenPrinterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtgenPrinterName_Type.__name__=_E
_PrtgenPrinterName_Object=MibTableColumn
prtgenPrinterName=_PrtgenPrinterName_Object((1,3,6,1,4,1,641,2,1,2,1,2),_PrtgenPrinterName_Type())
prtgenPrinterName.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenPrinterName.setStatus(_A)
class _PrtgenPeripheralID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtgenPeripheralID_Type.__name__=_E
_PrtgenPeripheralID_Object=MibTableColumn
prtgenPeripheralID=_PrtgenPeripheralID_Object((1,3,6,1,4,1,641,2,1,2,1,3),_PrtgenPeripheralID_Type())
prtgenPeripheralID.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenPeripheralID.setStatus(_A)
class _PrtgenCodeRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtgenCodeRevision_Type.__name__=_E
_PrtgenCodeRevision_Object=MibTableColumn
prtgenCodeRevision=_PrtgenCodeRevision_Object((1,3,6,1,4,1,641,2,1,2,1,4),_PrtgenCodeRevision_Type())
prtgenCodeRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenCodeRevision.setStatus(_A)
_PrtgenResValue_Type=Integer32
_PrtgenResValue_Object=MibTableColumn
prtgenResValue=_PrtgenResValue_Object((1,3,6,1,4,1,641,2,1,2,1,5),_PrtgenResValue_Type())
prtgenResValue.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenResValue.setStatus(_A)
class _PrtgenSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtgenSerialNo_Type.__name__=_E
_PrtgenSerialNo_Object=MibTableColumn
prtgenSerialNo=_PrtgenSerialNo_Object((1,3,6,1,4,1,641,2,1,2,1,6),_PrtgenSerialNo_Type())
prtgenSerialNo.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenSerialNo.setStatus(_A)
class _PrtgenAssetTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtgenAssetTag_Type.__name__=_E
_PrtgenAssetTag_Object=MibTableColumn
prtgenAssetTag=_PrtgenAssetTag_Object((1,3,6,1,4,1,641,2,1,2,1,7),_PrtgenAssetTag_Type())
prtgenAssetTag.setMaxAccess(_D)
if mibBuilder.loadTexts:prtgenAssetTag.setStatus(_A)
_PrtgenStatusTable_Object=MibTable
prtgenStatusTable=_PrtgenStatusTable_Object((1,3,6,1,4,1,641,2,1,3))
if mibBuilder.loadTexts:prtgenStatusTable.setStatus(_A)
_PrtgenStatusEntry_Object=MibTableRow
prtgenStatusEntry=_PrtgenStatusEntry_Object((1,3,6,1,4,1,641,2,1,3,1))
prtgenStatusEntry.setIndexNames((0,_F,_c))
if mibBuilder.loadTexts:prtgenStatusEntry.setStatus(_A)
class _PrtgenStatPrinterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PrtgenStatPrinterIndex_Type.__name__=_C
_PrtgenStatPrinterIndex_Object=MibTableColumn
prtgenStatPrinterIndex=_PrtgenStatPrinterIndex_Object((1,3,6,1,4,1,641,2,1,3,1,1),_PrtgenStatPrinterIndex_Type())
prtgenStatPrinterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatPrinterIndex.setStatus(_A)
_PrtgenStatusIRC_Type=Integer32
_PrtgenStatusIRC_Object=MibTableColumn
prtgenStatusIRC=_PrtgenStatusIRC_Object((1,3,6,1,4,1,641,2,1,3,1,2),_PrtgenStatusIRC_Type())
prtgenStatusIRC.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusIRC.setStatus(_A)
class _PrtgenStatusOutHopFull_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notFull',1),('full',2),(_G,3)))
_PrtgenStatusOutHopFull_Type.__name__=_C
_PrtgenStatusOutHopFull_Object=MibTableColumn
prtgenStatusOutHopFull=_PrtgenStatusOutHopFull_Object((1,3,6,1,4,1,641,2,1,3,1,3),_PrtgenStatusOutHopFull_Type())
prtgenStatusOutHopFull.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusOutHopFull.setStatus(_A)
class _PrtgenStatusInputEmpty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notEmpty',1),('empty',2),(_G,3)))
_PrtgenStatusInputEmpty_Type.__name__=_C
_PrtgenStatusInputEmpty_Object=MibTableColumn
prtgenStatusInputEmpty=_PrtgenStatusInputEmpty_Object((1,3,6,1,4,1,641,2,1,3,1,4),_PrtgenStatusInputEmpty_Type())
prtgenStatusInputEmpty.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusInputEmpty.setStatus(_A)
class _PrtgenStatusPaperJam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notJammed',1),('jamed',2),(_G,3)))
_PrtgenStatusPaperJam_Type.__name__=_C
_PrtgenStatusPaperJam_Object=MibTableColumn
prtgenStatusPaperJam=_PrtgenStatusPaperJam_Object((1,3,6,1,4,1,641,2,1,3,1,5),_PrtgenStatusPaperJam_Type())
prtgenStatusPaperJam.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusPaperJam.setStatus(_A)
class _PrtgenStatusTonerError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noTonerError',1),('tonerError',2),(_G,3)))
_PrtgenStatusTonerError_Type.__name__=_C
_PrtgenStatusTonerError_Object=MibTableColumn
prtgenStatusTonerError=_PrtgenStatusTonerError_Object((1,3,6,1,4,1,641,2,1,3,1,6),_PrtgenStatusTonerError_Type())
prtgenStatusTonerError.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusTonerError.setStatus(_A)
class _PrtgenStatusSrvcReqd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noServiceRequired',1),('serviceRequired',2),(_G,3)))
_PrtgenStatusSrvcReqd_Type.__name__=_C
_PrtgenStatusSrvcReqd_Object=MibTableColumn
prtgenStatusSrvcReqd=_PrtgenStatusSrvcReqd_Object((1,3,6,1,4,1,641,2,1,3,1,7),_PrtgenStatusSrvcReqd_Type())
prtgenStatusSrvcReqd.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusSrvcReqd.setStatus(_A)
class _PrtgenStatusDiskError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noDiskError',1),('diskError',2),(_G,3)))
_PrtgenStatusDiskError_Type.__name__=_C
_PrtgenStatusDiskError_Object=MibTableColumn
prtgenStatusDiskError=_PrtgenStatusDiskError_Object((1,3,6,1,4,1,641,2,1,3,1,8),_PrtgenStatusDiskError_Type())
prtgenStatusDiskError.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusDiskError.setStatus(_A)
class _PrtgenStatusCoverOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noCoverOpen',1),('coverOpen',2),(_G,3)))
_PrtgenStatusCoverOpen_Type.__name__=_C
_PrtgenStatusCoverOpen_Object=MibTableColumn
prtgenStatusCoverOpen=_PrtgenStatusCoverOpen_Object((1,3,6,1,4,1,641,2,1,3,1,9),_PrtgenStatusCoverOpen_Type())
prtgenStatusCoverOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusCoverOpen.setStatus(_A)
class _PrtgenStatusPageComplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noComplexPage',1),('complexPage',2),(_G,3)))
_PrtgenStatusPageComplex_Type.__name__=_C
_PrtgenStatusPageComplex_Object=MibTableColumn
prtgenStatusPageComplex=_PrtgenStatusPageComplex_Object((1,3,6,1,4,1,641,2,1,3,1,10),_PrtgenStatusPageComplex_Type())
prtgenStatusPageComplex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusPageComplex.setStatus(_A)
class _PrtgenStatusLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('online',1),('offline',2),(_G,3)))
_PrtgenStatusLineStatus_Type.__name__=_C
_PrtgenStatusLineStatus_Object=MibTableColumn
prtgenStatusLineStatus=_PrtgenStatusLineStatus_Object((1,3,6,1,4,1,641,2,1,3,1,11),_PrtgenStatusLineStatus_Type())
prtgenStatusLineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusLineStatus.setStatus(_A)
class _PrtgenStatusBusy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notBusy',1),('busy',2),(_G,3)))
_PrtgenStatusBusy_Type.__name__=_C
_PrtgenStatusBusy_Object=MibTableColumn
prtgenStatusBusy=_PrtgenStatusBusy_Object((1,3,6,1,4,1,641,2,1,3,1,12),_PrtgenStatusBusy_Type())
prtgenStatusBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusBusy.setStatus(_A)
class _PrtgenStatusWaiting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notWaiting',1),('waiting',2),(_G,3)))
_PrtgenStatusWaiting_Type.__name__=_C
_PrtgenStatusWaiting_Object=MibTableColumn
prtgenStatusWaiting=_PrtgenStatusWaiting_Object((1,3,6,1,4,1,641,2,1,3,1,13),_PrtgenStatusWaiting_Type())
prtgenStatusWaiting.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusWaiting.setStatus(_A)
class _PrtgenStatusWarming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notWarming',1),('warming',2),(_G,3)))
_PrtgenStatusWarming_Type.__name__=_C
_PrtgenStatusWarming_Object=MibTableColumn
prtgenStatusWarming=_PrtgenStatusWarming_Object((1,3,6,1,4,1,641,2,1,3,1,14),_PrtgenStatusWarming_Type())
prtgenStatusWarming.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusWarming.setStatus(_A)
class _PrtgenStatusPrinting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notPrinting',1),('printing',2),(_G,3)))
_PrtgenStatusPrinting_Type.__name__=_C
_PrtgenStatusPrinting_Object=MibTableColumn
prtgenStatusPrinting=_PrtgenStatusPrinting_Object((1,3,6,1,4,1,641,2,1,3,1,15),_PrtgenStatusPrinting_Type())
prtgenStatusPrinting.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenStatusPrinting.setStatus(_A)
_PrtgenFamilyID_Type=Integer32
_PrtgenFamilyID_Object=MibScalar
prtgenFamilyID=_PrtgenFamilyID_Object((1,3,6,1,4,1,641,2,1,4),_PrtgenFamilyID_Type())
prtgenFamilyID.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgenFamilyID.setStatus(_A)
_Pgcount_ObjectIdentity=ObjectIdentity
pgcount=_Pgcount_ObjectIdentity((1,3,6,1,4,1,641,2,1,5))
_PgTotal_Type=Counter32
_PgTotal_Object=MibScalar
pgTotal=_PgTotal_Object((1,3,6,1,4,1,641,2,1,5,1),_PgTotal_Type())
pgTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:pgTotal.setStatus(_A)
_PgMono_Type=Counter32
_PgMono_Object=MibScalar
pgMono=_PgMono_Object((1,3,6,1,4,1,641,2,1,5,2),_PgMono_Type())
pgMono.setMaxAccess(_B)
if mibBuilder.loadTexts:pgMono.setStatus(_A)
_PgColor_Type=Counter32
_PgColor_Object=MibScalar
pgColor=_PgColor_Object((1,3,6,1,4,1,641,2,1,5,3),_PgColor_Type())
pgColor.setMaxAccess(_B)
if mibBuilder.loadTexts:pgColor.setStatus(_A)
_Attachment_ObjectIdentity=ObjectIdentity
attachment=_Attachment_ObjectIdentity((1,3,6,1,4,1,641,3))
_Fax_ObjectIdentity=ObjectIdentity
fax=_Fax_ObjectIdentity((1,3,6,1,4,1,641,3,1))
_FaxNumber_Type=Integer32
_FaxNumber_Object=MibScalar
faxNumber=_FaxNumber_Object((1,3,6,1,4,1,641,3,1,1),_FaxNumber_Type())
faxNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:faxNumber.setStatus(_A)
_FaxTable_Object=MibTable
faxTable=_FaxTable_Object((1,3,6,1,4,1,641,3,1,2))
if mibBuilder.loadTexts:faxTable.setStatus(_A)
_FaxEntry_Object=MibTableRow
faxEntry=_FaxEntry_Object((1,3,6,1,4,1,641,3,1,2,1))
faxEntry.setIndexNames((0,_F,_d))
if mibBuilder.loadTexts:faxEntry.setStatus(_A)
class _FaxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FaxIndex_Type.__name__=_C
_FaxIndex_Object=MibTableColumn
faxIndex=_FaxIndex_Object((1,3,6,1,4,1,641,3,1,2,1,1),_FaxIndex_Type())
faxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:faxIndex.setStatus(_A)
class _FaxPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(145,146,147,148,149)));namedValues=NamedValues(*(('serial1',145),('serial2',146),('serial3',147),('serial4',148),('serial5',149)))
_FaxPort_Type.__name__=_C
_FaxPort_Object=MibTableColumn
faxPort=_FaxPort_Object((1,3,6,1,4,1,641,3,1,2,1,2),_FaxPort_Type())
faxPort.setMaxAccess(_B)
if mibBuilder.loadTexts:faxPort.setStatus(_A)
class _FaxAdapterCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FaxAdapterCapabilities_Type.__name__=_C
_FaxAdapterCapabilities_Object=MibTableColumn
faxAdapterCapabilities=_FaxAdapterCapabilities_Object((1,3,6,1,4,1,641,3,1,2,1,3),_FaxAdapterCapabilities_Type())
faxAdapterCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:faxAdapterCapabilities.setStatus(_A)
class _FaxModemCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FaxModemCapabilities_Type.__name__=_C
_FaxModemCapabilities_Object=MibTableColumn
faxModemCapabilities=_FaxModemCapabilities_Object((1,3,6,1,4,1,641,3,1,2,1,4),_FaxModemCapabilities_Type())
faxModemCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:faxModemCapabilities.setStatus(_A)
class _FaxSelectedCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FaxSelectedCapabilities_Type.__name__=_C
_FaxSelectedCapabilities_Object=MibTableColumn
faxSelectedCapabilities=_FaxSelectedCapabilities_Object((1,3,6,1,4,1,641,3,1,2,1,5),_FaxSelectedCapabilities_Type())
faxSelectedCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:faxSelectedCapabilities.setStatus(_A)
class _FaxActiveCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FaxActiveCapabilities_Type.__name__=_C
_FaxActiveCapabilities_Object=MibTableColumn
faxActiveCapabilities=_FaxActiveCapabilities_Object((1,3,6,1,4,1,641,3,1,2,1,6),_FaxActiveCapabilities_Type())
faxActiveCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:faxActiveCapabilities.setStatus(_A)
class _FaxIDString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FaxIDString_Type.__name__=_E
_FaxIDString_Object=MibTableColumn
faxIDString=_FaxIDString_Object((1,3,6,1,4,1,641,3,1,2,1,7),_FaxIDString_Type())
faxIDString.setMaxAccess(_D)
if mibBuilder.loadTexts:faxIDString.setStatus(_A)
class _FaxInitString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FaxInitString_Type.__name__=_E
_FaxInitString_Object=MibTableColumn
faxInitString=_FaxInitString_Object((1,3,6,1,4,1,641,3,1,2,1,8),_FaxInitString_Type())
faxInitString.setMaxAccess(_D)
if mibBuilder.loadTexts:faxInitString.setStatus(_A)
class _FaxNumberRings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FaxNumberRings_Type.__name__=_C
_FaxNumberRings_Object=MibTableColumn
faxNumberRings=_FaxNumberRings_Object((1,3,6,1,4,1,641,3,1,2,1,9),_FaxNumberRings_Type())
faxNumberRings.setMaxAccess(_D)
if mibBuilder.loadTexts:faxNumberRings.setStatus(_A)
class _FaxScaling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('scaleToFit',1),('cropToFit',2)))
_FaxScaling_Type.__name__=_C
_FaxScaling_Object=MibTableColumn
faxScaling=_FaxScaling_Object((1,3,6,1,4,1,641,3,1,2,1,10),_FaxScaling_Type())
faxScaling.setMaxAccess(_D)
if mibBuilder.loadTexts:faxScaling.setStatus(_A)
class _FaxBinaryEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('taggedBinary',1),('ascii85',2)))
_FaxBinaryEncoding_Type.__name__=_C
_FaxBinaryEncoding_Object=MibTableColumn
faxBinaryEncoding=_FaxBinaryEncoding_Object((1,3,6,1,4,1,641,3,1,2,1,11),_FaxBinaryEncoding_Type())
faxBinaryEncoding.setMaxAccess(_D)
if mibBuilder.loadTexts:faxBinaryEncoding.setStatus(_A)
class _FaxPrinterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(129,130,255)));namedValues=NamedValues(*(('parallel1',129),('parallel2',130),('firstAvail',255)))
_FaxPrinterPort_Type.__name__=_C
_FaxPrinterPort_Object=MibTableColumn
faxPrinterPort=_FaxPrinterPort_Object((1,3,6,1,4,1,641,3,1,2,1,13),_FaxPrinterPort_Type())
faxPrinterPort.setMaxAccess(_D)
if mibBuilder.loadTexts:faxPrinterPort.setStatus(_A)
_FaxInputTray_Type=Integer32
_FaxInputTray_Object=MibTableColumn
faxInputTray=_FaxInputTray_Object((1,3,6,1,4,1,641,3,1,2,1,14),_FaxInputTray_Type())
faxInputTray.setMaxAccess(_D)
if mibBuilder.loadTexts:faxInputTray.setStatus(_A)
_FaxOutputBin_Type=Integer32
_FaxOutputBin_Object=MibTableColumn
faxOutputBin=_FaxOutputBin_Object((1,3,6,1,4,1,641,3,1,2,1,15),_FaxOutputBin_Type())
faxOutputBin.setMaxAccess(_D)
if mibBuilder.loadTexts:faxOutputBin.setStatus(_A)
irCleared=NotificationType((1,3,6,1,4,1,641,1,0,0))
irCleared.setObjects((_F,_H))
if mibBuilder.loadTexts:irCleared.setStatus('')
irCondition=NotificationType((1,3,6,1,4,1,641,1,0,1))
irCondition.setObjects((_F,_H))
if mibBuilder.loadTexts:irCondition.setStatus('')
irOutputFull=NotificationType((1,3,6,1,4,1,641,1,0,2))
irOutputFull.setObjects((_F,_H))
if mibBuilder.loadTexts:irOutputFull.setStatus('')
irLoadPaper=NotificationType((1,3,6,1,4,1,641,1,0,3))
irLoadPaper.setObjects((_F,_H))
if mibBuilder.loadTexts:irLoadPaper.setStatus('')
irPaperJam=NotificationType((1,3,6,1,4,1,641,1,0,4))
irPaperJam.setObjects((_F,_H))
if mibBuilder.loadTexts:irPaperJam.setStatus('')
irTonerLow=NotificationType((1,3,6,1,4,1,641,1,0,5))
irTonerLow.setObjects((_F,_H))
if mibBuilder.loadTexts:irTonerLow.setStatus('')
irServiceReq=NotificationType((1,3,6,1,4,1,641,1,0,6))
irServiceReq.setObjects((_F,_H))
if mibBuilder.loadTexts:irServiceReq.setStatus('')
irDiskErr=NotificationType((1,3,6,1,4,1,641,1,0,7))
irDiskErr.setObjects((_F,_H))
if mibBuilder.loadTexts:irDiskErr.setStatus('')
irCoverOpen=NotificationType((1,3,6,1,4,1,641,1,0,8))
irCoverOpen.setObjects((_F,_H))
if mibBuilder.loadTexts:irCoverOpen.setStatus('')
irPageComplexity=NotificationType((1,3,6,1,4,1,641,1,0,9))
irPageComplexity.setObjects((_F,_H))
if mibBuilder.loadTexts:irPageComplexity.setStatus('')
irOffline=NotificationType((1,3,6,1,4,1,641,1,0,10))
irOffline.setObjects((_F,_H))
if mibBuilder.loadTexts:irOffline.setStatus('')
irClearedTypeII=NotificationType((1,3,6,1,4,1,641,1,0,11))
irClearedTypeII.setObjects((_F,_H))
if mibBuilder.loadTexts:irClearedTypeII.setStatus('')
mibBuilder.exportSymbols(_F,**{'lexmark':lexmark,'adapter':adapter,'irCleared':irCleared,'irCondition':irCondition,'irOutputFull':irOutputFull,'irLoadPaper':irLoadPaper,'irPaperJam':irPaperJam,'irTonerLow':irTonerLow,'irServiceReq':irServiceReq,'irDiskErr':irDiskErr,'irCoverOpen':irCoverOpen,'irPageComplexity':irPageComplexity,'irOffline':irOffline,'irClearedTypeII':irClearedTypeII,'opsys':opsys,'opsysCodeRev':opsysCodeRev,'opsysJobTimeout':opsysJobTimeout,'opsysCurrentJob':opsysCurrentJob,'opsysRAMSize':opsysRAMSize,'opsysNVRAMSize':opsysNVRAMSize,'opsysROMSize':opsysROMSize,'opsysROMType':opsysROMType,'opsysProtocols':opsysProtocols,'opsysTimeToReset':opsysTimeToReset,'opsysCardPartNo':opsysCardPartNo,'opsysCardEC':opsysCardEC,'opsysCurrentJobTable':opsysCurrentJobTable,'opsysCurrentJobEntry':opsysCurrentJobEntry,_O:opsysCurrentJobEntryIndex,'opsysCurrentJobString':opsysCurrentJobString,'opsysDeviceType':opsysDeviceType,'opsysAdapterName':opsysAdapterName,'opsysAdapterCapabilities':opsysAdapterCapabilities,'lexlink':lexlink,'lexlinkActivated':lexlinkActivated,'lexlinkNickname':lexlinkNickname,'lexipx':lexipx,'lexipxActivated':lexipxActivated,'lexipxLoginName':lexipxLoginName,'lexipxNetNumber':lexipxNetNumber,'lexipxSAPMode':lexipxSAPMode,'lexipxServerMode':lexipxServerMode,'lexipxNumPorts':lexipxNumPorts,'lexipxPortInfoTable':lexipxPortInfoTable,'lexipxPortInfoEntry':lexipxPortInfoEntry,_P:lexipxPortInfoIndex,'lexipxPortInfoPollIntvl':lexipxPortInfoPollIntvl,'lexipxPortInfoEnable':lexipxPortInfoEnable,'lexipxPortInfoBannerPage':lexipxPortInfoBannerPage,'lexipxNumPrefServers':lexipxNumPrefServers,'lexipxPrefSrvrTable':lexipxPrefSrvrTable,'lexipxPrefSrvrEntry':lexipxPrefSrvrEntry,_Q:lexipxPrefSrvrIndex,'lexipxPrefSrvrName':lexipxPrefSrvrName,'lexipxConnSrvrTable':lexipxConnSrvrTable,'lexipxConnSrvrEntry':lexipxConnSrvrEntry,_R:lexipxConnSrvrIndex,'lexipxConnSrvrName':lexipxConnSrvrName,'lexipxConnSrvrNet':lexipxConnSrvrNet,'lexipxConnSrvrNode':lexipxConnSrvrNode,'lexipxConnSrvrConnNum':lexipxConnSrvrConnNum,'lexipxConnSrvrConnId':lexipxConnSrvrConnId,'lexipxConnSrvrPSConnID':lexipxConnSrvrPSConnID,'lexipxFrameType':lexipxFrameType,'lexipxTrapTable':lexipxTrapTable,'lexipxTrapEntry':lexipxTrapEntry,_S:lexipxTrapIndex,'lexipxTrapMask':lexipxTrapMask,'lexipxTrapNetworkAddress':lexipxTrapNetworkAddress,'lexipxTrapNodeAddress':lexipxTrapNodeAddress,'lexipxTrapType':lexipxTrapType,'lexipxGSQ':lexipxGSQ,'lextalk':lextalk,'lextalkActivated':lextalkActivated,'lextalkAddress':lextalkAddress,'lextalkName':lextalkName,'lextalkZone':lextalkZone,'lextalkType':lextalkType,'lextcp':lextcp,'lextcpActivated':lextcpActivated,'lextcpBootpEnable':lextcpBootpEnable,'lextcpAddressServ':lextcpAddressServ,'lextcpNumNPAPservers':lextcpNumNPAPservers,'lextcpNPAPserversTable':lextcpNPAPserversTable,'lextcpNPAPserversEntry':lextcpNPAPserversEntry,_V:lextcpNPAPserverIndex,'lextcpNPAPserverAddress':lextcpNPAPserverAddress,'lexhttp':lexhttp,'lexhttpEnable':lexhttpEnable,'lexhttpNumLinks':lexhttpNumLinks,'lexhttpBytesRemaining':lexhttpBytesRemaining,'lexhttpResetLinks':lexhttpResetLinks,'lexhttpLinkTable':lexhttpLinkTable,'lexhttpLinkTableEntry':lexhttpLinkTableEntry,_X:lexhttpLinkTableIndex,'lexhttpLinkTableStatus':lexhttpLinkTableStatus,'lexhttpLinkTableLabel':lexhttpLinkTableLabel,'lexhttpLinkTableURL':lexhttpLinkTableURL,'lexhttpConfigEnable':lexhttpConfigEnable,'lexdhcp':lexdhcp,'lexdhcpDhcpEnable':lexdhcpDhcpEnable,'lexdhcpRarpEnable':lexdhcpRarpEnable,'lexdhcpAddressSource':lexdhcpAddressSource,'lexdhcpWinsStatus':lexdhcpWinsStatus,'lexdhcpWinsServer':lexdhcpWinsServer,'lexdhcpHostname':lexdhcpHostname,'lexdhcpLeaseLength':lexdhcpLeaseLength,'lexdhcpTimetoExpire':lexdhcpTimetoExpire,'lexdhcpDNSServer':lexdhcpDNSServer,'lexhdwr':lexhdwr,'lexhdwrNumPorts':lexhdwrNumPorts,'lexhdwrPortTable':lexhdwrPortTable,'lexhdwrPortTableEntry':lexhdwrPortTableEntry,_Y:lexhdwrPortTableIndex,'lexhdwrPortTableType':lexhdwrPortTableType,'lexhdwrPortTableParm1':lexhdwrPortTableParm1,'lexhdwrPortTableParm2':lexhdwrPortTableParm2,'lexhdwrPortTableParm3':lexhdwrPortTableParm3,'lexhdwrPortTableParm4':lexhdwrPortTableParm4,'lexhdwrPortTableParm5':lexhdwrPortTableParm5,'lexhdwrPortTableParm6':lexhdwrPortTableParm6,'lexhdwrPortTableParm7':lexhdwrPortTableParm7,'lexhdwrPortTableParm8':lexhdwrPortTableParm8,'lexhdwrPortTableParm9':lexhdwrPortTableParm9,'lexmac':lexmac,'lexmacType':lexmacType,'lexmacSpeed':lexmacSpeed,'lexmacConnType':lexmacConnType,'lexmacUAA':lexmacUAA,'lexmacLAA':lexmacLAA,'lextrap':lextrap,'lextrapDestNum':lextrapDestNum,'lextrapDestTable':lextrapDestTable,'lextrapDestEntry':lextrapDestEntry,_a:lextrapDestIndex,'lextrapDestIPAddr':lextrapDestIPAddr,'lextrapDestMask':lextrapDestMask,'lextrapIPTrapType':lextrapIPTrapType,'time':time,'timeReset':timeReset,'timeSource':timeSource,'timeUTCOffset':timeUTCOffset,'timeDSTEnable':timeDSTEnable,'timeDSTStartDate':timeDSTStartDate,'timeDSTEndDate':timeDSTEndDate,'timeDSTOffset':timeDSTOffset,'timeServerAddress':timeServerAddress,'timeServerName':timeServerName,_Z:printer,'prtgen':prtgen,'prtgenNumber':prtgenNumber,'prtgenInfoTable':prtgenInfoTable,'prtgenInfoEntry':prtgenInfoEntry,_b:prtgenPrinterIndex,'prtgenPrinterName':prtgenPrinterName,'prtgenPeripheralID':prtgenPeripheralID,'prtgenCodeRevision':prtgenCodeRevision,'prtgenResValue':prtgenResValue,'prtgenSerialNo':prtgenSerialNo,'prtgenAssetTag':prtgenAssetTag,'prtgenStatusTable':prtgenStatusTable,'prtgenStatusEntry':prtgenStatusEntry,_c:prtgenStatPrinterIndex,_H:prtgenStatusIRC,'prtgenStatusOutHopFull':prtgenStatusOutHopFull,'prtgenStatusInputEmpty':prtgenStatusInputEmpty,'prtgenStatusPaperJam':prtgenStatusPaperJam,'prtgenStatusTonerError':prtgenStatusTonerError,'prtgenStatusSrvcReqd':prtgenStatusSrvcReqd,'prtgenStatusDiskError':prtgenStatusDiskError,'prtgenStatusCoverOpen':prtgenStatusCoverOpen,'prtgenStatusPageComplex':prtgenStatusPageComplex,'prtgenStatusLineStatus':prtgenStatusLineStatus,'prtgenStatusBusy':prtgenStatusBusy,'prtgenStatusWaiting':prtgenStatusWaiting,'prtgenStatusWarming':prtgenStatusWarming,'prtgenStatusPrinting':prtgenStatusPrinting,'prtgenFamilyID':prtgenFamilyID,'pgcount':pgcount,'pgTotal':pgTotal,'pgMono':pgMono,'pgColor':pgColor,'attachment':attachment,'fax':fax,'faxNumber':faxNumber,'faxTable':faxTable,'faxEntry':faxEntry,_d:faxIndex,'faxPort':faxPort,'faxAdapterCapabilities':faxAdapterCapabilities,'faxModemCapabilities':faxModemCapabilities,'faxSelectedCapabilities':faxSelectedCapabilities,'faxActiveCapabilities':faxActiveCapabilities,'faxIDString':faxIDString,'faxInitString':faxInitString,'faxNumberRings':faxNumberRings,'faxScaling':faxScaling,'faxBinaryEncoding':faxBinaryEncoding,'faxPrinterPort':faxPrinterPort,'faxInputTray':faxInputTray,'faxOutputBin':faxOutputBin})