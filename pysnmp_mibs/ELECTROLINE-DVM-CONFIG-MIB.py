_H='cfgEmsAddressIndex'
_G='ELECTROLINE-DVM-CONFIG-MIB'
_F='DisplayString'
_E='SnmpAdminString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
TenthdB,TenthdBmV=mibBuilder.importSymbols('DOCS-IF-MIB','TenthdB','TenthdBmV')
dvmConfiguration,=mibBuilder.importSymbols('ELECTROLINE-DVM-ROOT-MIB','dvmConfiguration')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TruthValue')
_DvmCfgGlobal_ObjectIdentity=ObjectIdentity
dvmCfgGlobal=_DvmCfgGlobal_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,2,1))
if mibBuilder.loadTexts:dvmCfgGlobal.setStatus(_A)
_DvmCfgEms_ObjectIdentity=ObjectIdentity
dvmCfgEms=_DvmCfgEms_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,2,1,1))
if mibBuilder.loadTexts:dvmCfgEms.setStatus(_A)
_CfgEmsAddressTable_Object=MibTable
cfgEmsAddressTable=_CfgEmsAddressTable_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,1,1))
if mibBuilder.loadTexts:cfgEmsAddressTable.setStatus(_A)
_CfgEmsAddressEntry_Object=MibTableRow
cfgEmsAddressEntry=_CfgEmsAddressEntry_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,1,1,1))
cfgEmsAddressEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cfgEmsAddressEntry.setStatus(_A)
_CfgEmsAddressIndex_Type=Integer32
_CfgEmsAddressIndex_Object=MibTableColumn
cfgEmsAddressIndex=_CfgEmsAddressIndex_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,1,1,1,1),_CfgEmsAddressIndex_Type())
cfgEmsAddressIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgEmsAddressIndex.setStatus(_A)
_CfgEmsAddressIP_Type=IpAddress
_CfgEmsAddressIP_Object=MibTableColumn
cfgEmsAddressIP=_CfgEmsAddressIP_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,1,1,1,2),_CfgEmsAddressIP_Type())
cfgEmsAddressIP.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsAddressIP.setStatus(_A)
class _CfgEmsAddressTrapPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CfgEmsAddressTrapPortNumber_Type.__name__=_C
_CfgEmsAddressTrapPortNumber_Object=MibTableColumn
cfgEmsAddressTrapPortNumber=_CfgEmsAddressTrapPortNumber_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,1,1,1,3),_CfgEmsAddressTrapPortNumber_Type())
cfgEmsAddressTrapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsAddressTrapPortNumber.setStatus(_A)
_CfgEmsAddressType_Type=InetAddressType
_CfgEmsAddressType_Object=MibTableColumn
cfgEmsAddressType=_CfgEmsAddressType_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,1,1,1,4),_CfgEmsAddressType_Type())
cfgEmsAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsAddressType.setStatus(_A)
_CfgEmsAddress_Type=InetAddress
_CfgEmsAddress_Object=MibTableColumn
cfgEmsAddress=_CfgEmsAddress_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,1,1,1,5),_CfgEmsAddress_Type())
cfgEmsAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsAddress.setStatus(_A)
class _CfgEmsAddressProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('snmp',1),('http_post',2)))
_CfgEmsAddressProtocol_Type.__name__=_C
_CfgEmsAddressProtocol_Object=MibTableColumn
cfgEmsAddressProtocol=_CfgEmsAddressProtocol_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,1,1,1,6),_CfgEmsAddressProtocol_Type())
cfgEmsAddressProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsAddressProtocol.setStatus(_A)
class _DvmCfgResetToFactory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_DvmCfgResetToFactory_Type.__name__=_C
_DvmCfgResetToFactory_Object=MibScalar
dvmCfgResetToFactory=_DvmCfgResetToFactory_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,2),_DvmCfgResetToFactory_Type())
dvmCfgResetToFactory.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmCfgResetToFactory.setStatus(_A)
class _DvmCfgUsbMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cpe',1),('craft',2)))
_DvmCfgUsbMode_Type.__name__=_C
_DvmCfgUsbMode_Object=MibScalar
dvmCfgUsbMode=_DvmCfgUsbMode_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,3),_DvmCfgUsbMode_Type())
dvmCfgUsbMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmCfgUsbMode.setStatus(_A)
_DvmChannelBondingEnable_Type=TruthValue
_DvmChannelBondingEnable_Object=MibScalar
dvmChannelBondingEnable=_DvmChannelBondingEnable_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,4),_DvmChannelBondingEnable_Type())
dvmChannelBondingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmChannelBondingEnable.setStatus(_A)
_DvmCfgFpga_ObjectIdentity=ObjectIdentity
dvmCfgFpga=_DvmCfgFpga_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,2,1,5))
if mibBuilder.loadTexts:dvmCfgFpga.setStatus(_A)
_DvmCfgFpgaSoftware_ObjectIdentity=ObjectIdentity
dvmCfgFpgaSoftware=_DvmCfgFpgaSoftware_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,3,2,1,5,1))
if mibBuilder.loadTexts:dvmCfgFpgaSoftware.setStatus(_A)
_DvmCfgFpgaSwServerAddressType_Type=InetAddressType
_DvmCfgFpgaSwServerAddressType_Object=MibScalar
dvmCfgFpgaSwServerAddressType=_DvmCfgFpgaSwServerAddressType_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,5,1,1),_DvmCfgFpgaSwServerAddressType_Type())
dvmCfgFpgaSwServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmCfgFpgaSwServerAddressType.setStatus(_A)
_DvmCfgFpgaSwServer_Type=IpAddress
_DvmCfgFpgaSwServer_Object=MibScalar
dvmCfgFpgaSwServer=_DvmCfgFpgaSwServer_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,5,1,2),_DvmCfgFpgaSwServer_Type())
dvmCfgFpgaSwServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmCfgFpgaSwServer.setStatus(_A)
_DvmCfgFpgaSwServerAddress_Type=InetAddress
_DvmCfgFpgaSwServerAddress_Object=MibScalar
dvmCfgFpgaSwServerAddress=_DvmCfgFpgaSwServerAddress_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,5,1,3),_DvmCfgFpgaSwServerAddress_Type())
dvmCfgFpgaSwServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmCfgFpgaSwServerAddress.setStatus(_A)
class _DvmCfgFpgaSwFilename_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DvmCfgFpgaSwFilename_Type.__name__=_E
_DvmCfgFpgaSwFilename_Object=MibScalar
dvmCfgFpgaSwFilename=_DvmCfgFpgaSwFilename_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,5,1,4),_DvmCfgFpgaSwFilename_Type())
dvmCfgFpgaSwFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmCfgFpgaSwFilename.setStatus(_A)
_DvmCfgFpgaSwDloadNow_Type=TruthValue
_DvmCfgFpgaSwDloadNow_Object=MibScalar
dvmCfgFpgaSwDloadNow=_DvmCfgFpgaSwDloadNow_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,5,1,5),_DvmCfgFpgaSwDloadNow_Type())
dvmCfgFpgaSwDloadNow.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmCfgFpgaSwDloadNow.setStatus(_A)
class _DvmCfgFpgaSwDloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('failure',0),('success',1),('inProgress',2),('other',3)))
_DvmCfgFpgaSwDloadStatus_Type.__name__=_C
_DvmCfgFpgaSwDloadStatus_Object=MibScalar
dvmCfgFpgaSwDloadStatus=_DvmCfgFpgaSwDloadStatus_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,5,1,6),_DvmCfgFpgaSwDloadStatus_Type())
dvmCfgFpgaSwDloadStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmCfgFpgaSwDloadStatus.setStatus(_A)
_DvmCfgFpgaSwCurrentVers_Type=SnmpAdminString
_DvmCfgFpgaSwCurrentVers_Object=MibScalar
dvmCfgFpgaSwCurrentVers=_DvmCfgFpgaSwCurrentVers_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,5,1,7),_DvmCfgFpgaSwCurrentVers_Type())
dvmCfgFpgaSwCurrentVers.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmCfgFpgaSwCurrentVers.setStatus(_A)
class _DvmCfgSystemTrapEnginFilter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DvmCfgSystemTrapEnginFilter_Type.__name__=_F
_DvmCfgSystemTrapEnginFilter_Object=MibScalar
dvmCfgSystemTrapEnginFilter=_DvmCfgSystemTrapEnginFilter_Object((1,3,6,1,4,1,5802,1,3,1,3,2,1,6),_DvmCfgSystemTrapEnginFilter_Type())
dvmCfgSystemTrapEnginFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmCfgSystemTrapEnginFilter.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'dvmCfgGlobal':dvmCfgGlobal,'dvmCfgEms':dvmCfgEms,'cfgEmsAddressTable':cfgEmsAddressTable,'cfgEmsAddressEntry':cfgEmsAddressEntry,_H:cfgEmsAddressIndex,'cfgEmsAddressIP':cfgEmsAddressIP,'cfgEmsAddressTrapPortNumber':cfgEmsAddressTrapPortNumber,'cfgEmsAddressType':cfgEmsAddressType,'cfgEmsAddress':cfgEmsAddress,'cfgEmsAddressProtocol':cfgEmsAddressProtocol,'dvmCfgResetToFactory':dvmCfgResetToFactory,'dvmCfgUsbMode':dvmCfgUsbMode,'dvmChannelBondingEnable':dvmChannelBondingEnable,'dvmCfgFpga':dvmCfgFpga,'dvmCfgFpgaSoftware':dvmCfgFpgaSoftware,'dvmCfgFpgaSwServerAddressType':dvmCfgFpgaSwServerAddressType,'dvmCfgFpgaSwServer':dvmCfgFpgaSwServer,'dvmCfgFpgaSwServerAddress':dvmCfgFpgaSwServerAddress,'dvmCfgFpgaSwFilename':dvmCfgFpgaSwFilename,'dvmCfgFpgaSwDloadNow':dvmCfgFpgaSwDloadNow,'dvmCfgFpgaSwDloadStatus':dvmCfgFpgaSwDloadStatus,'dvmCfgFpgaSwCurrentVers':dvmCfgFpgaSwCurrentVers,'dvmCfgSystemTrapEnginFilter':dvmCfgSystemTrapEnginFilter})