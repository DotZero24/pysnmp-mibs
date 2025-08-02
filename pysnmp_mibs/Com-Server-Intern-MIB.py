_L='wtDeaDrvInterfaceNo'
_K='DisplayString'
_J='NotificationType'
_I='wtDeaDrvInputRegister'
_H='wtDeaInterfaceNo'
_G='wtSeriInterfaceNo'
_F='read-only'
_E='Com-Server-Intern-MIB'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
_Wut_ObjectIdentity=ObjectIdentity
wut=_Wut_ObjectIdentity((1,3,6,1,4,1,5040))
_WtComServer_ObjectIdentity=ObjectIdentity
wtComServer=_WtComServer_ObjectIdentity((1,3,6,1,4,1,5040,1))
_WtComServerIntern_ObjectIdentity=ObjectIdentity
wtComServerIntern=_WtComServerIntern_ObjectIdentity((1,3,6,1,4,1,5040,1,1))
_WtConfiguration_ObjectIdentity=ObjectIdentity
wtConfiguration=_WtConfiguration_ObjectIdentity((1,3,6,1,4,1,5040,1,1,1))
_WtSystem_ObjectIdentity=ObjectIdentity
wtSystem=_WtSystem_ObjectIdentity((1,3,6,1,4,1,5040,1,1,1,1))
class _WtCableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,8,16)));namedValues=NamedValues(*(('wtCoax',1),('wtTwistedPair',2),('wtAui',3),('wtTwistedPair10FD',4),('wtTwistedPair100HD',8),('wtTwistedPair100FD',16)))
_WtCableType_Type.__name__=_C
_WtCableType_Object=MibScalar
wtCableType=_WtCableType_Object((1,3,6,1,4,1,5040,1,1,1,1,1),_WtCableType_Type())
wtCableType.setMaxAccess(_F)
if mibBuilder.loadTexts:wtCableType.setStatus(_A)
_WtMacAddress_Type=PhysAddress
_WtMacAddress_Object=MibScalar
wtMacAddress=_WtMacAddress_Object((1,3,6,1,4,1,5040,1,1,1,1,2),_WtMacAddress_Type())
wtMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:wtMacAddress.setStatus(_A)
_WtSwDate_Type=DisplayString
_WtSwDate_Object=MibScalar
wtSwDate=_WtSwDate_Object((1,3,6,1,4,1,5040,1,1,1,1,3),_WtSwDate_Type())
wtSwDate.setMaxAccess(_F)
if mibBuilder.loadTexts:wtSwDate.setStatus(_A)
_WtSwRev_Type=DisplayString
_WtSwRev_Object=MibScalar
wtSwRev=_WtSwRev_Object((1,3,6,1,4,1,5040,1,1,1,1,4),_WtSwRev_Type())
wtSwRev.setMaxAccess(_F)
if mibBuilder.loadTexts:wtSwRev.setStatus(_A)
_WtDevType_Type=DisplayString
_WtDevType_Object=MibScalar
wtDevType=_WtDevType_Object((1,3,6,1,4,1,5040,1,1,1,1,5),_WtDevType_Type())
wtDevType.setMaxAccess(_F)
if mibBuilder.loadTexts:wtDevType.setStatus(_A)
_WtMibRev_Type=DisplayString
_WtMibRev_Object=MibScalar
wtMibRev=_WtMibRev_Object((1,3,6,1,4,1,5040,1,1,1,1,6),_WtMibRev_Type())
wtMibRev.setMaxAccess(_F)
if mibBuilder.loadTexts:wtMibRev.setStatus(_A)
_WtRunTime_Type=TimeTicks
_WtRunTime_Object=MibScalar
wtRunTime=_WtRunTime_Object((1,3,6,1,4,1,5040,1,1,1,1,7),_WtRunTime_Type())
wtRunTime.setMaxAccess(_F)
if mibBuilder.loadTexts:wtRunTime.setStatus(_A)
class _WtPhysPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WtPhysPorts_Type.__name__=_C
_WtPhysPorts_Object=MibScalar
wtPhysPorts=_WtPhysPorts_Object((1,3,6,1,4,1,5040,1,1,1,1,8),_WtPhysPorts_Type())
wtPhysPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:wtPhysPorts.setStatus(_A)
class _WtConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('wtConfigModeOff',1),('wtConfigModeOn',2),('wtSaveConfig',3)))
_WtConfigMode_Type.__name__=_C
_WtConfigMode_Object=MibScalar
wtConfigMode=_WtConfigMode_Object((1,3,6,1,4,1,5040,1,1,1,1,16),_WtConfigMode_Type())
wtConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtConfigMode.setStatus(_A)
class _WtPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_WtPassword_Type.__name__=_K
_WtPassword_Object=MibScalar
wtPassword=_WtPassword_Object((1,3,6,1,4,1,5040,1,1,1,1,17),_WtPassword_Type())
wtPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtPassword.setStatus(_A)
_WtSysPswd_Type=OctetString
_WtSysPswd_Object=MibScalar
wtSysPswd=_WtSysPswd_Object((1,3,6,1,4,1,5040,1,1,1,1,18),_WtSysPswd_Type())
wtSysPswd.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSysPswd.setStatus(_A)
_WtSysName_Type=OctetString
_WtSysName_Object=MibScalar
wtSysName=_WtSysName_Object((1,3,6,1,4,1,5040,1,1,1,1,19),_WtSysName_Type())
wtSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSysName.setStatus(_A)
_WtNetSetup_ObjectIdentity=ObjectIdentity
wtNetSetup=_WtNetSetup_ObjectIdentity((1,3,6,1,4,1,5040,1,1,1,2))
_WtIpAddress_Type=IpAddress
_WtIpAddress_Object=MibScalar
wtIpAddress=_WtIpAddress_Object((1,3,6,1,4,1,5040,1,1,1,2,1),_WtIpAddress_Type())
wtIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wtIpAddress.setStatus(_A)
_WtSubnetMask_Type=IpAddress
_WtSubnetMask_Object=MibScalar
wtSubnetMask=_WtSubnetMask_Object((1,3,6,1,4,1,5040,1,1,1,2,2),_WtSubnetMask_Type())
wtSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSubnetMask.setStatus(_A)
_WtGateway_Type=IpAddress
_WtGateway_Object=MibScalar
wtGateway=_WtGateway_Object((1,3,6,1,4,1,5040,1,1,1,2,3),_WtGateway_Type())
wtGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wtGateway.setStatus(_A)
class _WtMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,1024))
_WtMtu_Type.__name__=_C
_WtMtu_Object=MibScalar
wtMtu=_WtMtu_Object((1,3,6,1,4,1,5040,1,1,1,2,4),_WtMtu_Type())
wtMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:wtMtu.setStatus(_A)
class _WtBootpClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtBootpClientOff',1),('wtBootpClientOn',2)))
_WtBootpClient_Type.__name__=_C
_WtBootpClient_Object=MibScalar
wtBootpClient=_WtBootpClient_Object((1,3,6,1,4,1,5040,1,1,1,2,5),_WtBootpClient_Type())
wtBootpClient.setMaxAccess(_B)
if mibBuilder.loadTexts:wtBootpClient.setStatus(_A)
class _WtKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,65535))
_WtKeepAlive_Type.__name__=_C
_WtKeepAlive_Object=MibScalar
wtKeepAlive=_WtKeepAlive_Object((1,3,6,1,4,1,5040,1,1,1,2,6),_WtKeepAlive_Type())
wtKeepAlive.setMaxAccess(_B)
if mibBuilder.loadTexts:wtKeepAlive.setStatus(_A)
class _WtRetransmTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtRetransmTimeout_Type.__name__=_C
_WtRetransmTimeout_Object=MibScalar
wtRetransmTimeout=_WtRetransmTimeout_Object((1,3,6,1,4,1,5040,1,1,1,2,7),_WtRetransmTimeout_Type())
wtRetransmTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtRetransmTimeout.setStatus(_A)
class _WtDhcpClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtDhcpClientOff',1),('wtChcpClientOn',2)))
_WtDhcpClient_Type.__name__=_C
_WtDhcpClient_Object=MibScalar
wtDhcpClient=_WtDhcpClient_Object((1,3,6,1,4,1,5040,1,1,1,2,8),_WtDhcpClient_Type())
wtDhcpClient.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDhcpClient.setStatus(_A)
class _WtWbmPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtWbmPort_Type.__name__=_C
_WtWbmPort_Object=MibScalar
wtWbmPort=_WtWbmPort_Object((1,3,6,1,4,1,5040,1,1,1,2,9),_WtWbmPort_Type())
wtWbmPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWbmPort.setStatus(_A)
_WtDnsSrv_Type=IpAddress
_WtDnsSrv_Object=MibScalar
wtDnsSrv=_WtDnsSrv_Object((1,3,6,1,4,1,5040,1,1,1,2,10),_WtDnsSrv_Type())
wtDnsSrv.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDnsSrv.setStatus(_A)
class _WtLinkSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wtLinkSpeedAutonegotiation',1),('wtLinkSpeed10HD',2),('wtLinkSpeed10FD',3),('wtLinkSpeed100HD',4),('wtLinkSpeed100FD',5)))
_WtLinkSpeed_Type.__name__=_C
_WtLinkSpeed_Object=MibScalar
wtLinkSpeed=_WtLinkSpeed_Object((1,3,6,1,4,1,5040,1,1,1,2,11),_WtLinkSpeed_Type())
wtLinkSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:wtLinkSpeed.setStatus(_A)
_WtSeriPortSetup_ObjectIdentity=ObjectIdentity
wtSeriPortSetup=_WtSeriPortSetup_ObjectIdentity((1,3,6,1,4,1,5040,1,1,1,3))
class _WtSerialPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WtSerialPorts_Type.__name__=_C
_WtSerialPorts_Object=MibScalar
wtSerialPorts=_WtSerialPorts_Object((1,3,6,1,4,1,5040,1,1,1,3,1),_WtSerialPorts_Type())
wtSerialPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:wtSerialPorts.setStatus(_A)
_WtSeriInterfaceTable_Object=MibTable
wtSeriInterfaceTable=_WtSeriInterfaceTable_Object((1,3,6,1,4,1,5040,1,1,1,3,2))
if mibBuilder.loadTexts:wtSeriInterfaceTable.setStatus(_A)
_WtSeriInterfaceEntry_Object=MibTableRow
wtSeriInterfaceEntry=_WtSeriInterfaceEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,2,1))
wtSeriInterfaceEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriInterfaceEntry.setStatus(_A)
class _WtSeriInterfaceNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WtSeriInterfaceNo_Type.__name__=_C
_WtSeriInterfaceNo_Object=MibTableColumn
wtSeriInterfaceNo=_WtSeriInterfaceNo_Object((1,3,6,1,4,1,5040,1,1,1,3,2,1,1),_WtSeriInterfaceNo_Type())
wtSeriInterfaceNo.setMaxAccess(_F)
if mibBuilder.loadTexts:wtSeriInterfaceNo.setStatus(_A)
_WtSeriUartTable_Object=MibTable
wtSeriUartTable=_WtSeriUartTable_Object((1,3,6,1,4,1,5040,1,1,1,3,3))
if mibBuilder.loadTexts:wtSeriUartTable.setStatus(_A)
_WtSeriUartEntry_Object=MibTableRow
wtSeriUartEntry=_WtSeriUartEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1))
wtSeriUartEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriUartEntry.setStatus(_A)
class _WtBaudrate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('wtBaudrate-57600',1),('wtBaudrate-38400',2),('wtBaudrate-19200',3),('wtBaudrate-14400',4),('wtBaudrate-9600',5),('wtBaudrate-4800',6),('wtBaudrate-2400',7),('wtBaudrate-1200',8),('wtBaudrate-600',9),('wtBaudrate-300',10),('wtBaudrate-150',11),('wtBaudrate-110',12),('wtBaudrate-75',13),('wtBaudrate-50',14),('wtBaudrate-230400',15),('wtBaudrate-115200',16),('wtBaudrate-7200',17),('wtBaudrate-special',18)))
_WtBaudrate_Type.__name__=_C
_WtBaudrate_Object=MibTableColumn
wtBaudrate=_WtBaudrate_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1,1),_WtBaudrate_Type())
wtBaudrate.setMaxAccess(_B)
if mibBuilder.loadTexts:wtBaudrate.setStatus(_A)
class _WtParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wtNoParity',1),('wtOddParity',2),('wtEvenParity',3),('wtMarkOddParity',4),('wtMarkEvenParity',5)))
_WtParity_Type.__name__=_C
_WtParity_Object=MibTableColumn
wtParity=_WtParity_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1,2),_WtParity_Type())
wtParity.setMaxAccess(_B)
if mibBuilder.loadTexts:wtParity.setStatus(_A)
class _WtDatabits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wtDataBits-8',1),('wtDataBits-7',2),('wtDataBits-6',3),('wtDataBits-5',4)))
_WtDatabits_Type.__name__=_C
_WtDatabits_Object=MibTableColumn
wtDatabits=_WtDatabits_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1,3),_WtDatabits_Type())
wtDatabits.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDatabits.setStatus(_A)
class _WtStopbits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtStopBits-1',1),('wtStopBits-2',2)))
_WtStopbits_Type.__name__=_C
_WtStopbits_Object=MibTableColumn
wtStopbits=_WtStopbits_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1,4),_WtStopbits_Type())
wtStopbits.setMaxAccess(_B)
if mibBuilder.loadTexts:wtStopbits.setStatus(_A)
class _WtHsLines_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtHsLines_Type.__name__=_D
_WtHsLines_Object=MibTableColumn
wtHsLines=_WtHsLines_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1,5),_WtHsLines_Type())
wtHsLines.setMaxAccess(_B)
if mibBuilder.loadTexts:wtHsLines.setStatus(_A)
class _WtHsFunctions_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_WtHsFunctions_Type.__name__=_D
_WtHsFunctions_Object=MibTableColumn
wtHsFunctions=_WtHsFunctions_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1,6),_WtHsFunctions_Type())
wtHsFunctions.setMaxAccess(_B)
if mibBuilder.loadTexts:wtHsFunctions.setStatus(_A)
class _WtUartFifo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,5,7)));namedValues=NamedValues(*(('wtUartFifo-disable',0),('wtUartFifo-8-8',1),('wtUartFifo-16-16',3),('wtUartFifo-32-56',5),('wtUartFifo-56-60',7)))
_WtUartFifo_Type.__name__=_C
_WtUartFifo_Object=MibTableColumn
wtUartFifo=_WtUartFifo_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1,7),_WtUartFifo_Type())
wtUartFifo.setMaxAccess(_B)
if mibBuilder.loadTexts:wtUartFifo.setStatus(_A)
class _WtUartBaudrate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('wtUartBaudrate-230400',1),('wtUartBaudrate-153600',2),('wtUartBaudrate-115200',3),('wtUartBaudrate-57600',4),('wtUartBaudrate-38400',5),('wtUartBaudrate-19200',6),('wtUartBaudrate-9600',7),('wtUartBaudrate-7200',8),('wtUartBaudrate-4800',9),('wtUartBaudrate-2400',10),('wtUartBaudrate-1200',11),('wtUartBaudrate-600',12),('wtUartBaudrate-300',13),('wtUartBaudrate-150',14),('wtUartBaudrate-75',15),('wtUartBaudrate-50',16),('wtUartBaudrate-110',17),('wtUartBaudrate-special',18)))
_WtUartBaudrate_Type.__name__=_C
_WtUartBaudrate_Object=MibTableColumn
wtUartBaudrate=_WtUartBaudrate_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1,8),_WtUartBaudrate_Type())
wtUartBaudrate.setMaxAccess(_B)
if mibBuilder.loadTexts:wtUartBaudrate.setStatus(_A)
class _WtBaudDivisor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_WtBaudDivisor_Type.__name__=_C
_WtBaudDivisor_Object=MibTableColumn
wtBaudDivisor=_WtBaudDivisor_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1,9),_WtBaudDivisor_Type())
wtBaudDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtBaudDivisor.setStatus(_A)
class _WtSeriInQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,4094))
_WtSeriInQueue_Type.__name__=_C
_WtSeriInQueue_Object=MibTableColumn
wtSeriInQueue=_WtSeriInQueue_Object((1,3,6,1,4,1,5040,1,1,1,3,3,1,10),_WtSeriInQueue_Type())
wtSeriInQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriInQueue.setStatus(_A)
_WtSeriPortTable_Object=MibTable
wtSeriPortTable=_WtSeriPortTable_Object((1,3,6,1,4,1,5040,1,1,1,3,4))
if mibBuilder.loadTexts:wtSeriPortTable.setStatus(_A)
_WtSeriPortEntry_Object=MibTableRow
wtSeriPortEntry=_WtSeriPortEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,4,1))
wtSeriPortEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriPortEntry.setStatus(_A)
class _WtSeriLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtSeriLocalPort_Type.__name__=_C
_WtSeriLocalPort_Object=MibTableColumn
wtSeriLocalPort=_WtSeriLocalPort_Object((1,3,6,1,4,1,5040,1,1,1,3,4,1,1),_WtSeriLocalPort_Type())
wtSeriLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriLocalPort.setStatus(_A)
class _WtSeriPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('wtSeriServerMode',1),('wtSeriTcpClient',2),('wtSeriTelnetClient',3),('wtSeriFtpClient',4),('wtSeriBox2BoxMaster',5),('wtSeriUdpMode',6),('wtSeriMultiportProtokoll',7),('wtSeriBox2BoxSlave',8),('wtSeriSlipMode',9),('wtSeriIpBusSlave',10),('wtSeriIpBusMaster',11)))
_WtSeriPortMode_Type.__name__=_C
_WtSeriPortMode_Object=MibTableColumn
wtSeriPortMode=_WtSeriPortMode_Object((1,3,6,1,4,1,5040,1,1,1,3,4,1,2),_WtSeriPortMode_Type())
wtSeriPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriPortMode.setStatus(_A)
class _WtSeriControlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriControlPort_Type.__name__=_C
_WtSeriControlPort_Object=MibTableColumn
wtSeriControlPort=_WtSeriControlPort_Object((1,3,6,1,4,1,5040,1,1,1,3,4,1,3),_WtSeriControlPort_Type())
wtSeriControlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriControlPort.setStatus(_A)
class _WtSeriPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('wtSeriPortFree',0),('wtSeriPortInUse',1),('wtSeriPortLockScanning',2),('wtSeriPortLockConnected',3),('wtSeriPortLockUnconnected',4)))
_WtSeriPortState_Type.__name__=_C
_WtSeriPortState_Object=MibTableColumn
wtSeriPortState=_WtSeriPortState_Object((1,3,6,1,4,1,5040,1,1,1,3,4,1,4),_WtSeriPortState_Type())
wtSeriPortState.setMaxAccess(_F)
if mibBuilder.loadTexts:wtSeriPortState.setStatus(_A)
class _WtSeriRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriRemotePort_Type.__name__=_C
_WtSeriRemotePort_Object=MibTableColumn
wtSeriRemotePort=_WtSeriRemotePort_Object((1,3,6,1,4,1,5040,1,1,1,3,4,1,5),_WtSeriRemotePort_Type())
wtSeriRemotePort.setMaxAccess(_F)
if mibBuilder.loadTexts:wtSeriRemotePort.setStatus(_A)
_WtSeriRemoteIP_Type=IpAddress
_WtSeriRemoteIP_Object=MibTableColumn
wtSeriRemoteIP=_WtSeriRemoteIP_Object((1,3,6,1,4,1,5040,1,1,1,3,4,1,6),_WtSeriRemoteIP_Type())
wtSeriRemoteIP.setMaxAccess(_F)
if mibBuilder.loadTexts:wtSeriRemoteIP.setStatus(_A)
class _WtSeriNetPckDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriNetPckDelay_Type.__name__=_C
_WtSeriNetPckDelay_Object=MibTableColumn
wtSeriNetPckDelay=_WtSeriNetPckDelay_Object((1,3,6,1,4,1,5040,1,1,1,3,4,1,10),_WtSeriNetPckDelay_Type())
wtSeriNetPckDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriNetPckDelay.setStatus(_A)
class _WtSeriFlushBuf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriFlushBufOff',1),('wtSeriFlushBufOn',2)))
_WtSeriFlushBuf_Type.__name__=_C
_WtSeriFlushBuf_Object=MibTableColumn
wtSeriFlushBuf=_WtSeriFlushBuf_Object((1,3,6,1,4,1,5040,1,1,1,3,4,1,11),_WtSeriFlushBuf_Type())
wtSeriFlushBuf.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriFlushBuf.setStatus(_A)
class _WtSeriTelnetEcho_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriTelnetEchoOff',1),('wtSeriTelnetEchoOn',2)))
_WtSeriTelnetEcho_Type.__name__=_C
_WtSeriTelnetEcho_Object=MibTableColumn
wtSeriTelnetEcho=_WtSeriTelnetEcho_Object((1,3,6,1,4,1,5040,1,1,1,3,4,1,12),_WtSeriTelnetEcho_Type())
wtSeriTelnetEcho.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTelnetEcho.setStatus(_A)
_WtSeriTcpClientTable_Object=MibTable
wtSeriTcpClientTable=_WtSeriTcpClientTable_Object((1,3,6,1,4,1,5040,1,1,1,3,5))
if mibBuilder.loadTexts:wtSeriTcpClientTable.setStatus(_A)
_WtSeriTcpClientEntry_Object=MibTableRow
wtSeriTcpClientEntry=_WtSeriTcpClientEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1))
wtSeriTcpClientEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriTcpClientEntry.setStatus(_A)
class _WtSeriTcpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriTcpServerPort_Type.__name__=_C
_WtSeriTcpServerPort_Object=MibTableColumn
wtSeriTcpServerPort=_WtSeriTcpServerPort_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1,1),_WtSeriTcpServerPort_Type())
wtSeriTcpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTcpServerPort.setStatus(_A)
_WtSeriTcpServerIp_Type=IpAddress
_WtSeriTcpServerIp_Object=MibTableColumn
wtSeriTcpServerIp=_WtSeriTcpServerIp_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1,2),_WtSeriTcpServerIp_Type())
wtSeriTcpServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTcpServerIp.setStatus(_A)
class _WtSeriTcpInactTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriTcpInactTimeout_Type.__name__=_C
_WtSeriTcpInactTimeout_Object=MibTableColumn
wtSeriTcpInactTimeout=_WtSeriTcpInactTimeout_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1,3),_WtSeriTcpInactTimeout_Type())
wtSeriTcpInactTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTcpInactTimeout.setStatus(_A)
class _WtSeriTcpConnectTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriTcpConnectTimeout_Type.__name__=_C
_WtSeriTcpConnectTimeout_Object=MibTableColumn
wtSeriTcpConnectTimeout=_WtSeriTcpConnectTimeout_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1,4),_WtSeriTcpConnectTimeout_Type())
wtSeriTcpConnectTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTcpConnectTimeout.setStatus(_A)
class _WtSeriTcpDisconnectChar_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_WtSeriTcpDisconnectChar_Type.__name__=_D
_WtSeriTcpDisconnectChar_Object=MibTableColumn
wtSeriTcpDisconnectChar=_WtSeriTcpDisconnectChar_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1,5),_WtSeriTcpDisconnectChar_Type())
wtSeriTcpDisconnectChar.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTcpDisconnectChar.setStatus(_A)
class _WtSeriTcpDispString1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtSeriTcpDispString1_Type.__name__=_D
_WtSeriTcpDispString1_Object=MibTableColumn
wtSeriTcpDispString1=_WtSeriTcpDispString1_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1,6),_WtSeriTcpDispString1_Type())
wtSeriTcpDispString1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTcpDispString1.setStatus(_A)
class _WtSeriTcpDispString2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtSeriTcpDispString2_Type.__name__=_D
_WtSeriTcpDispString2_Object=MibTableColumn
wtSeriTcpDispString2=_WtSeriTcpDispString2_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1,7),_WtSeriTcpDispString2_Type())
wtSeriTcpDispString2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTcpDispString2.setStatus(_A)
class _WtSeriTcpCAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriTcpCAddressOff',1),('wtSeriTcpCAddressOn',2)))
_WtSeriTcpCAddress_Type.__name__=_C
_WtSeriTcpCAddress_Object=MibTableColumn
wtSeriTcpCAddress=_WtSeriTcpCAddress_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1,8),_WtSeriTcpCAddress_Type())
wtSeriTcpCAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTcpCAddress.setStatus(_A)
class _WtSeriTcpResponseMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriTcpRespModeOff',1),('wtSeriTcpRespModeOn',2)))
_WtSeriTcpResponseMode_Type.__name__=_C
_WtSeriTcpResponseMode_Object=MibTableColumn
wtSeriTcpResponseMode=_WtSeriTcpResponseMode_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1,10),_WtSeriTcpResponseMode_Type())
wtSeriTcpResponseMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTcpResponseMode.setStatus(_A)
_WtSeriTcpServerUrl_Type=OctetString
_WtSeriTcpServerUrl_Object=MibTableColumn
wtSeriTcpServerUrl=_WtSeriTcpServerUrl_Object((1,3,6,1,4,1,5040,1,1,1,3,5,1,11),_WtSeriTcpServerUrl_Type())
wtSeriTcpServerUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTcpServerUrl.setStatus(_A)
_WtSeriUdpClientTable_Object=MibTable
wtSeriUdpClientTable=_WtSeriUdpClientTable_Object((1,3,6,1,4,1,5040,1,1,1,3,6))
if mibBuilder.loadTexts:wtSeriUdpClientTable.setStatus(_A)
_WtSeriUdpClientEntry_Object=MibTableRow
wtSeriUdpClientEntry=_WtSeriUdpClientEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1))
wtSeriUdpClientEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriUdpClientEntry.setStatus(_A)
class _WtSeriUdpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriUdpServerPort_Type.__name__=_C
_WtSeriUdpServerPort_Object=MibTableColumn
wtSeriUdpServerPort=_WtSeriUdpServerPort_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1,1),_WtSeriUdpServerPort_Type())
wtSeriUdpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriUdpServerPort.setStatus(_A)
_WtSeriUdpServerIp_Type=IpAddress
_WtSeriUdpServerIp_Object=MibTableColumn
wtSeriUdpServerIp=_WtSeriUdpServerIp_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1,2),_WtSeriUdpServerIp_Type())
wtSeriUdpServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriUdpServerIp.setStatus(_A)
class _WtSeriUdpDispString1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtSeriUdpDispString1_Type.__name__=_D
_WtSeriUdpDispString1_Object=MibTableColumn
wtSeriUdpDispString1=_WtSeriUdpDispString1_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1,3),_WtSeriUdpDispString1_Type())
wtSeriUdpDispString1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriUdpDispString1.setStatus(_A)
class _WtSeriUdpDispString2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtSeriUdpDispString2_Type.__name__=_D
_WtSeriUdpDispString2_Object=MibTableColumn
wtSeriUdpDispString2=_WtSeriUdpDispString2_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1,4),_WtSeriUdpDispString2_Type())
wtSeriUdpDispString2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriUdpDispString2.setStatus(_A)
class _WtSeriUdpSeriProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriUdpProtocolOff',1),('wtSeriUdpProtocolOn',2)))
_WtSeriUdpSeriProtocol_Type.__name__=_C
_WtSeriUdpSeriProtocol_Object=MibTableColumn
wtSeriUdpSeriProtocol=_WtSeriUdpSeriProtocol_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1,5),_WtSeriUdpSeriProtocol_Type())
wtSeriUdpSeriProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriUdpSeriProtocol.setStatus(_A)
class _WtSeriUdpSeriCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriUdpSeriCodingOff',1),('wtSeriUdpSeriCodingOn',2)))
_WtSeriUdpSeriCoding_Type.__name__=_C
_WtSeriUdpSeriCoding_Object=MibTableColumn
wtSeriUdpSeriCoding=_WtSeriUdpSeriCoding_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1,6),_WtSeriUdpSeriCoding_Type())
wtSeriUdpSeriCoding.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriUdpSeriCoding.setStatus(_A)
class _WtSeriUdpCAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriUdpCAddressOff',1),('wtSeriUdpCAddressOn',2)))
_WtSeriUdpCAddress_Type.__name__=_C
_WtSeriUdpCAddress_Object=MibTableColumn
wtSeriUdpCAddress=_WtSeriUdpCAddress_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1,7),_WtSeriUdpCAddress_Type())
wtSeriUdpCAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriUdpCAddress.setStatus(_A)
class _WtSeriUdpWrCAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriUdpWrCAddressOff',1),('wtSeriUdpWrCAddressOn',2)))
_WtSeriUdpWrCAddress_Type.__name__=_C
_WtSeriUdpWrCAddress_Object=MibTableColumn
wtSeriUdpWrCAddress=_WtSeriUdpWrCAddress_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1,8),_WtSeriUdpWrCAddress_Type())
wtSeriUdpWrCAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriUdpWrCAddress.setStatus(_A)
class _WtSeriUdpDisconnectChar_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_WtSeriUdpDisconnectChar_Type.__name__=_D
_WtSeriUdpDisconnectChar_Object=MibTableColumn
wtSeriUdpDisconnectChar=_WtSeriUdpDisconnectChar_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1,9),_WtSeriUdpDisconnectChar_Type())
wtSeriUdpDisconnectChar.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriUdpDisconnectChar.setStatus(_A)
_WtSeriUdpServerUrl_Type=OctetString
_WtSeriUdpServerUrl_Object=MibTableColumn
wtSeriUdpServerUrl=_WtSeriUdpServerUrl_Object((1,3,6,1,4,1,5040,1,1,1,3,6,1,10),_WtSeriUdpServerUrl_Type())
wtSeriUdpServerUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriUdpServerUrl.setStatus(_A)
_WtSeriTelnetClientTable_Object=MibTable
wtSeriTelnetClientTable=_WtSeriTelnetClientTable_Object((1,3,6,1,4,1,5040,1,1,1,3,7))
if mibBuilder.loadTexts:wtSeriTelnetClientTable.setStatus(_A)
_WtSeriTelnetClientEntry_Object=MibTableRow
wtSeriTelnetClientEntry=_WtSeriTelnetClientEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,7,1))
wtSeriTelnetClientEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriTelnetClientEntry.setStatus(_A)
class _WtSeriTelnetServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriTelnetServerPort_Type.__name__=_C
_WtSeriTelnetServerPort_Object=MibTableColumn
wtSeriTelnetServerPort=_WtSeriTelnetServerPort_Object((1,3,6,1,4,1,5040,1,1,1,3,7,1,1),_WtSeriTelnetServerPort_Type())
wtSeriTelnetServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTelnetServerPort.setStatus(_A)
_WtSeriTelnetServerIp_Type=IpAddress
_WtSeriTelnetServerIp_Object=MibTableColumn
wtSeriTelnetServerIp=_WtSeriTelnetServerIp_Object((1,3,6,1,4,1,5040,1,1,1,3,7,1,2),_WtSeriTelnetServerIp_Type())
wtSeriTelnetServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTelnetServerIp.setStatus(_A)
class _WtSeriTelnetInactTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriTelnetInactTimeout_Type.__name__=_C
_WtSeriTelnetInactTimeout_Object=MibTableColumn
wtSeriTelnetInactTimeout=_WtSeriTelnetInactTimeout_Object((1,3,6,1,4,1,5040,1,1,1,3,7,1,3),_WtSeriTelnetInactTimeout_Type())
wtSeriTelnetInactTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTelnetInactTimeout.setStatus(_A)
class _WtSeriTelnetDisconnectChar_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_WtSeriTelnetDisconnectChar_Type.__name__=_D
_WtSeriTelnetDisconnectChar_Object=MibTableColumn
wtSeriTelnetDisconnectChar=_WtSeriTelnetDisconnectChar_Object((1,3,6,1,4,1,5040,1,1,1,3,7,1,4),_WtSeriTelnetDisconnectChar_Type())
wtSeriTelnetDisconnectChar.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTelnetDisconnectChar.setStatus(_A)
class _WtSeriTelnetChangeLineout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriTelnetChangeLineoutOff',1),('wtSeriTelnetChangeLineoutOn',2)))
_WtSeriTelnetChangeLineout_Type.__name__=_C
_WtSeriTelnetChangeLineout_Object=MibTableColumn
wtSeriTelnetChangeLineout=_WtSeriTelnetChangeLineout_Object((1,3,6,1,4,1,5040,1,1,1,3,7,1,5),_WtSeriTelnetChangeLineout_Type())
wtSeriTelnetChangeLineout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTelnetChangeLineout.setStatus(_A)
_WtSeriTelnetServerUrl_Type=OctetString
_WtSeriTelnetServerUrl_Object=MibTableColumn
wtSeriTelnetServerUrl=_WtSeriTelnetServerUrl_Object((1,3,6,1,4,1,5040,1,1,1,3,7,1,6),_WtSeriTelnetServerUrl_Type())
wtSeriTelnetServerUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriTelnetServerUrl.setStatus(_A)
_WtSeriFtpClientTable_Object=MibTable
wtSeriFtpClientTable=_WtSeriFtpClientTable_Object((1,3,6,1,4,1,5040,1,1,1,3,8))
if mibBuilder.loadTexts:wtSeriFtpClientTable.setStatus(_A)
_WtSeriFtpClientEntry_Object=MibTableRow
wtSeriFtpClientEntry=_WtSeriFtpClientEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,8,1))
wtSeriFtpClientEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriFtpClientEntry.setStatus(_A)
class _WtSeriFtpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriFtpServerPort_Type.__name__=_C
_WtSeriFtpServerPort_Object=MibTableColumn
wtSeriFtpServerPort=_WtSeriFtpServerPort_Object((1,3,6,1,4,1,5040,1,1,1,3,8,1,1),_WtSeriFtpServerPort_Type())
wtSeriFtpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriFtpServerPort.setStatus(_A)
_WtSeriFtpServerIp_Type=IpAddress
_WtSeriFtpServerIp_Object=MibTableColumn
wtSeriFtpServerIp=_WtSeriFtpServerIp_Object((1,3,6,1,4,1,5040,1,1,1,3,8,1,2),_WtSeriFtpServerIp_Type())
wtSeriFtpServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriFtpServerIp.setStatus(_A)
class _WtSeriFtpAutoFtp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriAutoFtpOff',1),('wtSeriAutoFtpOn',2)))
_WtSeriFtpAutoFtp_Type.__name__=_C
_WtSeriFtpAutoFtp_Object=MibTableColumn
wtSeriFtpAutoFtp=_WtSeriFtpAutoFtp_Object((1,3,6,1,4,1,5040,1,1,1,3,8,1,3),_WtSeriFtpAutoFtp_Type())
wtSeriFtpAutoFtp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriFtpAutoFtp.setStatus(_A)
_WtSeriFtpLoginString_Type=OctetString
_WtSeriFtpLoginString_Object=MibTableColumn
wtSeriFtpLoginString=_WtSeriFtpLoginString_Object((1,3,6,1,4,1,5040,1,1,1,3,8,1,4),_WtSeriFtpLoginString_Type())
wtSeriFtpLoginString.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriFtpLoginString.setStatus(_A)
class _WtSeriFtpInactTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriFtpInactTimeout_Type.__name__=_C
_WtSeriFtpInactTimeout_Object=MibTableColumn
wtSeriFtpInactTimeout=_WtSeriFtpInactTimeout_Object((1,3,6,1,4,1,5040,1,1,1,3,8,1,5),_WtSeriFtpInactTimeout_Type())
wtSeriFtpInactTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriFtpInactTimeout.setStatus(_A)
class _WtSeriFtpConnectTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtSeriFtpConnectTimeout_Type.__name__=_C
_WtSeriFtpConnectTimeout_Object=MibTableColumn
wtSeriFtpConnectTimeout=_WtSeriFtpConnectTimeout_Object((1,3,6,1,4,1,5040,1,1,1,3,8,1,6),_WtSeriFtpConnectTimeout_Type())
wtSeriFtpConnectTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriFtpConnectTimeout.setStatus(_A)
class _WtSeriFtpProtocolChar_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_WtSeriFtpProtocolChar_Type.__name__=_D
_WtSeriFtpProtocolChar_Object=MibTableColumn
wtSeriFtpProtocolChar=_WtSeriFtpProtocolChar_Object((1,3,6,1,4,1,5040,1,1,1,3,8,1,7),_WtSeriFtpProtocolChar_Type())
wtSeriFtpProtocolChar.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriFtpProtocolChar.setStatus(_A)
_WtSeriFtpServerUrl_Type=OctetString
_WtSeriFtpServerUrl_Object=MibTableColumn
wtSeriFtpServerUrl=_WtSeriFtpServerUrl_Object((1,3,6,1,4,1,5040,1,1,1,3,8,1,8),_WtSeriFtpServerUrl_Type())
wtSeriFtpServerUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriFtpServerUrl.setStatus(_A)
_WtSeriMultiPortPrtTable_Object=MibTable
wtSeriMultiPortPrtTable=_WtSeriMultiPortPrtTable_Object((1,3,6,1,4,1,5040,1,1,1,3,9))
if mibBuilder.loadTexts:wtSeriMultiPortPrtTable.setStatus(_A)
_WtSeriMultiPortPrtEntry_Object=MibTableRow
wtSeriMultiPortPrtEntry=_WtSeriMultiPortPrtEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,9,1))
wtSeriMultiPortPrtEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriMultiPortPrtEntry.setStatus(_A)
class _WtSeriPrtSeriProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriPrtSeriProtocolOff',1),('wtSeriPrtSeriProtocolOn',2)))
_WtSeriPrtSeriProtocol_Type.__name__=_C
_WtSeriPrtSeriProtocol_Object=MibTableColumn
wtSeriPrtSeriProtocol=_WtSeriPrtSeriProtocol_Object((1,3,6,1,4,1,5040,1,1,1,3,9,1,1),_WtSeriPrtSeriProtocol_Type())
wtSeriPrtSeriProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriPrtSeriProtocol.setStatus(_A)
class _WtSeriPrtSeriCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriPrtSeriCodingOff',1),('wtSeriPrtSeriCodingOn',2)))
_WtSeriPrtSeriCoding_Type.__name__=_C
_WtSeriPrtSeriCoding_Object=MibTableColumn
wtSeriPrtSeriCoding=_WtSeriPrtSeriCoding_Object((1,3,6,1,4,1,5040,1,1,1,3,9,1,2),_WtSeriPrtSeriCoding_Type())
wtSeriPrtSeriCoding.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriPrtSeriCoding.setStatus(_A)
class _WtSeriPrtProtocolChar_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_WtSeriPrtProtocolChar_Type.__name__=_D
_WtSeriPrtProtocolChar_Object=MibTableColumn
wtSeriPrtProtocolChar=_WtSeriPrtProtocolChar_Object((1,3,6,1,4,1,5040,1,1,1,3,9,1,3),_WtSeriPrtProtocolChar_Type())
wtSeriPrtProtocolChar.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriPrtProtocolChar.setStatus(_A)
_WtSeriB2bMasterTable_Object=MibTable
wtSeriB2bMasterTable=_WtSeriB2bMasterTable_Object((1,3,6,1,4,1,5040,1,1,1,3,10))
if mibBuilder.loadTexts:wtSeriB2bMasterTable.setStatus(_A)
_WtSeriB2bMasterEntry_Object=MibTableRow
wtSeriB2bMasterEntry=_WtSeriB2bMasterEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,10,1))
wtSeriB2bMasterEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriB2bMasterEntry.setStatus(_A)
class _WtSeriB2bMaster_SlavePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtSeriB2bMaster_SlavePort_Type.__name__=_C
_WtSeriB2bMaster_SlavePort_Object=MibTableColumn
wtSeriB2bMaster_SlavePort=_WtSeriB2bMaster_SlavePort_Object((1,3,6,1,4,1,5040,1,1,1,3,10,1,1),_WtSeriB2bMaster_SlavePort_Type())
wtSeriB2bMaster_SlavePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriB2bMaster_SlavePort.setStatus(_A)
_WtSeriB2bMaster_SlaveIp_Type=IpAddress
_WtSeriB2bMaster_SlaveIp_Object=MibTableColumn
wtSeriB2bMaster_SlaveIp=_WtSeriB2bMaster_SlaveIp_Object((1,3,6,1,4,1,5040,1,1,1,3,10,1,2),_WtSeriB2bMaster_SlaveIp_Type())
wtSeriB2bMaster_SlaveIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriB2bMaster_SlaveIp.setStatus(_A)
class _WtSeriB2bMaster_DispString1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtSeriB2bMaster_DispString1_Type.__name__=_D
_WtSeriB2bMaster_DispString1_Object=MibTableColumn
wtSeriB2bMaster_DispString1=_WtSeriB2bMaster_DispString1_Object((1,3,6,1,4,1,5040,1,1,1,3,10,1,3),_WtSeriB2bMaster_DispString1_Type())
wtSeriB2bMaster_DispString1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriB2bMaster_DispString1.setStatus(_A)
class _WtSeriB2bMaster_DispString2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtSeriB2bMaster_DispString2_Type.__name__=_D
_WtSeriB2bMaster_DispString2_Object=MibTableColumn
wtSeriB2bMaster_DispString2=_WtSeriB2bMaster_DispString2_Object((1,3,6,1,4,1,5040,1,1,1,3,10,1,4),_WtSeriB2bMaster_DispString2_Type())
wtSeriB2bMaster_DispString2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriB2bMaster_DispString2.setStatus(_A)
_WtSeriB2bSlaveTable_Object=MibTable
wtSeriB2bSlaveTable=_WtSeriB2bSlaveTable_Object((1,3,6,1,4,1,5040,1,1,1,3,11))
if mibBuilder.loadTexts:wtSeriB2bSlaveTable.setStatus(_A)
_WtSeriB2bSlaveEntry_Object=MibTableRow
wtSeriB2bSlaveEntry=_WtSeriB2bSlaveEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,11,1))
wtSeriB2bSlaveEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriB2bSlaveEntry.setStatus(_A)
class _WtSeriB2bSlave_MasterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtSeriB2bSlave_MasterPort_Type.__name__=_C
_WtSeriB2bSlave_MasterPort_Object=MibTableColumn
wtSeriB2bSlave_MasterPort=_WtSeriB2bSlave_MasterPort_Object((1,3,6,1,4,1,5040,1,1,1,3,11,1,1),_WtSeriB2bSlave_MasterPort_Type())
wtSeriB2bSlave_MasterPort.setMaxAccess(_F)
if mibBuilder.loadTexts:wtSeriB2bSlave_MasterPort.setStatus(_A)
_WtSeriB2bSlave_MasterIp_Type=IpAddress
_WtSeriB2bSlave_MasterIp_Object=MibTableColumn
wtSeriB2bSlave_MasterIp=_WtSeriB2bSlave_MasterIp_Object((1,3,6,1,4,1,5040,1,1,1,3,11,1,2),_WtSeriB2bSlave_MasterIp_Type())
wtSeriB2bSlave_MasterIp.setMaxAccess(_F)
if mibBuilder.loadTexts:wtSeriB2bSlave_MasterIp.setStatus(_A)
class _WtSeriB2bSlave_DispString1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtSeriB2bSlave_DispString1_Type.__name__=_D
_WtSeriB2bSlave_DispString1_Object=MibTableColumn
wtSeriB2bSlave_DispString1=_WtSeriB2bSlave_DispString1_Object((1,3,6,1,4,1,5040,1,1,1,3,11,1,3),_WtSeriB2bSlave_DispString1_Type())
wtSeriB2bSlave_DispString1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriB2bSlave_DispString1.setStatus(_A)
class _WtSeriB2bSlave_DispString2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtSeriB2bSlave_DispString2_Type.__name__=_D
_WtSeriB2bSlave_DispString2_Object=MibTableColumn
wtSeriB2bSlave_DispString2=_WtSeriB2bSlave_DispString2_Object((1,3,6,1,4,1,5040,1,1,1,3,11,1,4),_WtSeriB2bSlave_DispString2_Type())
wtSeriB2bSlave_DispString2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriB2bSlave_DispString2.setStatus(_A)
_WtSeriIpBusTable_Object=MibTable
wtSeriIpBusTable=_WtSeriIpBusTable_Object((1,3,6,1,4,1,5040,1,1,1,3,12))
if mibBuilder.loadTexts:wtSeriIpBusTable.setStatus(_A)
_WtSeriIpBusEntry_Object=MibTableRow
wtSeriIpBusEntry=_WtSeriIpBusEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,12,1))
wtSeriIpBusEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriIpBusEntry.setStatus(_A)
_WtSeriBusSlave_MasterIp_Type=IpAddress
_WtSeriBusSlave_MasterIp_Object=MibTableColumn
wtSeriBusSlave_MasterIp=_WtSeriBusSlave_MasterIp_Object((1,3,6,1,4,1,5040,1,1,1,3,12,1,1),_WtSeriBusSlave_MasterIp_Type())
wtSeriBusSlave_MasterIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriBusSlave_MasterIp.setStatus(_A)
_WtSeriBusMaster_SubnetIp_Type=IpAddress
_WtSeriBusMaster_SubnetIp_Object=MibTableColumn
wtSeriBusMaster_SubnetIp=_WtSeriBusMaster_SubnetIp_Object((1,3,6,1,4,1,5040,1,1,1,3,12,1,2),_WtSeriBusMaster_SubnetIp_Type())
wtSeriBusMaster_SubnetIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriBusMaster_SubnetIp.setStatus(_A)
_WtSeriSlipTable_Object=MibTable
wtSeriSlipTable=_WtSeriSlipTable_Object((1,3,6,1,4,1,5040,1,1,1,3,13))
if mibBuilder.loadTexts:wtSeriSlipTable.setStatus(_A)
_WtSeriSlipEntry_Object=MibTableRow
wtSeriSlipEntry=_WtSeriSlipEntry_Object((1,3,6,1,4,1,5040,1,1,1,3,13,1))
wtSeriSlipEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wtSeriSlipEntry.setStatus(_A)
_WtSeriSlipNetAddress_Type=IpAddress
_WtSeriSlipNetAddress_Object=MibTableColumn
wtSeriSlipNetAddress=_WtSeriSlipNetAddress_Object((1,3,6,1,4,1,5040,1,1,1,3,13,1,1),_WtSeriSlipNetAddress_Type())
wtSeriSlipNetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriSlipNetAddress.setStatus(_A)
class _WtSeriSlipNetRouting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtSeriSlipNetRoutingOff',1),('wtSeriSlipNetRoutingOn',2)))
_WtSeriSlipNetRouting_Type.__name__=_C
_WtSeriSlipNetRouting_Object=MibTableColumn
wtSeriSlipNetRouting=_WtSeriSlipNetRouting_Object((1,3,6,1,4,1,5040,1,1,1,3,13,1,2),_WtSeriSlipNetRouting_Type())
wtSeriSlipNetRouting.setMaxAccess(_B)
if mibBuilder.loadTexts:wtSeriSlipNetRouting.setStatus(_A)
_WtDeaPortSetup_ObjectIdentity=ObjectIdentity
wtDeaPortSetup=_WtDeaPortSetup_ObjectIdentity((1,3,6,1,4,1,5040,1,1,1,4))
class _WtDeaPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WtDeaPorts_Type.__name__=_C
_WtDeaPorts_Object=MibScalar
wtDeaPorts=_WtDeaPorts_Object((1,3,6,1,4,1,5040,1,1,1,4,1),_WtDeaPorts_Type())
wtDeaPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:wtDeaPorts.setStatus(_A)
_WtDeaInterfaceTable_Object=MibTable
wtDeaInterfaceTable=_WtDeaInterfaceTable_Object((1,3,6,1,4,1,5040,1,1,1,4,2))
if mibBuilder.loadTexts:wtDeaInterfaceTable.setStatus(_A)
_WtDeaInterfaceEntry_Object=MibTableRow
wtDeaInterfaceEntry=_WtDeaInterfaceEntry_Object((1,3,6,1,4,1,5040,1,1,1,4,2,1))
wtDeaInterfaceEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wtDeaInterfaceEntry.setStatus(_A)
class _WtDeaInterfaceNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WtDeaInterfaceNo_Type.__name__=_C
_WtDeaInterfaceNo_Object=MibTableColumn
wtDeaInterfaceNo=_WtDeaInterfaceNo_Object((1,3,6,1,4,1,5040,1,1,1,4,2,1,1),_WtDeaInterfaceNo_Type())
wtDeaInterfaceNo.setMaxAccess(_F)
if mibBuilder.loadTexts:wtDeaInterfaceNo.setStatus(_A)
_WtDeaPortTable_Object=MibTable
wtDeaPortTable=_WtDeaPortTable_Object((1,3,6,1,4,1,5040,1,1,1,4,3))
if mibBuilder.loadTexts:wtDeaPortTable.setStatus(_A)
_WtDeaPortEntry_Object=MibTableRow
wtDeaPortEntry=_WtDeaPortEntry_Object((1,3,6,1,4,1,5040,1,1,1,4,3,1))
wtDeaPortEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wtDeaPortEntry.setStatus(_A)
class _WtDeaLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(49152,65535))
_WtDeaLocalPort_Type.__name__=_C
_WtDeaLocalPort_Object=MibTableColumn
wtDeaLocalPort=_WtDeaLocalPort_Object((1,3,6,1,4,1,5040,1,1,1,4,3,1,1),_WtDeaLocalPort_Type())
wtDeaLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaLocalPort.setStatus(_A)
class _WtDeaPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('wtDeaServerMode',1),('wtDeaTcpClient',2),('wtDeaBox2BoxMaster',3),('wtDeaUdpMode',4),('wtDeaSnmpAgent',5),('wtDeaBox2BoxSlave',6)))
_WtDeaPortMode_Type.__name__=_C
_WtDeaPortMode_Object=MibTableColumn
wtDeaPortMode=_WtDeaPortMode_Object((1,3,6,1,4,1,5040,1,1,1,4,3,1,2),_WtDeaPortMode_Type())
wtDeaPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaPortMode.setStatus(_A)
_WtDeaDrvWatchdog_Type=Integer32
_WtDeaDrvWatchdog_Object=MibTableColumn
wtDeaDrvWatchdog=_WtDeaDrvWatchdog_Object((1,3,6,1,4,1,5040,1,1,1,4,3,1,3),_WtDeaDrvWatchdog_Type())
wtDeaDrvWatchdog.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaDrvWatchdog.setStatus(_A)
_WtDeaTcpClientTable_Object=MibTable
wtDeaTcpClientTable=_WtDeaTcpClientTable_Object((1,3,6,1,4,1,5040,1,1,1,4,4))
if mibBuilder.loadTexts:wtDeaTcpClientTable.setStatus(_A)
_WtDeaTcpClientEntry_Object=MibTableRow
wtDeaTcpClientEntry=_WtDeaTcpClientEntry_Object((1,3,6,1,4,1,5040,1,1,1,4,4,1))
wtDeaTcpClientEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wtDeaTcpClientEntry.setStatus(_A)
class _WtDeaTcpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaTcpServerPort_Type.__name__=_C
_WtDeaTcpServerPort_Object=MibTableColumn
wtDeaTcpServerPort=_WtDeaTcpServerPort_Object((1,3,6,1,4,1,5040,1,1,1,4,4,1,1),_WtDeaTcpServerPort_Type())
wtDeaTcpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaTcpServerPort.setStatus(_A)
_WtDeaTcpServerIp_Type=IpAddress
_WtDeaTcpServerIp_Object=MibTableColumn
wtDeaTcpServerIp=_WtDeaTcpServerIp_Object((1,3,6,1,4,1,5040,1,1,1,4,4,1,2),_WtDeaTcpServerIp_Type())
wtDeaTcpServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaTcpServerIp.setStatus(_A)
class _WtDeaTcpInactTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaTcpInactTimeout_Type.__name__=_C
_WtDeaTcpInactTimeout_Object=MibTableColumn
wtDeaTcpInactTimeout=_WtDeaTcpInactTimeout_Object((1,3,6,1,4,1,5040,1,1,1,4,4,1,3),_WtDeaTcpInactTimeout_Type())
wtDeaTcpInactTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaTcpInactTimeout.setStatus(_A)
class _WtDeaTcpConnectTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaTcpConnectTimeout_Type.__name__=_C
_WtDeaTcpConnectTimeout_Object=MibTableColumn
wtDeaTcpConnectTimeout=_WtDeaTcpConnectTimeout_Object((1,3,6,1,4,1,5040,1,1,1,4,4,1,4),_WtDeaTcpConnectTimeout_Type())
wtDeaTcpConnectTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaTcpConnectTimeout.setStatus(_A)
class _WtDeaTcpInputMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtDeaTcpInputMask_Type.__name__=_D
_WtDeaTcpInputMask_Object=MibTableColumn
wtDeaTcpInputMask=_WtDeaTcpInputMask_Object((1,3,6,1,4,1,5040,1,1,1,4,4,1,5),_WtDeaTcpInputMask_Type())
wtDeaTcpInputMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaTcpInputMask.setStatus(_A)
_WtDeaUdpClientTable_Object=MibTable
wtDeaUdpClientTable=_WtDeaUdpClientTable_Object((1,3,6,1,4,1,5040,1,1,1,4,5))
if mibBuilder.loadTexts:wtDeaUdpClientTable.setStatus(_A)
_WtDeaUdpClientEntry_Object=MibTableRow
wtDeaUdpClientEntry=_WtDeaUdpClientEntry_Object((1,3,6,1,4,1,5040,1,1,1,4,5,1))
wtDeaUdpClientEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wtDeaUdpClientEntry.setStatus(_A)
class _WtDeaUdpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaUdpServerPort_Type.__name__=_C
_WtDeaUdpServerPort_Object=MibTableColumn
wtDeaUdpServerPort=_WtDeaUdpServerPort_Object((1,3,6,1,4,1,5040,1,1,1,4,5,1,1),_WtDeaUdpServerPort_Type())
wtDeaUdpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaUdpServerPort.setStatus(_A)
_WtDeaUdpServerIp_Type=IpAddress
_WtDeaUdpServerIp_Object=MibTableColumn
wtDeaUdpServerIp=_WtDeaUdpServerIp_Object((1,3,6,1,4,1,5040,1,1,1,4,5,1,2),_WtDeaUdpServerIp_Type())
wtDeaUdpServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaUdpServerIp.setStatus(_A)
class _WtDeaUdpPacketProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wtDeaUdpPacketProtocolOff',1),('wtDeaUdpPacketProtocolOn',2)))
_WtDeaUdpPacketProtocol_Type.__name__=_C
_WtDeaUdpPacketProtocol_Object=MibTableColumn
wtDeaUdpPacketProtocol=_WtDeaUdpPacketProtocol_Object((1,3,6,1,4,1,5040,1,1,1,4,5,1,3),_WtDeaUdpPacketProtocol_Type())
wtDeaUdpPacketProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaUdpPacketProtocol.setStatus(_A)
class _WtDeaUdpInputMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtDeaUdpInputMask_Type.__name__=_D
_WtDeaUdpInputMask_Object=MibTableColumn
wtDeaUdpInputMask=_WtDeaUdpInputMask_Object((1,3,6,1,4,1,5040,1,1,1,4,5,1,4),_WtDeaUdpInputMask_Type())
wtDeaUdpInputMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaUdpInputMask.setStatus(_A)
class _WtDeaUdpSendInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaUdpSendInterval_Type.__name__=_C
_WtDeaUdpSendInterval_Object=MibTableColumn
wtDeaUdpSendInterval=_WtDeaUdpSendInterval_Object((1,3,6,1,4,1,5040,1,1,1,4,5,1,5),_WtDeaUdpSendInterval_Type())
wtDeaUdpSendInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaUdpSendInterval.setStatus(_A)
_WtDeaSnmpAgentTable_Object=MibTable
wtDeaSnmpAgentTable=_WtDeaSnmpAgentTable_Object((1,3,6,1,4,1,5040,1,1,1,4,6))
if mibBuilder.loadTexts:wtDeaSnmpAgentTable.setStatus(_A)
_WtDeaSnmpAgentEntry_Object=MibTableRow
wtDeaSnmpAgentEntry=_WtDeaSnmpAgentEntry_Object((1,3,6,1,4,1,5040,1,1,1,4,6,1))
wtDeaSnmpAgentEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wtDeaSnmpAgentEntry.setStatus(_A)
_WtDeaSnmpManagerIp_Type=IpAddress
_WtDeaSnmpManagerIp_Object=MibTableColumn
wtDeaSnmpManagerIp=_WtDeaSnmpManagerIp_Object((1,3,6,1,4,1,5040,1,1,1,4,6,1,1),_WtDeaSnmpManagerIp_Type())
wtDeaSnmpManagerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaSnmpManagerIp.setStatus(_A)
class _WtDeaSnmpInputMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtDeaSnmpInputMask_Type.__name__=_D
_WtDeaSnmpInputMask_Object=MibTableColumn
wtDeaSnmpInputMask=_WtDeaSnmpInputMask_Object((1,3,6,1,4,1,5040,1,1,1,4,6,1,2),_WtDeaSnmpInputMask_Type())
wtDeaSnmpInputMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaSnmpInputMask.setStatus(_A)
class _WtDeaSnmpSendInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaSnmpSendInterval_Type.__name__=_C
_WtDeaSnmpSendInterval_Object=MibTableColumn
wtDeaSnmpSendInterval=_WtDeaSnmpSendInterval_Object((1,3,6,1,4,1,5040,1,1,1,4,6,1,3),_WtDeaSnmpSendInterval_Type())
wtDeaSnmpSendInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaSnmpSendInterval.setStatus(_A)
_WtDeaB2bMasterTable_Object=MibTable
wtDeaB2bMasterTable=_WtDeaB2bMasterTable_Object((1,3,6,1,4,1,5040,1,1,1,4,7))
if mibBuilder.loadTexts:wtDeaB2bMasterTable.setStatus(_A)
_WtDeaB2bMasterEntry_Object=MibTableRow
wtDeaB2bMasterEntry=_WtDeaB2bMasterEntry_Object((1,3,6,1,4,1,5040,1,1,1,4,7,1))
wtDeaB2bMasterEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wtDeaB2bMasterEntry.setStatus(_A)
class _WtDeaB2bMaster_SlavePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaB2bMaster_SlavePort_Type.__name__=_C
_WtDeaB2bMaster_SlavePort_Object=MibTableColumn
wtDeaB2bMaster_SlavePort=_WtDeaB2bMaster_SlavePort_Object((1,3,6,1,4,1,5040,1,1,1,4,7,1,1),_WtDeaB2bMaster_SlavePort_Type())
wtDeaB2bMaster_SlavePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaB2bMaster_SlavePort.setStatus(_A)
_WtDeaB2bMaster_SlaveIp_Type=IpAddress
_WtDeaB2bMaster_SlaveIp_Object=MibTableColumn
wtDeaB2bMaster_SlaveIp=_WtDeaB2bMaster_SlaveIp_Object((1,3,6,1,4,1,5040,1,1,1,4,7,1,2),_WtDeaB2bMaster_SlaveIp_Type())
wtDeaB2bMaster_SlaveIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaB2bMaster_SlaveIp.setStatus(_A)
class _WtDeaB2bMaster_InputMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtDeaB2bMaster_InputMask_Type.__name__=_D
_WtDeaB2bMaster_InputMask_Object=MibTableColumn
wtDeaB2bMaster_InputMask=_WtDeaB2bMaster_InputMask_Object((1,3,6,1,4,1,5040,1,1,1,4,7,1,3),_WtDeaB2bMaster_InputMask_Type())
wtDeaB2bMaster_InputMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaB2bMaster_InputMask.setStatus(_A)
class _WtDeaB2bMaster_SendInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaB2bMaster_SendInterval_Type.__name__=_C
_WtDeaB2bMaster_SendInterval_Object=MibTableColumn
wtDeaB2bMaster_SendInterval=_WtDeaB2bMaster_SendInterval_Object((1,3,6,1,4,1,5040,1,1,1,4,7,1,4),_WtDeaB2bMaster_SendInterval_Type())
wtDeaB2bMaster_SendInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaB2bMaster_SendInterval.setStatus(_A)
_WtDeaB2bSlaveTable_Object=MibTable
wtDeaB2bSlaveTable=_WtDeaB2bSlaveTable_Object((1,3,6,1,4,1,5040,1,1,1,4,8))
if mibBuilder.loadTexts:wtDeaB2bSlaveTable.setStatus(_A)
_WtDeaB2bSlaveEntry_Object=MibTableRow
wtDeaB2bSlaveEntry=_WtDeaB2bSlaveEntry_Object((1,3,6,1,4,1,5040,1,1,1,4,8,1))
wtDeaB2bSlaveEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wtDeaB2bSlaveEntry.setStatus(_A)
class _WtDeaB2bSlave_MasterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaB2bSlave_MasterPort_Type.__name__=_C
_WtDeaB2bSlave_MasterPort_Object=MibTableColumn
wtDeaB2bSlave_MasterPort=_WtDeaB2bSlave_MasterPort_Object((1,3,6,1,4,1,5040,1,1,1,4,8,1,1),_WtDeaB2bSlave_MasterPort_Type())
wtDeaB2bSlave_MasterPort.setMaxAccess(_F)
if mibBuilder.loadTexts:wtDeaB2bSlave_MasterPort.setStatus(_A)
_WtDeaB2bSlave_MasterIp_Type=IpAddress
_WtDeaB2bSlave_MasterIp_Object=MibTableColumn
wtDeaB2bSlave_MasterIp=_WtDeaB2bSlave_MasterIp_Object((1,3,6,1,4,1,5040,1,1,1,4,8,1,2),_WtDeaB2bSlave_MasterIp_Type())
wtDeaB2bSlave_MasterIp.setMaxAccess(_F)
if mibBuilder.loadTexts:wtDeaB2bSlave_MasterIp.setStatus(_A)
class _WtDeaB2bSlave_InputMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtDeaB2bSlave_InputMask_Type.__name__=_D
_WtDeaB2bSlave_InputMask_Object=MibTableColumn
wtDeaB2bSlave_InputMask=_WtDeaB2bSlave_InputMask_Object((1,3,6,1,4,1,5040,1,1,1,4,8,1,3),_WtDeaB2bSlave_InputMask_Type())
wtDeaB2bSlave_InputMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaB2bSlave_InputMask.setStatus(_A)
class _WtDeaB2bSlave_SendInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaB2bSlave_SendInterval_Type.__name__=_C
_WtDeaB2bSlave_SendInterval_Object=MibTableColumn
wtDeaB2bSlave_SendInterval=_WtDeaB2bSlave_SendInterval_Object((1,3,6,1,4,1,5040,1,1,1,4,8,1,4),_WtDeaB2bSlave_SendInterval_Type())
wtDeaB2bSlave_SendInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaB2bSlave_SendInterval.setStatus(_A)
_WtDeaDriver_ObjectIdentity=ObjectIdentity
wtDeaDriver=_WtDeaDriver_ObjectIdentity((1,3,6,1,4,1,5040,1,1,2))
_WtDeaDrvTable_Object=MibTable
wtDeaDrvTable=_WtDeaDrvTable_Object((1,3,6,1,4,1,5040,1,1,2,1))
if mibBuilder.loadTexts:wtDeaDrvTable.setStatus(_A)
_WtDeaDrvEntry_Object=MibTableRow
wtDeaDrvEntry=_WtDeaDrvEntry_Object((1,3,6,1,4,1,5040,1,1,2,1,1))
wtDeaDrvEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:wtDeaDrvEntry.setStatus(_A)
class _WtDeaDrvInterfaceNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WtDeaDrvInterfaceNo_Type.__name__=_C
_WtDeaDrvInterfaceNo_Object=MibTableColumn
wtDeaDrvInterfaceNo=_WtDeaDrvInterfaceNo_Object((1,3,6,1,4,1,5040,1,1,2,1,1,1),_WtDeaDrvInterfaceNo_Type())
wtDeaDrvInterfaceNo.setMaxAccess(_F)
if mibBuilder.loadTexts:wtDeaDrvInterfaceNo.setStatus(_A)
class _WtDeaDrvInputRegister_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtDeaDrvInputRegister_Type.__name__=_D
_WtDeaDrvInputRegister_Object=MibTableColumn
wtDeaDrvInputRegister=_WtDeaDrvInputRegister_Object((1,3,6,1,4,1,5040,1,1,2,1,1,2),_WtDeaDrvInputRegister_Type())
wtDeaDrvInputRegister.setMaxAccess(_F)
if mibBuilder.loadTexts:wtDeaDrvInputRegister.setStatus(_A)
class _WtDeaDrvOutputRegister_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtDeaDrvOutputRegister_Type.__name__=_D
_WtDeaDrvOutputRegister_Object=MibTableColumn
wtDeaDrvOutputRegister=_WtDeaDrvOutputRegister_Object((1,3,6,1,4,1,5040,1,1,2,1,1,3),_WtDeaDrvOutputRegister_Type())
wtDeaDrvOutputRegister.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaDrvOutputRegister.setStatus(_A)
class _WtDeaDrvSetBit_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtDeaDrvSetBit_Type.__name__=_D
_WtDeaDrvSetBit_Object=MibTableColumn
wtDeaDrvSetBit=_WtDeaDrvSetBit_Object((1,3,6,1,4,1,5040,1,1,2,1,1,4),_WtDeaDrvSetBit_Type())
wtDeaDrvSetBit.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaDrvSetBit.setStatus(_A)
class _WtDeaDrvTrapInputMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_WtDeaDrvTrapInputMask_Type.__name__=_D
_WtDeaDrvTrapInputMask_Object=MibTableColumn
wtDeaDrvTrapInputMask=_WtDeaDrvTrapInputMask_Object((1,3,6,1,4,1,5040,1,1,2,1,1,5),_WtDeaDrvTrapInputMask_Type())
wtDeaDrvTrapInputMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaDrvTrapInputMask.setStatus(_A)
class _WtDeaDrvTrapInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtDeaDrvTrapInterval_Type.__name__=_C
_WtDeaDrvTrapInterval_Object=MibTableColumn
wtDeaDrvTrapInterval=_WtDeaDrvTrapInterval_Object((1,3,6,1,4,1,5040,1,1,2,1,1,6),_WtDeaDrvTrapInterval_Type())
wtDeaDrvTrapInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtDeaDrvTrapInterval.setStatus(_A)
deaInputChangedAlert=NotificationType((1,3,6,1,4,1,5040,1,1,2,1,1,0,1))
deaInputChangedAlert.setObjects((_E,_I))
if mibBuilder.loadTexts:deaInputChangedAlert.setStatus('')
deaIntervalExpiredAlert=NotificationType((1,3,6,1,4,1,5040,1,1,2,1,1,0,2))
deaIntervalExpiredAlert.setObjects((_E,_I))
if mibBuilder.loadTexts:deaIntervalExpiredAlert.setStatus('')
mibBuilder.exportSymbols(_E,**{'wut':wut,'wtComServer':wtComServer,'wtComServerIntern':wtComServerIntern,'wtConfiguration':wtConfiguration,'wtSystem':wtSystem,'wtCableType':wtCableType,'wtMacAddress':wtMacAddress,'wtSwDate':wtSwDate,'wtSwRev':wtSwRev,'wtDevType':wtDevType,'wtMibRev':wtMibRev,'wtRunTime':wtRunTime,'wtPhysPorts':wtPhysPorts,'wtConfigMode':wtConfigMode,'wtPassword':wtPassword,'wtSysPswd':wtSysPswd,'wtSysName':wtSysName,'wtNetSetup':wtNetSetup,'wtIpAddress':wtIpAddress,'wtSubnetMask':wtSubnetMask,'wtGateway':wtGateway,'wtMtu':wtMtu,'wtBootpClient':wtBootpClient,'wtKeepAlive':wtKeepAlive,'wtRetransmTimeout':wtRetransmTimeout,'wtDhcpClient':wtDhcpClient,'wtWbmPort':wtWbmPort,'wtDnsSrv':wtDnsSrv,'wtLinkSpeed':wtLinkSpeed,'wtSeriPortSetup':wtSeriPortSetup,'wtSerialPorts':wtSerialPorts,'wtSeriInterfaceTable':wtSeriInterfaceTable,'wtSeriInterfaceEntry':wtSeriInterfaceEntry,_G:wtSeriInterfaceNo,'wtSeriUartTable':wtSeriUartTable,'wtSeriUartEntry':wtSeriUartEntry,'wtBaudrate':wtBaudrate,'wtParity':wtParity,'wtDatabits':wtDatabits,'wtStopbits':wtStopbits,'wtHsLines':wtHsLines,'wtHsFunctions':wtHsFunctions,'wtUartFifo':wtUartFifo,'wtUartBaudrate':wtUartBaudrate,'wtBaudDivisor':wtBaudDivisor,'wtSeriInQueue':wtSeriInQueue,'wtSeriPortTable':wtSeriPortTable,'wtSeriPortEntry':wtSeriPortEntry,'wtSeriLocalPort':wtSeriLocalPort,'wtSeriPortMode':wtSeriPortMode,'wtSeriControlPort':wtSeriControlPort,'wtSeriPortState':wtSeriPortState,'wtSeriRemotePort':wtSeriRemotePort,'wtSeriRemoteIP':wtSeriRemoteIP,'wtSeriNetPckDelay':wtSeriNetPckDelay,'wtSeriFlushBuf':wtSeriFlushBuf,'wtSeriTelnetEcho':wtSeriTelnetEcho,'wtSeriTcpClientTable':wtSeriTcpClientTable,'wtSeriTcpClientEntry':wtSeriTcpClientEntry,'wtSeriTcpServerPort':wtSeriTcpServerPort,'wtSeriTcpServerIp':wtSeriTcpServerIp,'wtSeriTcpInactTimeout':wtSeriTcpInactTimeout,'wtSeriTcpConnectTimeout':wtSeriTcpConnectTimeout,'wtSeriTcpDisconnectChar':wtSeriTcpDisconnectChar,'wtSeriTcpDispString1':wtSeriTcpDispString1,'wtSeriTcpDispString2':wtSeriTcpDispString2,'wtSeriTcpCAddress':wtSeriTcpCAddress,'wtSeriTcpResponseMode':wtSeriTcpResponseMode,'wtSeriTcpServerUrl':wtSeriTcpServerUrl,'wtSeriUdpClientTable':wtSeriUdpClientTable,'wtSeriUdpClientEntry':wtSeriUdpClientEntry,'wtSeriUdpServerPort':wtSeriUdpServerPort,'wtSeriUdpServerIp':wtSeriUdpServerIp,'wtSeriUdpDispString1':wtSeriUdpDispString1,'wtSeriUdpDispString2':wtSeriUdpDispString2,'wtSeriUdpSeriProtocol':wtSeriUdpSeriProtocol,'wtSeriUdpSeriCoding':wtSeriUdpSeriCoding,'wtSeriUdpCAddress':wtSeriUdpCAddress,'wtSeriUdpWrCAddress':wtSeriUdpWrCAddress,'wtSeriUdpDisconnectChar':wtSeriUdpDisconnectChar,'wtSeriUdpServerUrl':wtSeriUdpServerUrl,'wtSeriTelnetClientTable':wtSeriTelnetClientTable,'wtSeriTelnetClientEntry':wtSeriTelnetClientEntry,'wtSeriTelnetServerPort':wtSeriTelnetServerPort,'wtSeriTelnetServerIp':wtSeriTelnetServerIp,'wtSeriTelnetInactTimeout':wtSeriTelnetInactTimeout,'wtSeriTelnetDisconnectChar':wtSeriTelnetDisconnectChar,'wtSeriTelnetChangeLineout':wtSeriTelnetChangeLineout,'wtSeriTelnetServerUrl':wtSeriTelnetServerUrl,'wtSeriFtpClientTable':wtSeriFtpClientTable,'wtSeriFtpClientEntry':wtSeriFtpClientEntry,'wtSeriFtpServerPort':wtSeriFtpServerPort,'wtSeriFtpServerIp':wtSeriFtpServerIp,'wtSeriFtpAutoFtp':wtSeriFtpAutoFtp,'wtSeriFtpLoginString':wtSeriFtpLoginString,'wtSeriFtpInactTimeout':wtSeriFtpInactTimeout,'wtSeriFtpConnectTimeout':wtSeriFtpConnectTimeout,'wtSeriFtpProtocolChar':wtSeriFtpProtocolChar,'wtSeriFtpServerUrl':wtSeriFtpServerUrl,'wtSeriMultiPortPrtTable':wtSeriMultiPortPrtTable,'wtSeriMultiPortPrtEntry':wtSeriMultiPortPrtEntry,'wtSeriPrtSeriProtocol':wtSeriPrtSeriProtocol,'wtSeriPrtSeriCoding':wtSeriPrtSeriCoding,'wtSeriPrtProtocolChar':wtSeriPrtProtocolChar,'wtSeriB2bMasterTable':wtSeriB2bMasterTable,'wtSeriB2bMasterEntry':wtSeriB2bMasterEntry,'wtSeriB2bMaster-SlavePort':wtSeriB2bMaster_SlavePort,'wtSeriB2bMaster-SlaveIp':wtSeriB2bMaster_SlaveIp,'wtSeriB2bMaster-DispString1':wtSeriB2bMaster_DispString1,'wtSeriB2bMaster-DispString2':wtSeriB2bMaster_DispString2,'wtSeriB2bSlaveTable':wtSeriB2bSlaveTable,'wtSeriB2bSlaveEntry':wtSeriB2bSlaveEntry,'wtSeriB2bSlave-MasterPort':wtSeriB2bSlave_MasterPort,'wtSeriB2bSlave-MasterIp':wtSeriB2bSlave_MasterIp,'wtSeriB2bSlave-DispString1':wtSeriB2bSlave_DispString1,'wtSeriB2bSlave-DispString2':wtSeriB2bSlave_DispString2,'wtSeriIpBusTable':wtSeriIpBusTable,'wtSeriIpBusEntry':wtSeriIpBusEntry,'wtSeriBusSlave-MasterIp':wtSeriBusSlave_MasterIp,'wtSeriBusMaster-SubnetIp':wtSeriBusMaster_SubnetIp,'wtSeriSlipTable':wtSeriSlipTable,'wtSeriSlipEntry':wtSeriSlipEntry,'wtSeriSlipNetAddress':wtSeriSlipNetAddress,'wtSeriSlipNetRouting':wtSeriSlipNetRouting,'wtDeaPortSetup':wtDeaPortSetup,'wtDeaPorts':wtDeaPorts,'wtDeaInterfaceTable':wtDeaInterfaceTable,'wtDeaInterfaceEntry':wtDeaInterfaceEntry,_H:wtDeaInterfaceNo,'wtDeaPortTable':wtDeaPortTable,'wtDeaPortEntry':wtDeaPortEntry,'wtDeaLocalPort':wtDeaLocalPort,'wtDeaPortMode':wtDeaPortMode,'wtDeaDrvWatchdog':wtDeaDrvWatchdog,'wtDeaTcpClientTable':wtDeaTcpClientTable,'wtDeaTcpClientEntry':wtDeaTcpClientEntry,'wtDeaTcpServerPort':wtDeaTcpServerPort,'wtDeaTcpServerIp':wtDeaTcpServerIp,'wtDeaTcpInactTimeout':wtDeaTcpInactTimeout,'wtDeaTcpConnectTimeout':wtDeaTcpConnectTimeout,'wtDeaTcpInputMask':wtDeaTcpInputMask,'wtDeaUdpClientTable':wtDeaUdpClientTable,'wtDeaUdpClientEntry':wtDeaUdpClientEntry,'wtDeaUdpServerPort':wtDeaUdpServerPort,'wtDeaUdpServerIp':wtDeaUdpServerIp,'wtDeaUdpPacketProtocol':wtDeaUdpPacketProtocol,'wtDeaUdpInputMask':wtDeaUdpInputMask,'wtDeaUdpSendInterval':wtDeaUdpSendInterval,'wtDeaSnmpAgentTable':wtDeaSnmpAgentTable,'wtDeaSnmpAgentEntry':wtDeaSnmpAgentEntry,'wtDeaSnmpManagerIp':wtDeaSnmpManagerIp,'wtDeaSnmpInputMask':wtDeaSnmpInputMask,'wtDeaSnmpSendInterval':wtDeaSnmpSendInterval,'wtDeaB2bMasterTable':wtDeaB2bMasterTable,'wtDeaB2bMasterEntry':wtDeaB2bMasterEntry,'wtDeaB2bMaster-SlavePort':wtDeaB2bMaster_SlavePort,'wtDeaB2bMaster-SlaveIp':wtDeaB2bMaster_SlaveIp,'wtDeaB2bMaster-InputMask':wtDeaB2bMaster_InputMask,'wtDeaB2bMaster-SendInterval':wtDeaB2bMaster_SendInterval,'wtDeaB2bSlaveTable':wtDeaB2bSlaveTable,'wtDeaB2bSlaveEntry':wtDeaB2bSlaveEntry,'wtDeaB2bSlave-MasterPort':wtDeaB2bSlave_MasterPort,'wtDeaB2bSlave-MasterIp':wtDeaB2bSlave_MasterIp,'wtDeaB2bSlave-InputMask':wtDeaB2bSlave_InputMask,'wtDeaB2bSlave-SendInterval':wtDeaB2bSlave_SendInterval,'wtDeaDriver':wtDeaDriver,'wtDeaDrvTable':wtDeaDrvTable,'wtDeaDrvEntry':wtDeaDrvEntry,'deaInputChangedAlert':deaInputChangedAlert,'deaIntervalExpiredAlert':deaIntervalExpiredAlert,_L:wtDeaDrvInterfaceNo,_I:wtDeaDrvInputRegister,'wtDeaDrvOutputRegister':wtDeaDrvOutputRegister,'wtDeaDrvSetBit':wtDeaDrvSetBit,'wtDeaDrvTrapInputMask':wtDeaDrvTrapInputMask,'wtDeaDrvTrapInterval':wtDeaDrvTrapInterval})