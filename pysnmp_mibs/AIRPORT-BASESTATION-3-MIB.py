_G='physicalInterfaceIndex'
_F='dhcpPhysAddress'
_E='wirelessPhysAddress'
_D='AIRPORT-BASESTATION-3-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
baseStation3=ModuleIdentity((1,3,6,1,4,1,63,501,3))
_Apple_ObjectIdentity=ObjectIdentity
apple=_Apple_ObjectIdentity((1,3,6,1,4,1,63))
_Airport_ObjectIdentity=ObjectIdentity
airport=_Airport_ObjectIdentity((1,3,6,1,4,1,63,501))
_Abs3SysConf_ObjectIdentity=ObjectIdentity
abs3SysConf=_Abs3SysConf_ObjectIdentity((1,3,6,1,4,1,63,501,3,1))
_SysConfName_Type=DisplayString
_SysConfName_Object=MibScalar
sysConfName=_SysConfName_Object((1,3,6,1,4,1,63,501,3,1,1),_SysConfName_Type())
sysConfName.setMaxAccess(_B)
if mibBuilder.loadTexts:sysConfName.setStatus(_A)
_SysConfContact_Type=DisplayString
_SysConfContact_Object=MibScalar
sysConfContact=_SysConfContact_Object((1,3,6,1,4,1,63,501,3,1,2),_SysConfContact_Type())
sysConfContact.setMaxAccess(_B)
if mibBuilder.loadTexts:sysConfContact.setStatus(_A)
_SysConfLocation_Type=DisplayString
_SysConfLocation_Object=MibScalar
sysConfLocation=_SysConfLocation_Object((1,3,6,1,4,1,63,501,3,1,3),_SysConfLocation_Type())
sysConfLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:sysConfLocation.setStatus(_A)
_SysConfUptime_Type=Integer32
_SysConfUptime_Object=MibScalar
sysConfUptime=_SysConfUptime_Object((1,3,6,1,4,1,63,501,3,1,4),_SysConfUptime_Type())
sysConfUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:sysConfUptime.setStatus(_A)
_SysConfFirmwareVersion_Type=DisplayString
_SysConfFirmwareVersion_Object=MibScalar
sysConfFirmwareVersion=_SysConfFirmwareVersion_Object((1,3,6,1,4,1,63,501,3,1,5),_SysConfFirmwareVersion_Type())
sysConfFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sysConfFirmwareVersion.setStatus(_A)
_Wireless_ObjectIdentity=ObjectIdentity
wireless=_Wireless_ObjectIdentity((1,3,6,1,4,1,63,501,3,2))
_WirelessNumber_Type=Integer32
_WirelessNumber_Object=MibScalar
wirelessNumber=_WirelessNumber_Object((1,3,6,1,4,1,63,501,3,2,1),_WirelessNumber_Type())
wirelessNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessNumber.setStatus(_A)
_WirelessClientsTable_Object=MibTable
wirelessClientsTable=_WirelessClientsTable_Object((1,3,6,1,4,1,63,501,3,2,2))
if mibBuilder.loadTexts:wirelessClientsTable.setStatus(_A)
_WirelessClient_Object=MibTableRow
wirelessClient=_WirelessClient_Object((1,3,6,1,4,1,63,501,3,2,2,1))
wirelessClient.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:wirelessClient.setStatus(_A)
_WirelessPhysAddress_Type=PhysAddress
_WirelessPhysAddress_Object=MibTableColumn
wirelessPhysAddress=_WirelessPhysAddress_Object((1,3,6,1,4,1,63,501,3,2,2,1,1),_WirelessPhysAddress_Type())
wirelessPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessPhysAddress.setStatus(_A)
class _WirelessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sta',1),('wds',2)))
_WirelessType_Type.__name__=_C
_WirelessType_Object=MibTableColumn
wirelessType=_WirelessType_Object((1,3,6,1,4,1,63,501,3,2,2,1,2),_WirelessType_Type())
wirelessType.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessType.setStatus(_A)
_WirelessDataRates_Type=DisplayString
_WirelessDataRates_Object=MibTableColumn
wirelessDataRates=_WirelessDataRates_Object((1,3,6,1,4,1,63,501,3,2,2,1,3),_WirelessDataRates_Type())
wirelessDataRates.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessDataRates.setStatus(_A)
_WirelessTimeAssociated_Type=Integer32
_WirelessTimeAssociated_Object=MibTableColumn
wirelessTimeAssociated=_WirelessTimeAssociated_Object((1,3,6,1,4,1,63,501,3,2,2,1,4),_WirelessTimeAssociated_Type())
wirelessTimeAssociated.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessTimeAssociated.setStatus(_A)
_WirelessLastRefreshTime_Type=Integer32
_WirelessLastRefreshTime_Object=MibTableColumn
wirelessLastRefreshTime=_WirelessLastRefreshTime_Object((1,3,6,1,4,1,63,501,3,2,2,1,5),_WirelessLastRefreshTime_Type())
wirelessLastRefreshTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessLastRefreshTime.setStatus(_A)
_WirelessStrength_Type=Integer32
_WirelessStrength_Object=MibTableColumn
wirelessStrength=_WirelessStrength_Object((1,3,6,1,4,1,63,501,3,2,2,1,6),_WirelessStrength_Type())
wirelessStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessStrength.setStatus(_A)
_WirelessNoise_Type=Integer32
_WirelessNoise_Object=MibTableColumn
wirelessNoise=_WirelessNoise_Object((1,3,6,1,4,1,63,501,3,2,2,1,7),_WirelessNoise_Type())
wirelessNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessNoise.setStatus(_A)
_WirelessRate_Type=Integer32
_WirelessRate_Object=MibTableColumn
wirelessRate=_WirelessRate_Object((1,3,6,1,4,1,63,501,3,2,2,1,8),_WirelessRate_Type())
wirelessRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessRate.setStatus(_A)
_WirelessNumRX_Type=Integer32
_WirelessNumRX_Object=MibTableColumn
wirelessNumRX=_WirelessNumRX_Object((1,3,6,1,4,1,63,501,3,2,2,1,9),_WirelessNumRX_Type())
wirelessNumRX.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessNumRX.setStatus(_A)
_WirelessNumTX_Type=Integer32
_WirelessNumTX_Object=MibTableColumn
wirelessNumTX=_WirelessNumTX_Object((1,3,6,1,4,1,63,501,3,2,2,1,10),_WirelessNumTX_Type())
wirelessNumTX.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessNumTX.setStatus(_A)
_WirelessNumRXErrors_Type=Integer32
_WirelessNumRXErrors_Object=MibTableColumn
wirelessNumRXErrors=_WirelessNumRXErrors_Object((1,3,6,1,4,1,63,501,3,2,2,1,11),_WirelessNumRXErrors_Type())
wirelessNumRXErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessNumRXErrors.setStatus(_A)
_WirelessNumTXErrors_Type=Integer32
_WirelessNumTXErrors_Object=MibTableColumn
wirelessNumTXErrors=_WirelessNumTXErrors_Object((1,3,6,1,4,1,63,501,3,2,2,1,12),_WirelessNumTXErrors_Type())
wirelessNumTXErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessNumTXErrors.setStatus(_A)
_DhcpServer_ObjectIdentity=ObjectIdentity
dhcpServer=_DhcpServer_ObjectIdentity((1,3,6,1,4,1,63,501,3,3))
_DhcpNumber_Type=Integer32
_DhcpNumber_Object=MibScalar
dhcpNumber=_DhcpNumber_Object((1,3,6,1,4,1,63,501,3,3,1),_DhcpNumber_Type())
dhcpNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpNumber.setStatus(_A)
_DhcpClientsTable_Object=MibTable
dhcpClientsTable=_DhcpClientsTable_Object((1,3,6,1,4,1,63,501,3,3,2))
if mibBuilder.loadTexts:dhcpClientsTable.setStatus(_A)
_DhcpClient_Object=MibTableRow
dhcpClient=_DhcpClient_Object((1,3,6,1,4,1,63,501,3,3,2,1))
dhcpClient.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:dhcpClient.setStatus(_A)
_DhcpPhysAddress_Type=PhysAddress
_DhcpPhysAddress_Object=MibTableColumn
dhcpPhysAddress=_DhcpPhysAddress_Object((1,3,6,1,4,1,63,501,3,3,2,1,1),_DhcpPhysAddress_Type())
dhcpPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpPhysAddress.setStatus(_A)
_DhcpIpAddress_Type=IpAddress
_DhcpIpAddress_Object=MibTableColumn
dhcpIpAddress=_DhcpIpAddress_Object((1,3,6,1,4,1,63,501,3,3,2,1,2),_DhcpIpAddress_Type())
dhcpIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpIpAddress.setStatus(_A)
_DhcpClientID_Type=OctetString
_DhcpClientID_Object=MibTableColumn
dhcpClientID=_DhcpClientID_Object((1,3,6,1,4,1,63,501,3,3,2,1,3),_DhcpClientID_Type())
dhcpClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientID.setStatus(_A)
_DhcpLeaseTime_Type=Integer32
_DhcpLeaseTime_Object=MibTableColumn
dhcpLeaseTime=_DhcpLeaseTime_Object((1,3,6,1,4,1,63,501,3,3,2,1,4),_DhcpLeaseTime_Type())
dhcpLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseTime.setStatus(_A)
_PhysicalInterfaces_ObjectIdentity=ObjectIdentity
physicalInterfaces=_PhysicalInterfaces_ObjectIdentity((1,3,6,1,4,1,63,501,3,4))
_PhysicalInterfaceCount_Type=Integer32
_PhysicalInterfaceCount_Object=MibScalar
physicalInterfaceCount=_PhysicalInterfaceCount_Object((1,3,6,1,4,1,63,501,3,4,1),_PhysicalInterfaceCount_Type())
physicalInterfaceCount.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceCount.setStatus(_A)
_PhysicalInterfacesTable_Object=MibTable
physicalInterfacesTable=_PhysicalInterfacesTable_Object((1,3,6,1,4,1,63,501,3,4,2))
if mibBuilder.loadTexts:physicalInterfacesTable.setStatus(_A)
_PhysicalInterface_Object=MibTableRow
physicalInterface=_PhysicalInterface_Object((1,3,6,1,4,1,63,501,3,4,2,1))
physicalInterface.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:physicalInterface.setStatus(_A)
_PhysicalInterfaceIndex_Type=Integer32
_PhysicalInterfaceIndex_Object=MibTableColumn
physicalInterfaceIndex=_PhysicalInterfaceIndex_Object((1,3,6,1,4,1,63,501,3,4,2,1,1),_PhysicalInterfaceIndex_Type())
physicalInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceIndex.setStatus(_A)
_PhysicalInterfaceName_Type=OctetString
_PhysicalInterfaceName_Object=MibTableColumn
physicalInterfaceName=_PhysicalInterfaceName_Object((1,3,6,1,4,1,63,501,3,4,2,1,2),_PhysicalInterfaceName_Type())
physicalInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceName.setStatus(_A)
_PhysicalInterfaceUnit_Type=Integer32
_PhysicalInterfaceUnit_Object=MibTableColumn
physicalInterfaceUnit=_PhysicalInterfaceUnit_Object((1,3,6,1,4,1,63,501,3,4,2,1,3),_PhysicalInterfaceUnit_Type())
physicalInterfaceUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceUnit.setStatus(_A)
_PhysicalInterfaceSpeed_Type=Integer32
_PhysicalInterfaceSpeed_Object=MibTableColumn
physicalInterfaceSpeed=_PhysicalInterfaceSpeed_Object((1,3,6,1,4,1,63,501,3,4,2,1,4),_PhysicalInterfaceSpeed_Type())
physicalInterfaceSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceSpeed.setStatus(_A)
class _PhysicalInterfaceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('linkDown',0),('linkUp',1)))
_PhysicalInterfaceState_Type.__name__=_C
_PhysicalInterfaceState_Object=MibTableColumn
physicalInterfaceState=_PhysicalInterfaceState_Object((1,3,6,1,4,1,63,501,3,4,2,1,5),_PhysicalInterfaceState_Type())
physicalInterfaceState.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceState.setStatus(_A)
class _PhysicalInterfaceDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('half',0),('full',1)))
_PhysicalInterfaceDuplex_Type.__name__=_C
_PhysicalInterfaceDuplex_Object=MibTableColumn
physicalInterfaceDuplex=_PhysicalInterfaceDuplex_Object((1,3,6,1,4,1,63,501,3,4,2,1,6),_PhysicalInterfaceDuplex_Type())
physicalInterfaceDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceDuplex.setStatus(_A)
_PhysicalInterfaceNumTX_Type=Integer32
_PhysicalInterfaceNumTX_Object=MibTableColumn
physicalInterfaceNumTX=_PhysicalInterfaceNumTX_Object((1,3,6,1,4,1,63,501,3,4,2,1,7),_PhysicalInterfaceNumTX_Type())
physicalInterfaceNumTX.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceNumTX.setStatus(_A)
_PhysicalInterfaceNumRX_Type=Integer32
_PhysicalInterfaceNumRX_Object=MibTableColumn
physicalInterfaceNumRX=_PhysicalInterfaceNumRX_Object((1,3,6,1,4,1,63,501,3,4,2,1,8),_PhysicalInterfaceNumRX_Type())
physicalInterfaceNumRX.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceNumRX.setStatus(_A)
_PhysicalInterfaceNumTXError_Type=Integer32
_PhysicalInterfaceNumTXError_Object=MibTableColumn
physicalInterfaceNumTXError=_PhysicalInterfaceNumTXError_Object((1,3,6,1,4,1,63,501,3,4,2,1,9),_PhysicalInterfaceNumTXError_Type())
physicalInterfaceNumTXError.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceNumTXError.setStatus(_A)
_PhysicalInterfaceNumRXError_Type=Integer32
_PhysicalInterfaceNumRXError_Object=MibTableColumn
physicalInterfaceNumRXError=_PhysicalInterfaceNumRXError_Object((1,3,6,1,4,1,63,501,3,4,2,1,10),_PhysicalInterfaceNumRXError_Type())
physicalInterfaceNumRXError.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalInterfaceNumRXError.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'apple':apple,'airport':airport,'baseStation3':baseStation3,'abs3SysConf':abs3SysConf,'sysConfName':sysConfName,'sysConfContact':sysConfContact,'sysConfLocation':sysConfLocation,'sysConfUptime':sysConfUptime,'sysConfFirmwareVersion':sysConfFirmwareVersion,'wireless':wireless,'wirelessNumber':wirelessNumber,'wirelessClientsTable':wirelessClientsTable,'wirelessClient':wirelessClient,_E:wirelessPhysAddress,'wirelessType':wirelessType,'wirelessDataRates':wirelessDataRates,'wirelessTimeAssociated':wirelessTimeAssociated,'wirelessLastRefreshTime':wirelessLastRefreshTime,'wirelessStrength':wirelessStrength,'wirelessNoise':wirelessNoise,'wirelessRate':wirelessRate,'wirelessNumRX':wirelessNumRX,'wirelessNumTX':wirelessNumTX,'wirelessNumRXErrors':wirelessNumRXErrors,'wirelessNumTXErrors':wirelessNumTXErrors,'dhcpServer':dhcpServer,'dhcpNumber':dhcpNumber,'dhcpClientsTable':dhcpClientsTable,'dhcpClient':dhcpClient,_F:dhcpPhysAddress,'dhcpIpAddress':dhcpIpAddress,'dhcpClientID':dhcpClientID,'dhcpLeaseTime':dhcpLeaseTime,'physicalInterfaces':physicalInterfaces,'physicalInterfaceCount':physicalInterfaceCount,'physicalInterfacesTable':physicalInterfacesTable,'physicalInterface':physicalInterface,_G:physicalInterfaceIndex,'physicalInterfaceName':physicalInterfaceName,'physicalInterfaceUnit':physicalInterfaceUnit,'physicalInterfaceSpeed':physicalInterfaceSpeed,'physicalInterfaceState':physicalInterfaceState,'physicalInterfaceDuplex':physicalInterfaceDuplex,'physicalInterfaceNumTX':physicalInterfaceNumTX,'physicalInterfaceNumRX':physicalInterfaceNumRX,'physicalInterfaceNumTXError':physicalInterfaceNumTXError,'physicalInterfaceNumRXError':physicalInterfaceNumRXError})