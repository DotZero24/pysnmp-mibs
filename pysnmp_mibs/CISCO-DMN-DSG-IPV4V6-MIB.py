_J='ethBackupStatusIndex'
_I='ethBackupIndex'
_H='ipConfigPortIdKey'
_G='macInfoMacIndex'
_F='CISCO-DMN-DSG-IPV4V6-MIB'
_E='read-write'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
ciscoDSGIPv4v6=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,25))
if mibBuilder.loadTexts:ciscoDSGIPv4v6.setRevisions(('2012-03-20 11:00','2010-08-30 11:00','2010-04-30 05:00','2010-04-12 05:00','2010-03-22 05:00','2009-12-20 12:00'))
_IpV4v6Table_ObjectIdentity=ObjectIdentity
ipV4v6Table=_IpV4v6Table_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,25,2))
_MacInfoTable_Object=MibTable
macInfoTable=_MacInfoTable_Object((1,3,6,1,4,1,1429,2,2,5,25,2,1))
if mibBuilder.loadTexts:macInfoTable.setStatus(_A)
_MacInfoEntry_Object=MibTableRow
macInfoEntry=_MacInfoEntry_Object((1,3,6,1,4,1,1429,2,2,5,25,2,1,1))
macInfoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:macInfoEntry.setStatus(_A)
class _MacInfoMacIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_MacInfoMacIndex_Type.__name__=_C
_MacInfoMacIndex_Object=MibTableColumn
macInfoMacIndex=_MacInfoMacIndex_Object((1,3,6,1,4,1,1429,2,2,5,25,2,1,1,1),_MacInfoMacIndex_Type())
macInfoMacIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:macInfoMacIndex.setStatus(_A)
class _MacInfoMacAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_MacInfoMacAddr_Type.__name__=_D
_MacInfoMacAddr_Object=MibTableColumn
macInfoMacAddr=_MacInfoMacAddr_Object((1,3,6,1,4,1,1429,2,2,5,25,2,1,1,2),_MacInfoMacAddr_Type())
macInfoMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:macInfoMacAddr.setStatus(_A)
_IpConfigTable_Object=MibTable
ipConfigTable=_IpConfigTable_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2))
if mibBuilder.loadTexts:ipConfigTable.setStatus(_A)
_IpConfigEntry_Object=MibTableRow
ipConfigEntry=_IpConfigEntry_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1))
ipConfigEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:ipConfigEntry.setStatus(_A)
class _IpConfigPortIdKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_IpConfigPortIdKey_Type.__name__=_C
_IpConfigPortIdKey_Object=MibTableColumn
ipConfigPortIdKey=_IpConfigPortIdKey_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,1),_IpConfigPortIdKey_Type())
ipConfigPortIdKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ipConfigPortIdKey.setStatus(_A)
class _IpConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_IpConfigName_Type.__name__=_D
_IpConfigName_Object=MibTableColumn
ipConfigName=_IpConfigName_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,2),_IpConfigName_Type())
ipConfigName.setMaxAccess(_E)
if mibBuilder.loadTexts:ipConfigName.setStatus(_A)
_IpConfigCurIPAddressV4_Type=IpAddress
_IpConfigCurIPAddressV4_Object=MibTableColumn
ipConfigCurIPAddressV4=_IpConfigCurIPAddressV4_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,3),_IpConfigCurIPAddressV4_Type())
ipConfigCurIPAddressV4.setMaxAccess(_E)
if mibBuilder.loadTexts:ipConfigCurIPAddressV4.setStatus(_A)
class _IpConfigCurNetworkMaskV4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,30))
_IpConfigCurNetworkMaskV4_Type.__name__=_C
_IpConfigCurNetworkMaskV4_Object=MibTableColumn
ipConfigCurNetworkMaskV4=_IpConfigCurNetworkMaskV4_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,4),_IpConfigCurNetworkMaskV4_Type())
ipConfigCurNetworkMaskV4.setMaxAccess(_E)
if mibBuilder.loadTexts:ipConfigCurNetworkMaskV4.setStatus(_A)
_IpConfigCurDefaultGatewayV4_Type=IpAddress
_IpConfigCurDefaultGatewayV4_Object=MibTableColumn
ipConfigCurDefaultGatewayV4=_IpConfigCurDefaultGatewayV4_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,5),_IpConfigCurDefaultGatewayV4_Type())
ipConfigCurDefaultGatewayV4.setMaxAccess(_E)
if mibBuilder.loadTexts:ipConfigCurDefaultGatewayV4.setStatus(_A)
class _IpConfigV4V6Flag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipV4',1),('ipV6',2)))
_IpConfigV4V6Flag_Type.__name__=_C
_IpConfigV4V6Flag_Object=MibTableColumn
ipConfigV4V6Flag=_IpConfigV4V6Flag_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,6),_IpConfigV4V6Flag_Type())
ipConfigV4V6Flag.setMaxAccess(_B)
if mibBuilder.loadTexts:ipConfigV4V6Flag.setStatus(_A)
class _IpConfigPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('auto',1),('hd10',2),('fd10',3),('hd100',4),('fd100',5),('hd1000',6),('fd1000',7)))
_IpConfigPortMode_Type.__name__=_C
_IpConfigPortMode_Object=MibTableColumn
ipConfigPortMode=_IpConfigPortMode_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,7),_IpConfigPortMode_Type())
ipConfigPortMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ipConfigPortMode.setStatus(_A)
class _EthStatusLink_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EthStatusLink_Type.__name__=_D
_EthStatusLink_Object=MibTableColumn
ethStatusLink=_EthStatusLink_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,11),_EthStatusLink_Type())
ethStatusLink.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatusLink.setStatus(_A)
class _EthStatusSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EthStatusSpeed_Type.__name__=_D
_EthStatusSpeed_Object=MibTableColumn
ethStatusSpeed=_EthStatusSpeed_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,12),_EthStatusSpeed_Type())
ethStatusSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatusSpeed.setStatus(_A)
class _EthStatusDuplex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EthStatusDuplex_Type.__name__=_D
_EthStatusDuplex_Object=MibTableColumn
ethStatusDuplex=_EthStatusDuplex_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,13),_EthStatusDuplex_Type())
ethStatusDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatusDuplex.setStatus(_A)
class _EthStatusXover_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EthStatusXover_Type.__name__=_D
_EthStatusXover_Object=MibTableColumn
ethStatusXover=_EthStatusXover_Object((1,3,6,1,4,1,1429,2,2,5,25,2,2,1,14),_EthStatusXover_Type())
ethStatusXover.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatusXover.setStatus(_A)
_EthBackupTable_Object=MibTable
ethBackupTable=_EthBackupTable_Object((1,3,6,1,4,1,1429,2,2,5,25,2,3))
if mibBuilder.loadTexts:ethBackupTable.setStatus(_A)
_EthBackupEntry_Object=MibTableRow
ethBackupEntry=_EthBackupEntry_Object((1,3,6,1,4,1,1429,2,2,5,25,2,3,1))
ethBackupEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:ethBackupEntry.setStatus(_A)
class _EthBackupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_EthBackupIndex_Type.__name__=_C
_EthBackupIndex_Object=MibTableColumn
ethBackupIndex=_EthBackupIndex_Object((1,3,6,1,4,1,1429,2,2,5,25,2,3,1,1),_EthBackupIndex_Type())
ethBackupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethBackupIndex.setStatus(_A)
class _EthBackupMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('mirroring',1),('backupPrimaryData1',2),('backupPrimaryData2',3),('manualData1',4),('manualData2',5)))
_EthBackupMode_Type.__name__=_C
_EthBackupMode_Object=MibTableColumn
ethBackupMode=_EthBackupMode_Object((1,3,6,1,4,1,1429,2,2,5,25,2,3,1,2),_EthBackupMode_Type())
ethBackupMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ethBackupMode.setStatus(_A)
class _EthBackupDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonRevertive',1),('revertive',2)))
_EthBackupDirection_Type.__name__=_C
_EthBackupDirection_Object=MibTableColumn
ethBackupDirection=_EthBackupDirection_Object((1,3,6,1,4,1,1429,2,2,5,25,2,3,1,3),_EthBackupDirection_Type())
ethBackupDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:ethBackupDirection.setStatus(_A)
class _EthBackupDelayForward_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EthBackupDelayForward_Type.__name__=_C
_EthBackupDelayForward_Object=MibTableColumn
ethBackupDelayForward=_EthBackupDelayForward_Object((1,3,6,1,4,1,1429,2,2,5,25,2,3,1,4),_EthBackupDelayForward_Type())
ethBackupDelayForward.setMaxAccess(_E)
if mibBuilder.loadTexts:ethBackupDelayForward.setStatus(_A)
class _EthBackupDelayBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_EthBackupDelayBack_Type.__name__=_C
_EthBackupDelayBack_Object=MibTableColumn
ethBackupDelayBack=_EthBackupDelayBack_Object((1,3,6,1,4,1,1429,2,2,5,25,2,3,1,5),_EthBackupDelayBack_Type())
ethBackupDelayBack.setMaxAccess(_E)
if mibBuilder.loadTexts:ethBackupDelayBack.setStatus(_A)
_EthBackupStatusTable_Object=MibTable
ethBackupStatusTable=_EthBackupStatusTable_Object((1,3,6,1,4,1,1429,2,2,5,25,2,4))
if mibBuilder.loadTexts:ethBackupStatusTable.setStatus(_A)
_EthBackupStatusEntry_Object=MibTableRow
ethBackupStatusEntry=_EthBackupStatusEntry_Object((1,3,6,1,4,1,1429,2,2,5,25,2,4,1))
ethBackupStatusEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:ethBackupStatusEntry.setStatus(_A)
class _EthBackupStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_EthBackupStatusIndex_Type.__name__=_C
_EthBackupStatusIndex_Object=MibTableColumn
ethBackupStatusIndex=_EthBackupStatusIndex_Object((1,3,6,1,4,1,1429,2,2,5,25,2,4,1,1),_EthBackupStatusIndex_Type())
ethBackupStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethBackupStatusIndex.setStatus(_A)
class _EthBackupStatusPortsInUse_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EthBackupStatusPortsInUse_Type.__name__=_D
_EthBackupStatusPortsInUse_Object=MibTableColumn
ethBackupStatusPortsInUse=_EthBackupStatusPortsInUse_Object((1,3,6,1,4,1,1429,2,2,5,25,2,4,1,2),_EthBackupStatusPortsInUse_Type())
ethBackupStatusPortsInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:ethBackupStatusPortsInUse.setStatus(_A)
class _EthBackupStatusChangeReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EthBackupStatusChangeReason_Type.__name__=_D
_EthBackupStatusChangeReason_Object=MibTableColumn
ethBackupStatusChangeReason=_EthBackupStatusChangeReason_Object((1,3,6,1,4,1,1429,2,2,5,25,2,4,1,3),_EthBackupStatusChangeReason_Type())
ethBackupStatusChangeReason.setMaxAccess(_B)
if mibBuilder.loadTexts:ethBackupStatusChangeReason.setStatus(_A)
class _EthBackupStatusChangeDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_EthBackupStatusChangeDateTime_Type.__name__=_D
_EthBackupStatusChangeDateTime_Object=MibTableColumn
ethBackupStatusChangeDateTime=_EthBackupStatusChangeDateTime_Object((1,3,6,1,4,1,1429,2,2,5,25,2,4,1,4),_EthBackupStatusChangeDateTime_Type())
ethBackupStatusChangeDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ethBackupStatusChangeDateTime.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ciscoDSGIPv4v6':ciscoDSGIPv4v6,'ipV4v6Table':ipV4v6Table,'macInfoTable':macInfoTable,'macInfoEntry':macInfoEntry,_G:macInfoMacIndex,'macInfoMacAddr':macInfoMacAddr,'ipConfigTable':ipConfigTable,'ipConfigEntry':ipConfigEntry,_H:ipConfigPortIdKey,'ipConfigName':ipConfigName,'ipConfigCurIPAddressV4':ipConfigCurIPAddressV4,'ipConfigCurNetworkMaskV4':ipConfigCurNetworkMaskV4,'ipConfigCurDefaultGatewayV4':ipConfigCurDefaultGatewayV4,'ipConfigV4V6Flag':ipConfigV4V6Flag,'ipConfigPortMode':ipConfigPortMode,'ethStatusLink':ethStatusLink,'ethStatusSpeed':ethStatusSpeed,'ethStatusDuplex':ethStatusDuplex,'ethStatusXover':ethStatusXover,'ethBackupTable':ethBackupTable,'ethBackupEntry':ethBackupEntry,_I:ethBackupIndex,'ethBackupMode':ethBackupMode,'ethBackupDirection':ethBackupDirection,'ethBackupDelayForward':ethBackupDelayForward,'ethBackupDelayBack':ethBackupDelayBack,'ethBackupStatusTable':ethBackupStatusTable,'ethBackupStatusEntry':ethBackupStatusEntry,_J:ethBackupStatusIndex,'ethBackupStatusPortsInUse':ethBackupStatusPortsInUse,'ethBackupStatusChangeReason':ethBackupStatusChangeReason,'ethBackupStatusChangeDateTime':ethBackupStatusChangeDateTime})