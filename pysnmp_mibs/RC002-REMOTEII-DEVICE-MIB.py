_q='rcftRemoteIIEthFxSfpExist'
_p='rcftRemoteIIEthFxSfpRXLOS'
_o='rcftRemoteIIEthFxPortLink'
_n='rcftRemoteIIEthFxPortSD'
_m='rcftRemoteIIEthFxPortLaserAbnormal'
_l='rcftRemoteIIEthFxPortRxSensitiveAbnormal'
_k='rcftRemoteIIEthFxPortTxPowerAbnormal'
_j='rcftRemoteIIEthFxPortTLK'
_i='rcftRemoteIIEthFxPortRLK'
_h='rcftRemoteIIEthFeLinkStatus'
_g='rcftRemoteIISysTemperature'
_f='rcftRemoteIIDeviceExist'
_e='rcftRemoteIIEthFxStatisticEntry'
_d='rcftRemoteIIEthFeStatisticEntry'
_c='rcftRemoteIIVLANIndex'
_b='rcftRemoteIIEthFxIndex'
_a='half-duplex'
_Z='full-duplex'
_Y='rcft10Gbps'
_X='rcft1000Mbps'
_W='rcft100Mbps'
_V='rcft10Mbps'
_U='rcftRemoteIISysVoltageStatus'
_T='abnormal'
_S='unlink'
_R='link'
_Q='rcftRemoteIIEthFeIndex'
_P='unknown'
_O='disable'
_N='enable'
_M='close'
_L='open'
_K='OctetString'
_J='normal'
_I='rcftRemoteIIDeviceIndex'
_H='rcftSlotIndex'
_G='rcftChassisIndex'
_F='RAISECOM-RCFT-MIB'
_E='RC002-REMOTEII-DEVICE-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rcftChassisIndex,rcftMibObjects,rcftSlotIndex=mibBuilder.importSymbols(_F,_G,'rcftMibObjects',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
rcftRemoteIIDeviceMib=ModuleIdentity((1,3,6,1,4,1,8886,2,1,7))
if mibBuilder.loadTexts:rcftRemoteIIDeviceMib.setRevisions(('1905-07-06 00:00','1909-02-09 00:00','1909-03-06 15:00','1909-03-23 00:00','1909-04-15 00:00','1909-09-02 10:00','1909-09-08 14:30','1910-04-28 17:34','1910-10-22 16:57'))
_RcftRemoteIIDeviceSystemMIB_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceSystemMIB=_RcftRemoteIIDeviceSystemMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,1))
_RcftRemoteIIDeviceSysObjects_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceSysObjects=_RcftRemoteIIDeviceSysObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,1,1))
_RcftRemoteIIDeviceSysTable_Object=MibTable
rcftRemoteIIDeviceSysTable=_RcftRemoteIIDeviceSysTable_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1))
if mibBuilder.loadTexts:rcftRemoteIIDeviceSysTable.setStatus(_A)
_RcftRemoteIIDeviceSysEntry_Object=MibTableRow
rcftRemoteIIDeviceSysEntry=_RcftRemoteIIDeviceSysEntry_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1))
rcftRemoteIIDeviceSysEntry.setIndexNames((0,_F,_G),(0,_F,_H),(0,_E,_I))
if mibBuilder.loadTexts:rcftRemoteIIDeviceSysEntry.setStatus(_A)
_RcftRemoteIIDeviceIndex_Type=Integer32
_RcftRemoteIIDeviceIndex_Object=MibTableColumn
rcftRemoteIIDeviceIndex=_RcftRemoteIIDeviceIndex_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,1),_RcftRemoteIIDeviceIndex_Type())
rcftRemoteIIDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceIndex.setStatus(_A)
class _RcftRemoteIIDeviceExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exist',1),('noexist',2)))
_RcftRemoteIIDeviceExist_Type.__name__=_C
_RcftRemoteIIDeviceExist_Object=MibTableColumn
rcftRemoteIIDeviceExist=_RcftRemoteIIDeviceExist_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,2),_RcftRemoteIIDeviceExist_Type())
rcftRemoteIIDeviceExist.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceExist.setStatus(_A)
class _RcftRemoteIIDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,65025,65026,65027)));namedValues=NamedValues(*(('rcftTypeRC501-FE-REV-C',30001),('rcftTypeRC601-FE-REV-C',30002),('rcftTypeRC511-FE-REV-A',30003),('rcftTypeRC511-4FE-REV-A',30004),('rcftTypeRC601-FE-REV-E',30005),('rcftTypeRC511-FE-C-REV-A',30006),('rcftTypeRC513-FE-REV-A',30007),('rcftTypeRC513-FE-C-REV-A',30008),('rcftTypeRC532-FE-REV-A',30009),('rcftTypeRC531-FE-REV-A',30010),('rcftTypeRC532-2FE-REV-A',30011),('rcftTypeRC512-FE-DoubleFiber-S-REV-A',30012),('rcftTypeRC512-FE-SingleFiber-S-REV-A',30013),('rcftTypeRC512-FE-DoubleFiber-C-REV-A',30014),('rcftTypeRC512-FE-SingleFiber-C-REV-A',30015),('rcftTypeRC512-FE-SS34-S-REV-A',30016),('rcftTypeRC512-FE-SS34-C-REV-A',30017),('rcftTypeRC512-FE-SS13-SLAVE',30019),('rcftTypeRC512-FE-SS23-SLAVE',30020),('rcftTypeRC512-FE-SS34-SLAVE',30021),('rcftTypeRC552-FE-REV-A-SLAVE-NEW',30022),('rcftTypeRC511-4FE-REV-B-SLAVE',30023),('rcftTypeRC521H-FE-DoubleFiber-S',30024),('rcftTypeRC521H-FE-SingleFiber-S',30025),('rcftTypeRC521H-FE-S',30026),('rcftTypeRC522E-FE-REMOTE',30027),('rcftTypeRC521E-FE',30028),('rcftTypeRC512-FE',30029),('rcftTypeRC512-FE-SLAVE',30030),('rcftTypeTS1000-UNCONFIG-PRODUCT',65025),('rcftTypeRC521-FE-REV-C',65026),('rcftTypeRC521-FE-REV-D',65027)))
_RcftRemoteIIDeviceType_Type.__name__=_C
_RcftRemoteIIDeviceType_Object=MibTableColumn
rcftRemoteIIDeviceType=_RcftRemoteIIDeviceType_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,3),_RcftRemoteIIDeviceType_Type())
rcftRemoteIIDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceType.setStatus(_A)
_RcftRemoteIIDeviceToRDeviceID_Type=Integer32
_RcftRemoteIIDeviceToRDeviceID_Object=MibTableColumn
rcftRemoteIIDeviceToRDeviceID=_RcftRemoteIIDeviceToRDeviceID_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,4),_RcftRemoteIIDeviceToRDeviceID_Type())
rcftRemoteIIDeviceToRDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceToRDeviceID.setStatus(_A)
class _RcftRemoteIIDeviceToRPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ethport',1),('optical',2),('e1port',3)))
_RcftRemoteIIDeviceToRPortType_Type.__name__=_C
_RcftRemoteIIDeviceToRPortType_Object=MibTableColumn
rcftRemoteIIDeviceToRPortType=_RcftRemoteIIDeviceToRPortType_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,5),_RcftRemoteIIDeviceToRPortType_Type())
rcftRemoteIIDeviceToRPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceToRPortType.setStatus(_A)
_RcftRemoteIIDeviceToRPortIndex_Type=Integer32
_RcftRemoteIIDeviceToRPortIndex_Object=MibTableColumn
rcftRemoteIIDeviceToRPortIndex=_RcftRemoteIIDeviceToRPortIndex_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,6),_RcftRemoteIIDeviceToRPortIndex_Type())
rcftRemoteIIDeviceToRPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceToRPortIndex.setStatus(_A)
class _RcftRemoteIIDeviceVersionInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_RcftRemoteIIDeviceVersionInfo_Type.__name__=_K
_RcftRemoteIIDeviceVersionInfo_Object=MibTableColumn
rcftRemoteIIDeviceVersionInfo=_RcftRemoteIIDeviceVersionInfo_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,7),_RcftRemoteIIDeviceVersionInfo_Type())
rcftRemoteIIDeviceVersionInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceVersionInfo.setStatus(_A)
_RcftRemoteIISysTemperature_Type=Integer32
_RcftRemoteIISysTemperature_Object=MibTableColumn
rcftRemoteIISysTemperature=_RcftRemoteIISysTemperature_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,8),_RcftRemoteIISysTemperature_Type())
rcftRemoteIISysTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIISysTemperature.setStatus(_A)
class _RcftRemoteIISysVoltageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('toohigh',2),('toolow',3)))
_RcftRemoteIISysVoltageStatus_Type.__name__=_C
_RcftRemoteIISysVoltageStatus_Object=MibTableColumn
rcftRemoteIISysVoltageStatus=_RcftRemoteIISysVoltageStatus_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,9),_RcftRemoteIISysVoltageStatus_Type())
rcftRemoteIISysVoltageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIISysVoltageStatus.setStatus(_A)
class _RcftRemoteIIDeviceFrameLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('framelen1916B',1),('framelen1536B',2)))
_RcftRemoteIIDeviceFrameLen_Type.__name__=_C
_RcftRemoteIIDeviceFrameLen_Object=MibTableColumn
rcftRemoteIIDeviceFrameLen=_RcftRemoteIIDeviceFrameLen_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,10),_RcftRemoteIIDeviceFrameLen_Type())
rcftRemoteIIDeviceFrameLen.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIDeviceFrameLen.setStatus(_A)
class _RcftRemoteIIDeviceOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reset',1),('reqInfoStart',2),('reqInfoStop',3),('linePortInsideLoopEnable',4),('linePortOutsideLoopEnable',5),('linePortInsideLoopDisable',6),('linePortOutsideLoopDisable',7)))
_RcftRemoteIIDeviceOrder_Type.__name__=_C
_RcftRemoteIIDeviceOrder_Object=MibTableColumn
rcftRemoteIIDeviceOrder=_RcftRemoteIIDeviceOrder_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,11),_RcftRemoteIIDeviceOrder_Type())
rcftRemoteIIDeviceOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIDeviceOrder.setStatus(_A)
class _RcftRemoteIIDeviceConfigFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('set',1))
_RcftRemoteIIDeviceConfigFlag_Type.__name__=_C
_RcftRemoteIIDeviceConfigFlag_Object=MibTableColumn
rcftRemoteIIDeviceConfigFlag=_RcftRemoteIIDeviceConfigFlag_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,12),_RcftRemoteIIDeviceConfigFlag_Type())
rcftRemoteIIDeviceConfigFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIDeviceConfigFlag.setStatus(_A)
_RcftRemoteIIDeviceStatus_Type=Integer32
_RcftRemoteIIDeviceStatus_Object=MibTableColumn
rcftRemoteIIDeviceStatus=_RcftRemoteIIDeviceStatus_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,13),_RcftRemoteIIDeviceStatus_Type())
rcftRemoteIIDeviceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIDeviceStatus.setStatus(_A)
_RcftRemoteIIDeviceVenderCode_Type=Integer32
_RcftRemoteIIDeviceVenderCode_Object=MibTableColumn
rcftRemoteIIDeviceVenderCode=_RcftRemoteIIDeviceVenderCode_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,14),_RcftRemoteIIDeviceVenderCode_Type())
rcftRemoteIIDeviceVenderCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceVenderCode.setStatus(_A)
_RcftRemoteIIDeviceModelID_Type=Integer32
_RcftRemoteIIDeviceModelID_Object=MibTableColumn
rcftRemoteIIDeviceModelID=_RcftRemoteIIDeviceModelID_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,15),_RcftRemoteIIDeviceModelID_Type())
rcftRemoteIIDeviceModelID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceModelID.setStatus(_A)
_RcftRemoteIIDeviceLoopBackStatus_Type=Integer32
_RcftRemoteIIDeviceLoopBackStatus_Object=MibTableColumn
rcftRemoteIIDeviceLoopBackStatus=_RcftRemoteIIDeviceLoopBackStatus_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,16),_RcftRemoteIIDeviceLoopBackStatus_Type())
rcftRemoteIIDeviceLoopBackStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceLoopBackStatus.setStatus(_A)
_RcftRemoteIIDeviceLoopBackMode_Type=Integer32
_RcftRemoteIIDeviceLoopBackMode_Object=MibTableColumn
rcftRemoteIIDeviceLoopBackMode=_RcftRemoteIIDeviceLoopBackMode_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,17),_RcftRemoteIIDeviceLoopBackMode_Type())
rcftRemoteIIDeviceLoopBackMode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIDeviceLoopBackMode.setStatus(_A)
_RcftRemoteIIDeviceVLANType_Type=Integer32
_RcftRemoteIIDeviceVLANType_Object=MibTableColumn
rcftRemoteIIDeviceVLANType=_RcftRemoteIIDeviceVLANType_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,18),_RcftRemoteIIDeviceVLANType_Type())
rcftRemoteIIDeviceVLANType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIDeviceVLANType.setStatus(_A)
_RcftRemoteIIQosEnable_Type=Integer32
_RcftRemoteIIQosEnable_Object=MibTableColumn
rcftRemoteIIQosEnable=_RcftRemoteIIQosEnable_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,19),_RcftRemoteIIQosEnable_Type())
rcftRemoteIIQosEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIQosEnable.setStatus(_A)
_RcftRemoteIIBaseCOS_Type=Integer32
_RcftRemoteIIBaseCOS_Object=MibTableColumn
rcftRemoteIIBaseCOS=_RcftRemoteIIBaseCOS_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,20),_RcftRemoteIIBaseCOS_Type())
rcftRemoteIIBaseCOS.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIBaseCOS.setStatus(_A)
_RcftRemoteIIQueuesPolicy_Type=Integer32
_RcftRemoteIIQueuesPolicy_Object=MibTableColumn
rcftRemoteIIQueuesPolicy=_RcftRemoteIIQueuesPolicy_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,21),_RcftRemoteIIQueuesPolicy_Type())
rcftRemoteIIQueuesPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIQueuesPolicy.setStatus(_A)
_RcftRemoteIIDeviceQoSPolicy_Type=Integer32
_RcftRemoteIIDeviceQoSPolicy_Object=MibTableColumn
rcftRemoteIIDeviceQoSPolicy=_RcftRemoteIIDeviceQoSPolicy_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,22),_RcftRemoteIIDeviceQoSPolicy_Type())
rcftRemoteIIDeviceQoSPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIDeviceQoSPolicy.setStatus(_A)
class _RcftRemoteIIDeviceMibUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mib002',1),('rccomlib',2)))
_RcftRemoteIIDeviceMibUse_Type.__name__=_C
_RcftRemoteIIDeviceMibUse_Object=MibTableColumn
rcftRemoteIIDeviceMibUse=_RcftRemoteIIDeviceMibUse_Object((1,3,6,1,4,1,8886,2,1,7,1,1,1,1,23),_RcftRemoteIIDeviceMibUse_Type())
rcftRemoteIIDeviceMibUse.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIDeviceMibUse.setStatus(_A)
_RcftRemoteIIDeviceConfigFlagTable_Object=MibTable
rcftRemoteIIDeviceConfigFlagTable=_RcftRemoteIIDeviceConfigFlagTable_Object((1,3,6,1,4,1,8886,2,1,7,1,1,2))
if mibBuilder.loadTexts:rcftRemoteIIDeviceConfigFlagTable.setStatus(_A)
_RcftRemoteIIDeviceConfigFlagEntry_Object=MibTableRow
rcftRemoteIIDeviceConfigFlagEntry=_RcftRemoteIIDeviceConfigFlagEntry_Object((1,3,6,1,4,1,8886,2,1,7,1,1,2,1))
rcftRemoteIIDeviceConfigFlagEntry.setIndexNames((0,_F,_G),(0,_F,_H),(0,_E,_I))
if mibBuilder.loadTexts:rcftRemoteIIDeviceConfigFlagEntry.setStatus(_A)
_RcftRemoteIIDeviceConfigFinishFlag_Type=Integer32
_RcftRemoteIIDeviceConfigFinishFlag_Object=MibTableColumn
rcftRemoteIIDeviceConfigFinishFlag=_RcftRemoteIIDeviceConfigFinishFlag_Object((1,3,6,1,4,1,8886,2,1,7,1,1,2,1,1),_RcftRemoteIIDeviceConfigFinishFlag_Type())
rcftRemoteIIDeviceConfigFinishFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIDeviceConfigFinishFlag.setStatus(_A)
_RcftRemoteIIDeviceSysTraps_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceSysTraps=_RcftRemoteIIDeviceSysTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,1,2))
_RcftRemoteIIDeviceEthMIB_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceEthMIB=_RcftRemoteIIDeviceEthMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,2))
_RcftRemoteIIDeviceEthFeMIB_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceEthFeMIB=_RcftRemoteIIDeviceEthFeMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,2,1))
_RcftRemoteIIDeviceEthFeObjects_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceEthFeObjects=_RcftRemoteIIDeviceEthFeObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,2,1,1))
_RcftRemoteIIEthFePortTable_Object=MibTable
rcftRemoteIIEthFePortTable=_RcftRemoteIIEthFePortTable_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1))
if mibBuilder.loadTexts:rcftRemoteIIEthFePortTable.setStatus(_A)
_RcftRemoteIIEthFePortEntry_Object=MibTableRow
rcftRemoteIIEthFePortEntry=_RcftRemoteIIEthFePortEntry_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1))
rcftRemoteIIEthFePortEntry.setIndexNames((0,_F,_G),(0,_F,_H),(0,_E,_I),(0,_E,_Q))
if mibBuilder.loadTexts:rcftRemoteIIEthFePortEntry.setStatus(_A)
_RcftRemoteIIEthFeIndex_Type=Integer32
_RcftRemoteIIEthFeIndex_Object=MibTableColumn
rcftRemoteIIEthFeIndex=_RcftRemoteIIEthFeIndex_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,1),_RcftRemoteIIEthFeIndex_Type())
rcftRemoteIIEthFeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeIndex.setStatus(_A)
class _RcftRemoteIIEthFeLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linkup',1),('linkdown',2)))
_RcftRemoteIIEthFeLinkStatus_Type.__name__=_C
_RcftRemoteIIEthFeLinkStatus_Object=MibTableColumn
rcftRemoteIIEthFeLinkStatus=_RcftRemoteIIEthFeLinkStatus_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,2),_RcftRemoteIIEthFeLinkStatus_Type())
rcftRemoteIIEthFeLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeLinkStatus.setStatus(_A)
class _RcftRemoteIIEthFeShutDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),('closebyLocalOtherPortFault',3),('closebyOppositeFePortFault',4),('closebyLoopBack',5)))
_RcftRemoteIIEthFeShutDown_Type.__name__=_C
_RcftRemoteIIEthFeShutDown_Object=MibTableColumn
rcftRemoteIIEthFeShutDown=_RcftRemoteIIEthFeShutDown_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,3),_RcftRemoteIIEthFeShutDown_Type())
rcftRemoteIIEthFeShutDown.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeShutDown.setStatus(_A)
class _RcftRemoteIIEthFeAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manul',2)))
_RcftRemoteIIEthFeAutoNegotiation_Type.__name__=_C
_RcftRemoteIIEthFeAutoNegotiation_Object=MibTableColumn
rcftRemoteIIEthFeAutoNegotiation=_RcftRemoteIIEthFeAutoNegotiation_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,4),_RcftRemoteIIEthFeAutoNegotiation_Type())
rcftRemoteIIEthFeAutoNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeAutoNegotiation.setStatus(_A)
class _RcftRemoteIIEthFeSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,16)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4),('other',16)))
_RcftRemoteIIEthFeSpeed_Type.__name__=_C
_RcftRemoteIIEthFeSpeed_Object=MibTableColumn
rcftRemoteIIEthFeSpeed=_RcftRemoteIIEthFeSpeed_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,5),_RcftRemoteIIEthFeSpeed_Type())
rcftRemoteIIEthFeSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeSpeed.setStatus(_A)
class _RcftRemoteIIEthFeDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_RcftRemoteIIEthFeDuplex_Type.__name__=_C
_RcftRemoteIIEthFeDuplex_Object=MibTableColumn
rcftRemoteIIEthFeDuplex=_RcftRemoteIIEthFeDuplex_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,6),_RcftRemoteIIEthFeDuplex_Type())
rcftRemoteIIEthFeDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeDuplex.setStatus(_A)
_RcftRemoteIIEthFeRestrictSpeed_Type=Integer32
_RcftRemoteIIEthFeRestrictSpeed_Object=MibTableColumn
rcftRemoteIIEthFeRestrictSpeed=_RcftRemoteIIEthFeRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,7),_RcftRemoteIIEthFeRestrictSpeed_Type())
rcftRemoteIIEthFeRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeRestrictSpeed.setStatus(_A)
class _RcftRemoteIIEthFeFaultPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcftRemoteIIEthFeFaultPass_Type.__name__=_C
_RcftRemoteIIEthFeFaultPass_Object=MibTableColumn
rcftRemoteIIEthFeFaultPass=_RcftRemoteIIEthFeFaultPass_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,8),_RcftRemoteIIEthFeFaultPass_Type())
rcftRemoteIIEthFeFaultPass.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeFaultPass.setStatus(_A)
class _RcftRemoteIIEthFeDisabledByRemoteTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_RcftRemoteIIEthFeDisabledByRemoteTP_Type.__name__=_C
_RcftRemoteIIEthFeDisabledByRemoteTP_Object=MibTableColumn
rcftRemoteIIEthFeDisabledByRemoteTP=_RcftRemoteIIEthFeDisabledByRemoteTP_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,9),_RcftRemoteIIEthFeDisabledByRemoteTP_Type())
rcftRemoteIIEthFeDisabledByRemoteTP.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeDisabledByRemoteTP.setStatus(_A)
class _RcftRemoteIIEthFeDisabledByFxToFeFP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_RcftRemoteIIEthFeDisabledByFxToFeFP_Type.__name__=_C
_RcftRemoteIIEthFeDisabledByFxToFeFP_Object=MibTableColumn
rcftRemoteIIEthFeDisabledByFxToFeFP=_RcftRemoteIIEthFeDisabledByFxToFeFP_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,10),_RcftRemoteIIEthFeDisabledByFxToFeFP_Type())
rcftRemoteIIEthFeDisabledByFxToFeFP.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeDisabledByFxToFeFP.setStatus(_A)
_RcftRemoteIIEthFeTxRestrictSpeed_Type=Integer32
_RcftRemoteIIEthFeTxRestrictSpeed_Object=MibTableColumn
rcftRemoteIIEthFeTxRestrictSpeed=_RcftRemoteIIEthFeTxRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,11),_RcftRemoteIIEthFeTxRestrictSpeed_Type())
rcftRemoteIIEthFeTxRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeTxRestrictSpeed.setStatus(_A)
class _RcftRemoteIIEthFeTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tag',1),('untag',2)))
_RcftRemoteIIEthFeTag_Type.__name__=_C
_RcftRemoteIIEthFeTag_Object=MibTableColumn
rcftRemoteIIEthFeTag=_RcftRemoteIIEthFeTag_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,12),_RcftRemoteIIEthFeTag_Type())
rcftRemoteIIEthFeTag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeTag.setStatus(_A)
_RcftRemoteIIEthFePVID_Type=Integer32
_RcftRemoteIIEthFePVID_Object=MibTableColumn
rcftRemoteIIEthFePVID=_RcftRemoteIIEthFePVID_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,13),_RcftRemoteIIEthFePVID_Type())
rcftRemoteIIEthFePVID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFePVID.setStatus(_A)
_RcftRemoteIIEthFeQoSPolicy_Type=Integer32
_RcftRemoteIIEthFeQoSPolicy_Object=MibTableColumn
rcftRemoteIIEthFeQoSPolicy=_RcftRemoteIIEthFeQoSPolicy_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,1,1,14),_RcftRemoteIIEthFeQoSPolicy_Type())
rcftRemoteIIEthFeQoSPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeQoSPolicy.setStatus(_A)
_RcftRemoteIIEthFeStatisticTable_Object=MibTable
rcftRemoteIIEthFeStatisticTable=_RcftRemoteIIEthFeStatisticTable_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,2))
if mibBuilder.loadTexts:rcftRemoteIIEthFeStatisticTable.setStatus(_A)
_RcftRemoteIIEthFeStatisticEntry_Object=MibTableRow
rcftRemoteIIEthFeStatisticEntry=_RcftRemoteIIEthFeStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,2,1))
if mibBuilder.loadTexts:rcftRemoteIIEthFeStatisticEntry.setStatus(_A)
_RcftRemoteIIEthFeTxPackets_Type=Counter32
_RcftRemoteIIEthFeTxPackets_Object=MibTableColumn
rcftRemoteIIEthFeTxPackets=_RcftRemoteIIEthFeTxPackets_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,2,1,1),_RcftRemoteIIEthFeTxPackets_Type())
rcftRemoteIIEthFeTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeTxPackets.setStatus(_A)
_RcftRemoteIIEthFeTxBytes_Type=Counter32
_RcftRemoteIIEthFeTxBytes_Object=MibTableColumn
rcftRemoteIIEthFeTxBytes=_RcftRemoteIIEthFeTxBytes_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,2,1,2),_RcftRemoteIIEthFeTxBytes_Type())
rcftRemoteIIEthFeTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeTxBytes.setStatus(_A)
_RcftRemoteIIEthFeRxPackets_Type=Counter32
_RcftRemoteIIEthFeRxPackets_Object=MibTableColumn
rcftRemoteIIEthFeRxPackets=_RcftRemoteIIEthFeRxPackets_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,2,1,3),_RcftRemoteIIEthFeRxPackets_Type())
rcftRemoteIIEthFeRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeRxPackets.setStatus(_A)
_RcftRemoteIIEthFeRxBytes_Type=Counter32
_RcftRemoteIIEthFeRxBytes_Object=MibTableColumn
rcftRemoteIIEthFeRxBytes=_RcftRemoteIIEthFeRxBytes_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,2,1,4),_RcftRemoteIIEthFeRxBytes_Type())
rcftRemoteIIEthFeRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeRxBytes.setStatus(_A)
_RcftRemoteIIEthFeRxLostPackets_Type=Counter32
_RcftRemoteIIEthFeRxLostPackets_Object=MibTableColumn
rcftRemoteIIEthFeRxLostPackets=_RcftRemoteIIEthFeRxLostPackets_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,2,1,5),_RcftRemoteIIEthFeRxLostPackets_Type())
rcftRemoteIIEthFeRxLostPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeRxLostPackets.setStatus(_A)
_RcftRemoteIIEthFeFluxTimer_Type=Counter32
_RcftRemoteIIEthFeFluxTimer_Object=MibTableColumn
rcftRemoteIIEthFeFluxTimer=_RcftRemoteIIEthFeFluxTimer_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,2,1,6),_RcftRemoteIIEthFeFluxTimer_Type())
rcftRemoteIIEthFeFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeFluxTimer.setStatus(_A)
_RcftRemoteIIEthFeTxLostPackets_Type=Counter32
_RcftRemoteIIEthFeTxLostPackets_Object=MibTableColumn
rcftRemoteIIEthFeTxLostPackets=_RcftRemoteIIEthFeTxLostPackets_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,2,1,7),_RcftRemoteIIEthFeTxLostPackets_Type())
rcftRemoteIIEthFeTxLostPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFeTxLostPackets.setStatus(_A)
_RcftRemoteIIEthFePortConfTable_Object=MibTable
rcftRemoteIIEthFePortConfTable=_RcftRemoteIIEthFePortConfTable_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,3))
if mibBuilder.loadTexts:rcftRemoteIIEthFePortConfTable.setStatus(_A)
_RcftRemoteIIEthFePortConfEntry_Object=MibTableRow
rcftRemoteIIEthFePortConfEntry=_RcftRemoteIIEthFePortConfEntry_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,3,1))
rcftRemoteIIEthFePortConfEntry.setIndexNames((0,_F,_G),(0,_F,_H),(0,_E,_I),(0,_E,_Q))
if mibBuilder.loadTexts:rcftRemoteIIEthFePortConfEntry.setStatus(_A)
class _RcftRemoteIIEthFeConfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,16)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4),('other',16)))
_RcftRemoteIIEthFeConfSpeed_Type.__name__=_C
_RcftRemoteIIEthFeConfSpeed_Object=MibTableColumn
rcftRemoteIIEthFeConfSpeed=_RcftRemoteIIEthFeConfSpeed_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,3,1,1),_RcftRemoteIIEthFeConfSpeed_Type())
rcftRemoteIIEthFeConfSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeConfSpeed.setStatus(_A)
class _RcftRemoteIIEthFeConfDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_RcftRemoteIIEthFeConfDuplex_Type.__name__=_C
_RcftRemoteIIEthFeConfDuplex_Object=MibTableColumn
rcftRemoteIIEthFeConfDuplex=_RcftRemoteIIEthFeConfDuplex_Object((1,3,6,1,4,1,8886,2,1,7,2,1,1,3,1,2),_RcftRemoteIIEthFeConfDuplex_Type())
rcftRemoteIIEthFeConfDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFeConfDuplex.setStatus(_A)
_RcftRemoteIIDeviceEthFeTraps_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceEthFeTraps=_RcftRemoteIIDeviceEthFeTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,2,1,2))
_RcftRemoteIIDeviceEthFxMIB_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceEthFxMIB=_RcftRemoteIIDeviceEthFxMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,2,2))
_RcftRemoteIIDeviceEthFxObjects_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceEthFxObjects=_RcftRemoteIIDeviceEthFxObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,2,2,1))
_RcftRemoteIIEthFxPortTable_Object=MibTable
rcftRemoteIIEthFxPortTable=_RcftRemoteIIEthFxPortTable_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortTable.setStatus(_A)
_RcftRemoteIIEthFxPortEntry_Object=MibTableRow
rcftRemoteIIEthFxPortEntry=_RcftRemoteIIEthFxPortEntry_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1))
rcftRemoteIIEthFxPortEntry.setIndexNames((0,_F,_G),(0,_F,_H),(0,_E,_I),(0,_E,_b))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortEntry.setStatus(_A)
_RcftRemoteIIEthFxIndex_Type=Integer32
_RcftRemoteIIEthFxIndex_Object=MibTableColumn
rcftRemoteIIEthFxIndex=_RcftRemoteIIEthFxIndex_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,1),_RcftRemoteIIEthFxIndex_Type())
rcftRemoteIIEthFxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxIndex.setStatus(_A)
class _RcftRemoteIIEthFxPortRLK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_RcftRemoteIIEthFxPortRLK_Type.__name__=_C
_RcftRemoteIIEthFxPortRLK_Object=MibTableColumn
rcftRemoteIIEthFxPortRLK=_RcftRemoteIIEthFxPortRLK_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,2),_RcftRemoteIIEthFxPortRLK_Type())
rcftRemoteIIEthFxPortRLK.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortRLK.setStatus(_A)
class _RcftRemoteIIEthFxPortTLK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_RcftRemoteIIEthFxPortTLK_Type.__name__=_C
_RcftRemoteIIEthFxPortTLK_Object=MibTableColumn
rcftRemoteIIEthFxPortTLK=_RcftRemoteIIEthFxPortTLK_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,3),_RcftRemoteIIEthFxPortTLK_Type())
rcftRemoteIIEthFxPortTLK.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortTLK.setStatus(_A)
class _RcftRemoteIIEthFxPortSD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('sd',2)))
_RcftRemoteIIEthFxPortSD_Type.__name__=_C
_RcftRemoteIIEthFxPortSD_Object=MibTableColumn
rcftRemoteIIEthFxPortSD=_RcftRemoteIIEthFxPortSD_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,4),_RcftRemoteIIEthFxPortSD_Type())
rcftRemoteIIEthFxPortSD.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortSD.setStatus(_A)
class _RcftRemoteIIEthFxPortTxPowerAbnormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_T,2)))
_RcftRemoteIIEthFxPortTxPowerAbnormal_Type.__name__=_C
_RcftRemoteIIEthFxPortTxPowerAbnormal_Object=MibTableColumn
rcftRemoteIIEthFxPortTxPowerAbnormal=_RcftRemoteIIEthFxPortTxPowerAbnormal_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,5),_RcftRemoteIIEthFxPortTxPowerAbnormal_Type())
rcftRemoteIIEthFxPortTxPowerAbnormal.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortTxPowerAbnormal.setStatus(_A)
class _RcftRemoteIIEthFxPortRxSensitiveAbnormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_T,2)))
_RcftRemoteIIEthFxPortRxSensitiveAbnormal_Type.__name__=_C
_RcftRemoteIIEthFxPortRxSensitiveAbnormal_Object=MibTableColumn
rcftRemoteIIEthFxPortRxSensitiveAbnormal=_RcftRemoteIIEthFxPortRxSensitiveAbnormal_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,6),_RcftRemoteIIEthFxPortRxSensitiveAbnormal_Type())
rcftRemoteIIEthFxPortRxSensitiveAbnormal.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortRxSensitiveAbnormal.setStatus(_A)
class _RcftRemoteIIEthFxPortLaserAbnormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_T,2)))
_RcftRemoteIIEthFxPortLaserAbnormal_Type.__name__=_C
_RcftRemoteIIEthFxPortLaserAbnormal_Object=MibTableColumn
rcftRemoteIIEthFxPortLaserAbnormal=_RcftRemoteIIEthFxPortLaserAbnormal_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,7),_RcftRemoteIIEthFxPortLaserAbnormal_Type())
rcftRemoteIIEthFxPortLaserAbnormal.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortLaserAbnormal.setStatus(_A)
class _RcftRemoteIIEthFxPortModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,100)));namedValues=NamedValues(*(('optical-M',1),('optical-S1',2),('optical-S2',3),('optical-S3',4),('optical-SS13',5),('optical-SS15',6),('optical-SS23',7),('optical-SS25',8),('optical-SS34',9),('optical-SS35',10),('unknown-type',100)))
_RcftRemoteIIEthFxPortModuleType_Type.__name__=_C
_RcftRemoteIIEthFxPortModuleType_Object=MibTableColumn
rcftRemoteIIEthFxPortModuleType=_RcftRemoteIIEthFxPortModuleType_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,8),_RcftRemoteIIEthFxPortModuleType_Type())
rcftRemoteIIEthFxPortModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortModuleType.setStatus(_A)
class _RcftRemoteIIEthFxPortFaultPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcftRemoteIIEthFxPortFaultPass_Type.__name__=_C
_RcftRemoteIIEthFxPortFaultPass_Object=MibTableColumn
rcftRemoteIIEthFxPortFaultPass=_RcftRemoteIIEthFxPortFaultPass_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,9),_RcftRemoteIIEthFxPortFaultPass_Type())
rcftRemoteIIEthFxPortFaultPass.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortFaultPass.setStatus(_A)
class _RcftRemoteIIEthFxPortLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_RcftRemoteIIEthFxPortLink_Type.__name__=_C
_RcftRemoteIIEthFxPortLink_Object=MibTableColumn
rcftRemoteIIEthFxPortLink=_RcftRemoteIIEthFxPortLink_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,10),_RcftRemoteIIEthFxPortLink_Type())
rcftRemoteIIEthFxPortLink.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortLink.setStatus(_A)
class _RcftRemoteIIEthFxRxToTxFaultPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcftRemoteIIEthFxRxToTxFaultPass_Type.__name__=_C
_RcftRemoteIIEthFxRxToTxFaultPass_Object=MibTableColumn
rcftRemoteIIEthFxRxToTxFaultPass=_RcftRemoteIIEthFxRxToTxFaultPass_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,11),_RcftRemoteIIEthFxRxToTxFaultPass_Type())
rcftRemoteIIEthFxRxToTxFaultPass.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFxRxToTxFaultPass.setStatus(_A)
class _RcftRemoteIIEthFxTxDisabledByFR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_RcftRemoteIIEthFxTxDisabledByFR_Type.__name__=_C
_RcftRemoteIIEthFxTxDisabledByFR_Object=MibTableColumn
rcftRemoteIIEthFxTxDisabledByFR=_RcftRemoteIIEthFxTxDisabledByFR_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,12),_RcftRemoteIIEthFxTxDisabledByFR_Type())
rcftRemoteIIEthFxTxDisabledByFR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxTxDisabledByFR.setStatus(_A)
class _RcftRemoteIIEthFxShutDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),('closeByFP',3),('closeByALS',4),('closeByLP',5)))
_RcftRemoteIIEthFxShutDown_Type.__name__=_C
_RcftRemoteIIEthFxShutDown_Object=MibTableColumn
rcftRemoteIIEthFxShutDown=_RcftRemoteIIEthFxShutDown_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,13),_RcftRemoteIIEthFxShutDown_Type())
rcftRemoteIIEthFxShutDown.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFxShutDown.setStatus(_A)
class _RcftRemoteIIEthFxPortAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manul',2)))
_RcftRemoteIIEthFxPortAutoNegotiation_Type.__name__=_C
_RcftRemoteIIEthFxPortAutoNegotiation_Object=MibTableColumn
rcftRemoteIIEthFxPortAutoNegotiation=_RcftRemoteIIEthFxPortAutoNegotiation_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,14),_RcftRemoteIIEthFxPortAutoNegotiation_Type())
rcftRemoteIIEthFxPortAutoNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortAutoNegotiation.setStatus(_A)
class _RcftRemoteIIEthFxPortOptHeadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sfpType',1),(_J,2)))
_RcftRemoteIIEthFxPortOptHeadType_Type.__name__=_C
_RcftRemoteIIEthFxPortOptHeadType_Object=MibTableColumn
rcftRemoteIIEthFxPortOptHeadType=_RcftRemoteIIEthFxPortOptHeadType_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,15),_RcftRemoteIIEthFxPortOptHeadType_Type())
rcftRemoteIIEthFxPortOptHeadType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortOptHeadType.setStatus(_A)
class _RcftRemoteIIEthFxSfpRXLOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('alarm',2)))
_RcftRemoteIIEthFxSfpRXLOS_Type.__name__=_C
_RcftRemoteIIEthFxSfpRXLOS_Object=MibTableColumn
rcftRemoteIIEthFxSfpRXLOS=_RcftRemoteIIEthFxSfpRXLOS_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,16),_RcftRemoteIIEthFxSfpRXLOS_Type())
rcftRemoteIIEthFxSfpRXLOS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpRXLOS.setStatus(_A)
class _RcftRemoteIIEthFxSfpTXDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcftRemoteIIEthFxSfpTXDisable_Type.__name__=_C
_RcftRemoteIIEthFxSfpTXDisable_Object=MibTableColumn
rcftRemoteIIEthFxSfpTXDisable=_RcftRemoteIIEthFxSfpTXDisable_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,17),_RcftRemoteIIEthFxSfpTXDisable_Type())
rcftRemoteIIEthFxSfpTXDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpTXDisable.setStatus(_A)
class _RcftRemoteIIEthFxSfpExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exist',1),('notExist',2)))
_RcftRemoteIIEthFxSfpExist_Type.__name__=_C
_RcftRemoteIIEthFxSfpExist_Object=MibTableColumn
rcftRemoteIIEthFxSfpExist=_RcftRemoteIIEthFxSfpExist_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,18),_RcftRemoteIIEthFxSfpExist_Type())
rcftRemoteIIEthFxSfpExist.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpExist.setStatus(_A)
class _RcftRemoteIIEthFxSfpSpeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),('speed155M',2),('speed622M',3),('speed1250M',4),('speed2500M',5)))
_RcftRemoteIIEthFxSfpSpeedStatus_Type.__name__=_C
_RcftRemoteIIEthFxSfpSpeedStatus_Object=MibTableColumn
rcftRemoteIIEthFxSfpSpeedStatus=_RcftRemoteIIEthFxSfpSpeedStatus_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,19),_RcftRemoteIIEthFxSfpSpeedStatus_Type())
rcftRemoteIIEthFxSfpSpeedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpSpeedStatus.setStatus(_A)
_RcftRemoteIIEthFxSfpTransportDistance_Type=Integer32
_RcftRemoteIIEthFxSfpTransportDistance_Object=MibTableColumn
rcftRemoteIIEthFxSfpTransportDistance=_RcftRemoteIIEthFxSfpTransportDistance_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,20),_RcftRemoteIIEthFxSfpTransportDistance_Type())
rcftRemoteIIEthFxSfpTransportDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpTransportDistance.setStatus(_A)
_RcftRemoteIIEthFxSfpWaveLength_Type=Integer32
_RcftRemoteIIEthFxSfpWaveLength_Object=MibTableColumn
rcftRemoteIIEthFxSfpWaveLength=_RcftRemoteIIEthFxSfpWaveLength_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,21),_RcftRemoteIIEthFxSfpWaveLength_Type())
rcftRemoteIIEthFxSfpWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpWaveLength.setStatus(_A)
class _RcftRemoteIIEthFxSfpManufactory_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RcftRemoteIIEthFxSfpManufactory_Type.__name__=_K
_RcftRemoteIIEthFxSfpManufactory_Object=MibTableColumn
rcftRemoteIIEthFxSfpManufactory=_RcftRemoteIIEthFxSfpManufactory_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,22),_RcftRemoteIIEthFxSfpManufactory_Type())
rcftRemoteIIEthFxSfpManufactory.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpManufactory.setStatus(_A)
class _RcftRemoteIIEthFxSfpProductType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RcftRemoteIIEthFxSfpProductType_Type.__name__=_K
_RcftRemoteIIEthFxSfpProductType_Object=MibTableColumn
rcftRemoteIIEthFxSfpProductType=_RcftRemoteIIEthFxSfpProductType_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,23),_RcftRemoteIIEthFxSfpProductType_Type())
rcftRemoteIIEthFxSfpProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpProductType.setStatus(_A)
class _RcftRemoteIIEthFxSfpVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_RcftRemoteIIEthFxSfpVersion_Type.__name__=_K
_RcftRemoteIIEthFxSfpVersion_Object=MibTableColumn
rcftRemoteIIEthFxSfpVersion=_RcftRemoteIIEthFxSfpVersion_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,24),_RcftRemoteIIEthFxSfpVersion_Type())
rcftRemoteIIEthFxSfpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpVersion.setStatus(_A)
class _RcftRemoteIIEthFxSfpWaterMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RcftRemoteIIEthFxSfpWaterMask_Type.__name__=_K
_RcftRemoteIIEthFxSfpWaterMask_Object=MibTableColumn
rcftRemoteIIEthFxSfpWaterMask=_RcftRemoteIIEthFxSfpWaterMask_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,25),_RcftRemoteIIEthFxSfpWaterMask_Type())
rcftRemoteIIEthFxSfpWaterMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpWaterMask.setStatus(_A)
class _RcftRemoteIIEthFxSfpMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),('fiber9u125u',2),('fiber50u125u',3),('fiber625u125u',4),('copper',5)))
_RcftRemoteIIEthFxSfpMediaType_Type.__name__=_C
_RcftRemoteIIEthFxSfpMediaType_Object=MibTableColumn
rcftRemoteIIEthFxSfpMediaType=_RcftRemoteIIEthFxSfpMediaType_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,26),_RcftRemoteIIEthFxSfpMediaType_Type())
rcftRemoteIIEthFxSfpMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpMediaType.setStatus(_A)
class _RcftRemoteIIEthFxSfpModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('gbic',2),('sff',3),('sfp',4)))
_RcftRemoteIIEthFxSfpModuleType_Type.__name__=_C
_RcftRemoteIIEthFxSfpModuleType_Object=MibTableColumn
rcftRemoteIIEthFxSfpModuleType=_RcftRemoteIIEthFxSfpModuleType_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,27),_RcftRemoteIIEthFxSfpModuleType_Type())
rcftRemoteIIEthFxSfpModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpModuleType.setStatus(_A)
class _RcftRemoteIIEthFxSfpOpticalInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('sc',2),('lc',3),('rj45',4)))
_RcftRemoteIIEthFxSfpOpticalInterface_Type.__name__=_C
_RcftRemoteIIEthFxSfpOpticalInterface_Object=MibTableColumn
rcftRemoteIIEthFxSfpOpticalInterface=_RcftRemoteIIEthFxSfpOpticalInterface_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,28),_RcftRemoteIIEthFxSfpOpticalInterface_Type())
rcftRemoteIIEthFxSfpOpticalInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxSfpOpticalInterface.setStatus(_A)
class _RcftRemoteIIEthFxUntag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('untag',1),('tag',2)))
_RcftRemoteIIEthFxUntag_Type.__name__=_C
_RcftRemoteIIEthFxUntag_Object=MibTableColumn
rcftRemoteIIEthFxUntag=_RcftRemoteIIEthFxUntag_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,29),_RcftRemoteIIEthFxUntag_Type())
rcftRemoteIIEthFxUntag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFxUntag.setStatus(_A)
_RcftRemoteIIEthFxPVID_Type=Integer32
_RcftRemoteIIEthFxPVID_Object=MibTableColumn
rcftRemoteIIEthFxPVID=_RcftRemoteIIEthFxPVID_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,1,1,30),_RcftRemoteIIEthFxPVID_Type())
rcftRemoteIIEthFxPVID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIEthFxPVID.setStatus(_A)
_RcftRemoteIIEthFxStatisticTable_Object=MibTable
rcftRemoteIIEthFxStatisticTable=_RcftRemoteIIEthFxStatisticTable_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,2))
if mibBuilder.loadTexts:rcftRemoteIIEthFxStatisticTable.setStatus(_A)
_RcftRemoteIIEthFxStatisticEntry_Object=MibTableRow
rcftRemoteIIEthFxStatisticEntry=_RcftRemoteIIEthFxStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,2,1))
if mibBuilder.loadTexts:rcftRemoteIIEthFxStatisticEntry.setStatus(_A)
_RcftRemoteIIEthFxTxPackets_Type=Counter32
_RcftRemoteIIEthFxTxPackets_Object=MibTableColumn
rcftRemoteIIEthFxTxPackets=_RcftRemoteIIEthFxTxPackets_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,2,1,1),_RcftRemoteIIEthFxTxPackets_Type())
rcftRemoteIIEthFxTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxTxPackets.setStatus(_A)
_RcftRemoteIIEthFxTxBytes_Type=Counter32
_RcftRemoteIIEthFxTxBytes_Object=MibTableColumn
rcftRemoteIIEthFxTxBytes=_RcftRemoteIIEthFxTxBytes_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,2,1,2),_RcftRemoteIIEthFxTxBytes_Type())
rcftRemoteIIEthFxTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxTxBytes.setStatus(_A)
_RcftRemoteIIEthFxRxPackets_Type=Counter32
_RcftRemoteIIEthFxRxPackets_Object=MibTableColumn
rcftRemoteIIEthFxRxPackets=_RcftRemoteIIEthFxRxPackets_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,2,1,3),_RcftRemoteIIEthFxRxPackets_Type())
rcftRemoteIIEthFxRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxRxPackets.setStatus(_A)
_RcftRemoteIIEthFxRxBytes_Type=Counter32
_RcftRemoteIIEthFxRxBytes_Object=MibTableColumn
rcftRemoteIIEthFxRxBytes=_RcftRemoteIIEthFxRxBytes_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,2,1,4),_RcftRemoteIIEthFxRxBytes_Type())
rcftRemoteIIEthFxRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxRxBytes.setStatus(_A)
_RcftRemoteIIEthFxRxLostPackets_Type=Counter32
_RcftRemoteIIEthFxRxLostPackets_Object=MibTableColumn
rcftRemoteIIEthFxRxLostPackets=_RcftRemoteIIEthFxRxLostPackets_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,2,1,5),_RcftRemoteIIEthFxRxLostPackets_Type())
rcftRemoteIIEthFxRxLostPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxRxLostPackets.setStatus(_A)
_RcftRemoteIIEthFxFluxTimer_Type=Counter32
_RcftRemoteIIEthFxFluxTimer_Object=MibTableColumn
rcftRemoteIIEthFxFluxTimer=_RcftRemoteIIEthFxFluxTimer_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,2,1,6),_RcftRemoteIIEthFxFluxTimer_Type())
rcftRemoteIIEthFxFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxFluxTimer.setStatus(_A)
_RcftRemoteIIEthFxTxLostPackets_Type=Counter32
_RcftRemoteIIEthFxTxLostPackets_Object=MibTableColumn
rcftRemoteIIEthFxTxLostPackets=_RcftRemoteIIEthFxTxLostPackets_Object((1,3,6,1,4,1,8886,2,1,7,2,2,1,2,1,7),_RcftRemoteIIEthFxTxLostPackets_Type())
rcftRemoteIIEthFxTxLostPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIEthFxTxLostPackets.setStatus(_A)
_RcftRemoteIIDeviceEthFxTraps_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceEthFxTraps=_RcftRemoteIIDeviceEthFxTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,2,2,2))
_RcftRemoteIIDeviceVLANMIB_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceVLANMIB=_RcftRemoteIIDeviceVLANMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,3))
_RcftRemoteIIDeviceVLANObjects_ObjectIdentity=ObjectIdentity
rcftRemoteIIDeviceVLANObjects=_RcftRemoteIIDeviceVLANObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,7,3,1))
_RcftRemoteIIDeviceVLANTable_Object=MibTable
rcftRemoteIIDeviceVLANTable=_RcftRemoteIIDeviceVLANTable_Object((1,3,6,1,4,1,8886,2,1,7,3,1,1))
if mibBuilder.loadTexts:rcftRemoteIIDeviceVLANTable.setStatus(_A)
_RcftRemoteIIDeviceVLANEntry_Object=MibTableRow
rcftRemoteIIDeviceVLANEntry=_RcftRemoteIIDeviceVLANEntry_Object((1,3,6,1,4,1,8886,2,1,7,3,1,1,1))
rcftRemoteIIDeviceVLANEntry.setIndexNames((0,_F,_G),(0,_F,_H),(0,_E,_I),(0,_E,_c))
if mibBuilder.loadTexts:rcftRemoteIIDeviceVLANEntry.setStatus(_A)
_RcftRemoteIIVLANIndex_Type=Integer32
_RcftRemoteIIVLANIndex_Object=MibTableColumn
rcftRemoteIIVLANIndex=_RcftRemoteIIVLANIndex_Object((1,3,6,1,4,1,8886,2,1,7,3,1,1,1,1),_RcftRemoteIIVLANIndex_Type())
rcftRemoteIIVLANIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteIIVLANIndex.setStatus(_A)
_RcftRemoteIIVLANStatus_Type=Integer32
_RcftRemoteIIVLANStatus_Object=MibTableColumn
rcftRemoteIIVLANStatus=_RcftRemoteIIVLANStatus_Object((1,3,6,1,4,1,8886,2,1,7,3,1,1,1,2),_RcftRemoteIIVLANStatus_Type())
rcftRemoteIIVLANStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIVLANStatus.setStatus(_A)
_RcftRemoteIIVLANmember_Type=Integer32
_RcftRemoteIIVLANmember_Object=MibTableColumn
rcftRemoteIIVLANmember=_RcftRemoteIIVLANmember_Object((1,3,6,1,4,1,8886,2,1,7,3,1,1,1,3),_RcftRemoteIIVLANmember_Type())
rcftRemoteIIVLANmember.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIVLANmember.setStatus(_A)
_RcftRemoteIIVID_Type=Integer32
_RcftRemoteIIVID_Object=MibTableColumn
rcftRemoteIIVID=_RcftRemoteIIVID_Object((1,3,6,1,4,1,8886,2,1,7,3,1,1,1,4),_RcftRemoteIIVID_Type())
rcftRemoteIIVID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteIIVID.setStatus(_A)
rcftRemoteIIEthFePortEntry.registerAugmentions((_E,_d))
rcftRemoteIIEthFeStatisticEntry.setIndexNames(*rcftRemoteIIEthFePortEntry.getIndexNames())
rcftRemoteIIEthFxPortEntry.registerAugmentions((_E,_e))
rcftRemoteIIEthFxStatisticEntry.setIndexNames(*rcftRemoteIIEthFxPortEntry.getIndexNames())
rcftRemoteIIDevExistTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,1,2,1))
rcftRemoteIIDevExistTrap.setObjects((_E,_f))
if mibBuilder.loadTexts:rcftRemoteIIDevExistTrap.setStatus(_A)
rcftRemoteIIDevVoltTooHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,1,2,2))
rcftRemoteIIDevVoltTooHighTrap.setObjects((_E,_U))
if mibBuilder.loadTexts:rcftRemoteIIDevVoltTooHighTrap.setStatus(_A)
rcftRemoteIIDevVoltTooLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,1,2,3))
rcftRemoteIIDevVoltTooLowTrap.setObjects((_E,_U))
if mibBuilder.loadTexts:rcftRemoteIIDevVoltTooLowTrap.setStatus(_A)
rcftRemoteIIDevTmptTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,1,2,4))
rcftRemoteIIDevTmptTrap.setObjects((_E,_g))
if mibBuilder.loadTexts:rcftRemoteIIDevTmptTrap.setStatus(_A)
rcftRemoteIIEthFeLinkTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,2,1,2,1))
rcftRemoteIIEthFeLinkTrap.setObjects((_E,_h))
if mibBuilder.loadTexts:rcftRemoteIIEthFeLinkTrap.setStatus(_A)
rcftRemoteIIEthFxPortRLKTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,2,2,2,1))
rcftRemoteIIEthFxPortRLKTrap.setObjects((_E,_i))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortRLKTrap.setStatus(_A)
rcftRemoteIIEthFxPortTLKTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,2,2,2,2))
rcftRemoteIIEthFxPortTLKTrap.setObjects((_E,_j))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortTLKTrap.setStatus(_A)
rcftRemoteIIEthFxPortTxPowerTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,2,2,2,3))
rcftRemoteIIEthFxPortTxPowerTrap.setObjects((_E,_k))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortTxPowerTrap.setStatus(_A)
rcftRemoteIIEthFxPortRxSensitiveTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,2,2,2,4))
rcftRemoteIIEthFxPortRxSensitiveTrap.setObjects((_E,_l))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortRxSensitiveTrap.setStatus(_A)
rcftRemoteIIEthFxPortLaserTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,2,2,2,5))
rcftRemoteIIEthFxPortLaserTrap.setObjects((_E,_m))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortLaserTrap.setStatus(_A)
rcftRemoteIIEthFxPortSDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,2,2,2,6))
rcftRemoteIIEthFxPortSDTrap.setObjects((_E,_n))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortSDTrap.setStatus(_A)
rcftRemoteIIEthFxPortLinkTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,2,2,2,7))
rcftRemoteIIEthFxPortLinkTrap.setObjects((_E,_o))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortLinkTrap.setStatus(_A)
rcftRemoteIIEthFxPortSfpRXLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,2,2,2,8))
rcftRemoteIIEthFxPortSfpRXLOSTrap.setObjects((_E,_p))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortSfpRXLOSTrap.setStatus(_A)
rcftRemoteIIEthFxPortSfpExistTrap=NotificationType((1,3,6,1,4,1,8886,2,1,7,2,2,2,9))
rcftRemoteIIEthFxPortSfpExistTrap.setObjects((_E,_q))
if mibBuilder.loadTexts:rcftRemoteIIEthFxPortSfpExistTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rcftRemoteIIDeviceMib':rcftRemoteIIDeviceMib,'rcftRemoteIIDeviceSystemMIB':rcftRemoteIIDeviceSystemMIB,'rcftRemoteIIDeviceSysObjects':rcftRemoteIIDeviceSysObjects,'rcftRemoteIIDeviceSysTable':rcftRemoteIIDeviceSysTable,'rcftRemoteIIDeviceSysEntry':rcftRemoteIIDeviceSysEntry,_I:rcftRemoteIIDeviceIndex,_f:rcftRemoteIIDeviceExist,'rcftRemoteIIDeviceType':rcftRemoteIIDeviceType,'rcftRemoteIIDeviceToRDeviceID':rcftRemoteIIDeviceToRDeviceID,'rcftRemoteIIDeviceToRPortType':rcftRemoteIIDeviceToRPortType,'rcftRemoteIIDeviceToRPortIndex':rcftRemoteIIDeviceToRPortIndex,'rcftRemoteIIDeviceVersionInfo':rcftRemoteIIDeviceVersionInfo,_g:rcftRemoteIISysTemperature,_U:rcftRemoteIISysVoltageStatus,'rcftRemoteIIDeviceFrameLen':rcftRemoteIIDeviceFrameLen,'rcftRemoteIIDeviceOrder':rcftRemoteIIDeviceOrder,'rcftRemoteIIDeviceConfigFlag':rcftRemoteIIDeviceConfigFlag,'rcftRemoteIIDeviceStatus':rcftRemoteIIDeviceStatus,'rcftRemoteIIDeviceVenderCode':rcftRemoteIIDeviceVenderCode,'rcftRemoteIIDeviceModelID':rcftRemoteIIDeviceModelID,'rcftRemoteIIDeviceLoopBackStatus':rcftRemoteIIDeviceLoopBackStatus,'rcftRemoteIIDeviceLoopBackMode':rcftRemoteIIDeviceLoopBackMode,'rcftRemoteIIDeviceVLANType':rcftRemoteIIDeviceVLANType,'rcftRemoteIIQosEnable':rcftRemoteIIQosEnable,'rcftRemoteIIBaseCOS':rcftRemoteIIBaseCOS,'rcftRemoteIIQueuesPolicy':rcftRemoteIIQueuesPolicy,'rcftRemoteIIDeviceQoSPolicy':rcftRemoteIIDeviceQoSPolicy,'rcftRemoteIIDeviceMibUse':rcftRemoteIIDeviceMibUse,'rcftRemoteIIDeviceConfigFlagTable':rcftRemoteIIDeviceConfigFlagTable,'rcftRemoteIIDeviceConfigFlagEntry':rcftRemoteIIDeviceConfigFlagEntry,'rcftRemoteIIDeviceConfigFinishFlag':rcftRemoteIIDeviceConfigFinishFlag,'rcftRemoteIIDeviceSysTraps':rcftRemoteIIDeviceSysTraps,'rcftRemoteIIDevExistTrap':rcftRemoteIIDevExistTrap,'rcftRemoteIIDevVoltTooHighTrap':rcftRemoteIIDevVoltTooHighTrap,'rcftRemoteIIDevVoltTooLowTrap':rcftRemoteIIDevVoltTooLowTrap,'rcftRemoteIIDevTmptTrap':rcftRemoteIIDevTmptTrap,'rcftRemoteIIDeviceEthMIB':rcftRemoteIIDeviceEthMIB,'rcftRemoteIIDeviceEthFeMIB':rcftRemoteIIDeviceEthFeMIB,'rcftRemoteIIDeviceEthFeObjects':rcftRemoteIIDeviceEthFeObjects,'rcftRemoteIIEthFePortTable':rcftRemoteIIEthFePortTable,'rcftRemoteIIEthFePortEntry':rcftRemoteIIEthFePortEntry,_Q:rcftRemoteIIEthFeIndex,_h:rcftRemoteIIEthFeLinkStatus,'rcftRemoteIIEthFeShutDown':rcftRemoteIIEthFeShutDown,'rcftRemoteIIEthFeAutoNegotiation':rcftRemoteIIEthFeAutoNegotiation,'rcftRemoteIIEthFeSpeed':rcftRemoteIIEthFeSpeed,'rcftRemoteIIEthFeDuplex':rcftRemoteIIEthFeDuplex,'rcftRemoteIIEthFeRestrictSpeed':rcftRemoteIIEthFeRestrictSpeed,'rcftRemoteIIEthFeFaultPass':rcftRemoteIIEthFeFaultPass,'rcftRemoteIIEthFeDisabledByRemoteTP':rcftRemoteIIEthFeDisabledByRemoteTP,'rcftRemoteIIEthFeDisabledByFxToFeFP':rcftRemoteIIEthFeDisabledByFxToFeFP,'rcftRemoteIIEthFeTxRestrictSpeed':rcftRemoteIIEthFeTxRestrictSpeed,'rcftRemoteIIEthFeTag':rcftRemoteIIEthFeTag,'rcftRemoteIIEthFePVID':rcftRemoteIIEthFePVID,'rcftRemoteIIEthFeQoSPolicy':rcftRemoteIIEthFeQoSPolicy,'rcftRemoteIIEthFeStatisticTable':rcftRemoteIIEthFeStatisticTable,_d:rcftRemoteIIEthFeStatisticEntry,'rcftRemoteIIEthFeTxPackets':rcftRemoteIIEthFeTxPackets,'rcftRemoteIIEthFeTxBytes':rcftRemoteIIEthFeTxBytes,'rcftRemoteIIEthFeRxPackets':rcftRemoteIIEthFeRxPackets,'rcftRemoteIIEthFeRxBytes':rcftRemoteIIEthFeRxBytes,'rcftRemoteIIEthFeRxLostPackets':rcftRemoteIIEthFeRxLostPackets,'rcftRemoteIIEthFeFluxTimer':rcftRemoteIIEthFeFluxTimer,'rcftRemoteIIEthFeTxLostPackets':rcftRemoteIIEthFeTxLostPackets,'rcftRemoteIIEthFePortConfTable':rcftRemoteIIEthFePortConfTable,'rcftRemoteIIEthFePortConfEntry':rcftRemoteIIEthFePortConfEntry,'rcftRemoteIIEthFeConfSpeed':rcftRemoteIIEthFeConfSpeed,'rcftRemoteIIEthFeConfDuplex':rcftRemoteIIEthFeConfDuplex,'rcftRemoteIIDeviceEthFeTraps':rcftRemoteIIDeviceEthFeTraps,'rcftRemoteIIEthFeLinkTrap':rcftRemoteIIEthFeLinkTrap,'rcftRemoteIIDeviceEthFxMIB':rcftRemoteIIDeviceEthFxMIB,'rcftRemoteIIDeviceEthFxObjects':rcftRemoteIIDeviceEthFxObjects,'rcftRemoteIIEthFxPortTable':rcftRemoteIIEthFxPortTable,'rcftRemoteIIEthFxPortEntry':rcftRemoteIIEthFxPortEntry,_b:rcftRemoteIIEthFxIndex,_i:rcftRemoteIIEthFxPortRLK,_j:rcftRemoteIIEthFxPortTLK,_n:rcftRemoteIIEthFxPortSD,_k:rcftRemoteIIEthFxPortTxPowerAbnormal,_l:rcftRemoteIIEthFxPortRxSensitiveAbnormal,_m:rcftRemoteIIEthFxPortLaserAbnormal,'rcftRemoteIIEthFxPortModuleType':rcftRemoteIIEthFxPortModuleType,'rcftRemoteIIEthFxPortFaultPass':rcftRemoteIIEthFxPortFaultPass,_o:rcftRemoteIIEthFxPortLink,'rcftRemoteIIEthFxRxToTxFaultPass':rcftRemoteIIEthFxRxToTxFaultPass,'rcftRemoteIIEthFxTxDisabledByFR':rcftRemoteIIEthFxTxDisabledByFR,'rcftRemoteIIEthFxShutDown':rcftRemoteIIEthFxShutDown,'rcftRemoteIIEthFxPortAutoNegotiation':rcftRemoteIIEthFxPortAutoNegotiation,'rcftRemoteIIEthFxPortOptHeadType':rcftRemoteIIEthFxPortOptHeadType,_p:rcftRemoteIIEthFxSfpRXLOS,'rcftRemoteIIEthFxSfpTXDisable':rcftRemoteIIEthFxSfpTXDisable,_q:rcftRemoteIIEthFxSfpExist,'rcftRemoteIIEthFxSfpSpeedStatus':rcftRemoteIIEthFxSfpSpeedStatus,'rcftRemoteIIEthFxSfpTransportDistance':rcftRemoteIIEthFxSfpTransportDistance,'rcftRemoteIIEthFxSfpWaveLength':rcftRemoteIIEthFxSfpWaveLength,'rcftRemoteIIEthFxSfpManufactory':rcftRemoteIIEthFxSfpManufactory,'rcftRemoteIIEthFxSfpProductType':rcftRemoteIIEthFxSfpProductType,'rcftRemoteIIEthFxSfpVersion':rcftRemoteIIEthFxSfpVersion,'rcftRemoteIIEthFxSfpWaterMask':rcftRemoteIIEthFxSfpWaterMask,'rcftRemoteIIEthFxSfpMediaType':rcftRemoteIIEthFxSfpMediaType,'rcftRemoteIIEthFxSfpModuleType':rcftRemoteIIEthFxSfpModuleType,'rcftRemoteIIEthFxSfpOpticalInterface':rcftRemoteIIEthFxSfpOpticalInterface,'rcftRemoteIIEthFxUntag':rcftRemoteIIEthFxUntag,'rcftRemoteIIEthFxPVID':rcftRemoteIIEthFxPVID,'rcftRemoteIIEthFxStatisticTable':rcftRemoteIIEthFxStatisticTable,_e:rcftRemoteIIEthFxStatisticEntry,'rcftRemoteIIEthFxTxPackets':rcftRemoteIIEthFxTxPackets,'rcftRemoteIIEthFxTxBytes':rcftRemoteIIEthFxTxBytes,'rcftRemoteIIEthFxRxPackets':rcftRemoteIIEthFxRxPackets,'rcftRemoteIIEthFxRxBytes':rcftRemoteIIEthFxRxBytes,'rcftRemoteIIEthFxRxLostPackets':rcftRemoteIIEthFxRxLostPackets,'rcftRemoteIIEthFxFluxTimer':rcftRemoteIIEthFxFluxTimer,'rcftRemoteIIEthFxTxLostPackets':rcftRemoteIIEthFxTxLostPackets,'rcftRemoteIIDeviceEthFxTraps':rcftRemoteIIDeviceEthFxTraps,'rcftRemoteIIEthFxPortRLKTrap':rcftRemoteIIEthFxPortRLKTrap,'rcftRemoteIIEthFxPortTLKTrap':rcftRemoteIIEthFxPortTLKTrap,'rcftRemoteIIEthFxPortTxPowerTrap':rcftRemoteIIEthFxPortTxPowerTrap,'rcftRemoteIIEthFxPortRxSensitiveTrap':rcftRemoteIIEthFxPortRxSensitiveTrap,'rcftRemoteIIEthFxPortLaserTrap':rcftRemoteIIEthFxPortLaserTrap,'rcftRemoteIIEthFxPortSDTrap':rcftRemoteIIEthFxPortSDTrap,'rcftRemoteIIEthFxPortLinkTrap':rcftRemoteIIEthFxPortLinkTrap,'rcftRemoteIIEthFxPortSfpRXLOSTrap':rcftRemoteIIEthFxPortSfpRXLOSTrap,'rcftRemoteIIEthFxPortSfpExistTrap':rcftRemoteIIEthFxPortSfpExistTrap,'rcftRemoteIIDeviceVLANMIB':rcftRemoteIIDeviceVLANMIB,'rcftRemoteIIDeviceVLANObjects':rcftRemoteIIDeviceVLANObjects,'rcftRemoteIIDeviceVLANTable':rcftRemoteIIDeviceVLANTable,'rcftRemoteIIDeviceVLANEntry':rcftRemoteIIDeviceVLANEntry,_c:rcftRemoteIIVLANIndex,'rcftRemoteIIVLANStatus':rcftRemoteIIVLANStatus,'rcftRemoteIIVLANmember':rcftRemoteIIVLANmember,'rcftRemoteIIVID':rcftRemoteIIVID})