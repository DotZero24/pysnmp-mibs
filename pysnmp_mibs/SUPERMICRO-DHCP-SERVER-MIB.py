_S='dhcpSrvSubnetUtlThreshold'
_R='dhcpSrvBindIpAddress'
_Q='dhcpSrvHostOptType'
_P='dhcpSrvSubnetOptType'
_O='dhcpSrvGblOptType'
_N='dhcpSrvExcludeStartIpAddress'
_M='TimeTicks'
_L='OctetString'
_K='dhcpSrvHostId'
_J='dhcpSrvHostType'
_I='DisplayString'
_H='TruthValue'
_G='dhcpSrvSubnetPoolIndex'
_F='not-accessible'
_E='Integer32'
_D='SUPERMICRO-DHCP-SERVER-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_M,'Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention',_H)
futureDhcpSrvMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,84))
if mibBuilder.loadTexts:futureDhcpSrvMIB.setRevisions(('2012-09-05 00:00',))
_DhcpSrvConfig_ObjectIdentity=ObjectIdentity
dhcpSrvConfig=_DhcpSrvConfig_ObjectIdentity((1,3,6,1,4,1,10876,101,1,84,1))
_DhcpSrvEnable_Type=TruthValue
_DhcpSrvEnable_Object=MibScalar
dhcpSrvEnable=_DhcpSrvEnable_Object((1,3,6,1,4,1,10876,101,1,84,1,1),_DhcpSrvEnable_Type())
dhcpSrvEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvEnable.setStatus(_A)
class _DhcpSrvDebugLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DhcpSrvDebugLevel_Type.__name__=_E
_DhcpSrvDebugLevel_Object=MibScalar
dhcpSrvDebugLevel=_DhcpSrvDebugLevel_Object((1,3,6,1,4,1,10876,101,1,84,1,2),_DhcpSrvDebugLevel_Type())
dhcpSrvDebugLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvDebugLevel.setStatus(_A)
class _DhcpSrvOfferReuseTimeOut_Type(TimeTicks):defaultValue=5
_DhcpSrvOfferReuseTimeOut_Type.__name__=_M
_DhcpSrvOfferReuseTimeOut_Object=MibScalar
dhcpSrvOfferReuseTimeOut=_DhcpSrvOfferReuseTimeOut_Object((1,3,6,1,4,1,10876,101,1,84,1,3),_DhcpSrvOfferReuseTimeOut_Type())
dhcpSrvOfferReuseTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvOfferReuseTimeOut.setStatus(_A)
class _DhcpSrvIcmpEchoEnable_Type(TruthValue):defaultValue=2
_DhcpSrvIcmpEchoEnable_Type.__name__=_H
_DhcpSrvIcmpEchoEnable_Object=MibScalar
dhcpSrvIcmpEchoEnable=_DhcpSrvIcmpEchoEnable_Object((1,3,6,1,4,1,10876,101,1,84,1,4),_DhcpSrvIcmpEchoEnable_Type())
dhcpSrvIcmpEchoEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvIcmpEchoEnable.setStatus(_A)
_DhcpSrvBootServerAddress_Type=IpAddress
_DhcpSrvBootServerAddress_Object=MibScalar
dhcpSrvBootServerAddress=_DhcpSrvBootServerAddress_Object((1,3,6,1,4,1,10876,101,1,84,1,5),_DhcpSrvBootServerAddress_Type())
dhcpSrvBootServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvBootServerAddress.setStatus(_A)
_DhcpSrvDefBootFilename_Type=OctetString
_DhcpSrvDefBootFilename_Object=MibScalar
dhcpSrvDefBootFilename=_DhcpSrvDefBootFilename_Object((1,3,6,1,4,1,10876,101,1,84,1,6),_DhcpSrvDefBootFilename_Type())
dhcpSrvDefBootFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvDefBootFilename.setStatus(_A)
class _DhcpSrvBootpClientsSupported_Type(TruthValue):defaultValue=1
_DhcpSrvBootpClientsSupported_Type.__name__=_H
_DhcpSrvBootpClientsSupported_Object=MibScalar
dhcpSrvBootpClientsSupported=_DhcpSrvBootpClientsSupported_Object((1,3,6,1,4,1,10876,101,1,84,1,7),_DhcpSrvBootpClientsSupported_Type())
dhcpSrvBootpClientsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvBootpClientsSupported.setStatus(_A)
class _DhcpSrvAutomaticBootpEnabled_Type(TruthValue):defaultValue=1
_DhcpSrvAutomaticBootpEnabled_Type.__name__=_H
_DhcpSrvAutomaticBootpEnabled_Object=MibScalar
dhcpSrvAutomaticBootpEnabled=_DhcpSrvAutomaticBootpEnabled_Object((1,3,6,1,4,1,10876,101,1,84,1,8),_DhcpSrvAutomaticBootpEnabled_Type())
dhcpSrvAutomaticBootpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvAutomaticBootpEnabled.setStatus(_A)
_DhcpSrvSubnetPoolConfigTable_Object=MibTable
dhcpSrvSubnetPoolConfigTable=_DhcpSrvSubnetPoolConfigTable_Object((1,3,6,1,4,1,10876,101,1,84,1,9))
if mibBuilder.loadTexts:dhcpSrvSubnetPoolConfigTable.setStatus(_A)
_DhcpSrvSubnetPoolConfigEntry_Object=MibTableRow
dhcpSrvSubnetPoolConfigEntry=_DhcpSrvSubnetPoolConfigEntry_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1))
dhcpSrvSubnetPoolConfigEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:dhcpSrvSubnetPoolConfigEntry.setStatus(_A)
class _DhcpSrvSubnetPoolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DhcpSrvSubnetPoolIndex_Type.__name__=_E
_DhcpSrvSubnetPoolIndex_Object=MibTableColumn
dhcpSrvSubnetPoolIndex=_DhcpSrvSubnetPoolIndex_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1,1),_DhcpSrvSubnetPoolIndex_Type())
dhcpSrvSubnetPoolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpSrvSubnetPoolIndex.setStatus(_A)
_DhcpSrvSubnetSubnet_Type=IpAddress
_DhcpSrvSubnetSubnet_Object=MibTableColumn
dhcpSrvSubnetSubnet=_DhcpSrvSubnetSubnet_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1,2),_DhcpSrvSubnetSubnet_Type())
dhcpSrvSubnetSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetSubnet.setStatus(_A)
_DhcpSrvSubnetPortNumber_Type=Integer32
_DhcpSrvSubnetPortNumber_Object=MibTableColumn
dhcpSrvSubnetPortNumber=_DhcpSrvSubnetPortNumber_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1,3),_DhcpSrvSubnetPortNumber_Type())
dhcpSrvSubnetPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetPortNumber.setStatus(_A)
_DhcpSrvSubnetMask_Type=IpAddress
_DhcpSrvSubnetMask_Object=MibTableColumn
dhcpSrvSubnetMask=_DhcpSrvSubnetMask_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1,4),_DhcpSrvSubnetMask_Type())
dhcpSrvSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetMask.setStatus(_A)
_DhcpSrvSubnetStartIpAddress_Type=IpAddress
_DhcpSrvSubnetStartIpAddress_Object=MibTableColumn
dhcpSrvSubnetStartIpAddress=_DhcpSrvSubnetStartIpAddress_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1,5),_DhcpSrvSubnetStartIpAddress_Type())
dhcpSrvSubnetStartIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetStartIpAddress.setStatus(_A)
_DhcpSrvSubnetEndIpAddress_Type=IpAddress
_DhcpSrvSubnetEndIpAddress_Object=MibTableColumn
dhcpSrvSubnetEndIpAddress=_DhcpSrvSubnetEndIpAddress_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1,6),_DhcpSrvSubnetEndIpAddress_Type())
dhcpSrvSubnetEndIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetEndIpAddress.setStatus(_A)
_DhcpSrvSubnetLeaseTime_Type=Integer32
_DhcpSrvSubnetLeaseTime_Object=MibTableColumn
dhcpSrvSubnetLeaseTime=_DhcpSrvSubnetLeaseTime_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1,7),_DhcpSrvSubnetLeaseTime_Type())
dhcpSrvSubnetLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetLeaseTime.setStatus(_A)
class _DhcpSrvSubnetPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DhcpSrvSubnetPoolName_Type.__name__=_I
_DhcpSrvSubnetPoolName_Object=MibTableColumn
dhcpSrvSubnetPoolName=_DhcpSrvSubnetPoolName_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1,8),_DhcpSrvSubnetPoolName_Type())
dhcpSrvSubnetPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetPoolName.setStatus(_A)
class _DhcpSrvSubnetUtlThreshold_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DhcpSrvSubnetUtlThreshold_Type.__name__=_E
_DhcpSrvSubnetUtlThreshold_Object=MibTableColumn
dhcpSrvSubnetUtlThreshold=_DhcpSrvSubnetUtlThreshold_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1,9),_DhcpSrvSubnetUtlThreshold_Type())
dhcpSrvSubnetUtlThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetUtlThreshold.setStatus(_A)
_DhcpSrvSubnetPoolRowStatus_Type=RowStatus
_DhcpSrvSubnetPoolRowStatus_Object=MibTableColumn
dhcpSrvSubnetPoolRowStatus=_DhcpSrvSubnetPoolRowStatus_Object((1,3,6,1,4,1,10876,101,1,84,1,9,1,10),_DhcpSrvSubnetPoolRowStatus_Type())
dhcpSrvSubnetPoolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetPoolRowStatus.setStatus(_A)
_DhcpSrvExcludeIpAddressTable_Object=MibTable
dhcpSrvExcludeIpAddressTable=_DhcpSrvExcludeIpAddressTable_Object((1,3,6,1,4,1,10876,101,1,84,1,10))
if mibBuilder.loadTexts:dhcpSrvExcludeIpAddressTable.setStatus(_A)
_DhcpSrvExcludeIpAddressEntry_Object=MibTableRow
dhcpSrvExcludeIpAddressEntry=_DhcpSrvExcludeIpAddressEntry_Object((1,3,6,1,4,1,10876,101,1,84,1,10,1))
dhcpSrvExcludeIpAddressEntry.setIndexNames((0,_D,_G),(0,_D,_N))
if mibBuilder.loadTexts:dhcpSrvExcludeIpAddressEntry.setStatus(_A)
_DhcpSrvExcludeStartIpAddress_Type=IpAddress
_DhcpSrvExcludeStartIpAddress_Object=MibTableColumn
dhcpSrvExcludeStartIpAddress=_DhcpSrvExcludeStartIpAddress_Object((1,3,6,1,4,1,10876,101,1,84,1,10,1,1),_DhcpSrvExcludeStartIpAddress_Type())
dhcpSrvExcludeStartIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpSrvExcludeStartIpAddress.setStatus(_A)
_DhcpSrvExcludeEndIpAddress_Type=IpAddress
_DhcpSrvExcludeEndIpAddress_Object=MibTableColumn
dhcpSrvExcludeEndIpAddress=_DhcpSrvExcludeEndIpAddress_Object((1,3,6,1,4,1,10876,101,1,84,1,10,1,2),_DhcpSrvExcludeEndIpAddress_Type())
dhcpSrvExcludeEndIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvExcludeEndIpAddress.setStatus(_A)
_DhcpSrvExcludeAddressRowStatus_Type=RowStatus
_DhcpSrvExcludeAddressRowStatus_Object=MibTableColumn
dhcpSrvExcludeAddressRowStatus=_DhcpSrvExcludeAddressRowStatus_Object((1,3,6,1,4,1,10876,101,1,84,1,10,1,3),_DhcpSrvExcludeAddressRowStatus_Type())
dhcpSrvExcludeAddressRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvExcludeAddressRowStatus.setStatus(_A)
_DhcpSrvGblOptTable_Object=MibTable
dhcpSrvGblOptTable=_DhcpSrvGblOptTable_Object((1,3,6,1,4,1,10876,101,1,84,1,11))
if mibBuilder.loadTexts:dhcpSrvGblOptTable.setStatus(_A)
_DhcpSrvGblOptEntry_Object=MibTableRow
dhcpSrvGblOptEntry=_DhcpSrvGblOptEntry_Object((1,3,6,1,4,1,10876,101,1,84,1,11,1))
dhcpSrvGblOptEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:dhcpSrvGblOptEntry.setStatus(_A)
class _DhcpSrvGblOptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DhcpSrvGblOptType_Type.__name__=_E
_DhcpSrvGblOptType_Object=MibTableColumn
dhcpSrvGblOptType=_DhcpSrvGblOptType_Object((1,3,6,1,4,1,10876,101,1,84,1,11,1,1),_DhcpSrvGblOptType_Type())
dhcpSrvGblOptType.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpSrvGblOptType.setStatus(_A)
_DhcpSrvGblOptLen_Type=Integer32
_DhcpSrvGblOptLen_Object=MibTableColumn
dhcpSrvGblOptLen=_DhcpSrvGblOptLen_Object((1,3,6,1,4,1,10876,101,1,84,1,11,1,2),_DhcpSrvGblOptLen_Type())
dhcpSrvGblOptLen.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvGblOptLen.setStatus(_A)
_DhcpSrvGblOptVal_Type=OctetString
_DhcpSrvGblOptVal_Object=MibTableColumn
dhcpSrvGblOptVal=_DhcpSrvGblOptVal_Object((1,3,6,1,4,1,10876,101,1,84,1,11,1,3),_DhcpSrvGblOptVal_Type())
dhcpSrvGblOptVal.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvGblOptVal.setStatus(_A)
_DhcpSrvGblOptRowStatus_Type=RowStatus
_DhcpSrvGblOptRowStatus_Object=MibTableColumn
dhcpSrvGblOptRowStatus=_DhcpSrvGblOptRowStatus_Object((1,3,6,1,4,1,10876,101,1,84,1,11,1,4),_DhcpSrvGblOptRowStatus_Type())
dhcpSrvGblOptRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvGblOptRowStatus.setStatus(_A)
_DhcpSrvSubnetOptTable_Object=MibTable
dhcpSrvSubnetOptTable=_DhcpSrvSubnetOptTable_Object((1,3,6,1,4,1,10876,101,1,84,1,12))
if mibBuilder.loadTexts:dhcpSrvSubnetOptTable.setStatus(_A)
_DhcpSrvSubnetOptEntry_Object=MibTableRow
dhcpSrvSubnetOptEntry=_DhcpSrvSubnetOptEntry_Object((1,3,6,1,4,1,10876,101,1,84,1,12,1))
dhcpSrvSubnetOptEntry.setIndexNames((0,_D,_G),(0,_D,_P))
if mibBuilder.loadTexts:dhcpSrvSubnetOptEntry.setStatus(_A)
class _DhcpSrvSubnetOptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DhcpSrvSubnetOptType_Type.__name__=_E
_DhcpSrvSubnetOptType_Object=MibTableColumn
dhcpSrvSubnetOptType=_DhcpSrvSubnetOptType_Object((1,3,6,1,4,1,10876,101,1,84,1,12,1,1),_DhcpSrvSubnetOptType_Type())
dhcpSrvSubnetOptType.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpSrvSubnetOptType.setStatus(_A)
_DhcpSrvSubnetOptLen_Type=Integer32
_DhcpSrvSubnetOptLen_Object=MibTableColumn
dhcpSrvSubnetOptLen=_DhcpSrvSubnetOptLen_Object((1,3,6,1,4,1,10876,101,1,84,1,12,1,2),_DhcpSrvSubnetOptLen_Type())
dhcpSrvSubnetOptLen.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetOptLen.setStatus(_A)
_DhcpSrvSubnetOptVal_Type=OctetString
_DhcpSrvSubnetOptVal_Object=MibTableColumn
dhcpSrvSubnetOptVal=_DhcpSrvSubnetOptVal_Object((1,3,6,1,4,1,10876,101,1,84,1,12,1,3),_DhcpSrvSubnetOptVal_Type())
dhcpSrvSubnetOptVal.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetOptVal.setStatus(_A)
_DhcpSrvSubnetOptRowStatus_Type=RowStatus
_DhcpSrvSubnetOptRowStatus_Object=MibTableColumn
dhcpSrvSubnetOptRowStatus=_DhcpSrvSubnetOptRowStatus_Object((1,3,6,1,4,1,10876,101,1,84,1,12,1,4),_DhcpSrvSubnetOptRowStatus_Type())
dhcpSrvSubnetOptRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvSubnetOptRowStatus.setStatus(_A)
_DhcpSrvHostOptTable_Object=MibTable
dhcpSrvHostOptTable=_DhcpSrvHostOptTable_Object((1,3,6,1,4,1,10876,101,1,84,1,13))
if mibBuilder.loadTexts:dhcpSrvHostOptTable.setStatus(_A)
_DhcpSrvHostOptEntry_Object=MibTableRow
dhcpSrvHostOptEntry=_DhcpSrvHostOptEntry_Object((1,3,6,1,4,1,10876,101,1,84,1,13,1))
dhcpSrvHostOptEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_G),(0,_D,_Q))
if mibBuilder.loadTexts:dhcpSrvHostOptEntry.setStatus(_A)
class _DhcpSrvHostType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DhcpSrvHostType_Type.__name__=_E
_DhcpSrvHostType_Object=MibTableColumn
dhcpSrvHostType=_DhcpSrvHostType_Object((1,3,6,1,4,1,10876,101,1,84,1,13,1,1),_DhcpSrvHostType_Type())
dhcpSrvHostType.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpSrvHostType.setStatus(_A)
class _DhcpSrvHostId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DhcpSrvHostId_Type.__name__=_L
_DhcpSrvHostId_Object=MibTableColumn
dhcpSrvHostId=_DhcpSrvHostId_Object((1,3,6,1,4,1,10876,101,1,84,1,13,1,2),_DhcpSrvHostId_Type())
dhcpSrvHostId.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpSrvHostId.setStatus(_A)
class _DhcpSrvHostOptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DhcpSrvHostOptType_Type.__name__=_E
_DhcpSrvHostOptType_Object=MibTableColumn
dhcpSrvHostOptType=_DhcpSrvHostOptType_Object((1,3,6,1,4,1,10876,101,1,84,1,13,1,3),_DhcpSrvHostOptType_Type())
dhcpSrvHostOptType.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpSrvHostOptType.setStatus(_A)
_DhcpSrvHostOptLen_Type=Integer32
_DhcpSrvHostOptLen_Object=MibTableColumn
dhcpSrvHostOptLen=_DhcpSrvHostOptLen_Object((1,3,6,1,4,1,10876,101,1,84,1,13,1,4),_DhcpSrvHostOptLen_Type())
dhcpSrvHostOptLen.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvHostOptLen.setStatus(_A)
_DhcpSrvHostOptVal_Type=OctetString
_DhcpSrvHostOptVal_Object=MibTableColumn
dhcpSrvHostOptVal=_DhcpSrvHostOptVal_Object((1,3,6,1,4,1,10876,101,1,84,1,13,1,5),_DhcpSrvHostOptVal_Type())
dhcpSrvHostOptVal.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvHostOptVal.setStatus(_A)
_DhcpSrvHostOptRowStatus_Type=RowStatus
_DhcpSrvHostOptRowStatus_Object=MibTableColumn
dhcpSrvHostOptRowStatus=_DhcpSrvHostOptRowStatus_Object((1,3,6,1,4,1,10876,101,1,84,1,13,1,6),_DhcpSrvHostOptRowStatus_Type())
dhcpSrvHostOptRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvHostOptRowStatus.setStatus(_A)
_DhcpSrvHostConfigTable_Object=MibTable
dhcpSrvHostConfigTable=_DhcpSrvHostConfigTable_Object((1,3,6,1,4,1,10876,101,1,84,1,14))
if mibBuilder.loadTexts:dhcpSrvHostConfigTable.setStatus(_A)
_DhcpSrvHostConfigEntry_Object=MibTableRow
dhcpSrvHostConfigEntry=_DhcpSrvHostConfigEntry_Object((1,3,6,1,4,1,10876,101,1,84,1,14,1))
dhcpSrvHostConfigEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_G))
if mibBuilder.loadTexts:dhcpSrvHostConfigEntry.setStatus(_A)
_DhcpSrvHostIpAddress_Type=IpAddress
_DhcpSrvHostIpAddress_Object=MibTableColumn
dhcpSrvHostIpAddress=_DhcpSrvHostIpAddress_Object((1,3,6,1,4,1,10876,101,1,84,1,14,1,1),_DhcpSrvHostIpAddress_Type())
dhcpSrvHostIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvHostIpAddress.setStatus(_A)
_DhcpSrvHostPoolName_Type=Integer32
_DhcpSrvHostPoolName_Object=MibTableColumn
dhcpSrvHostPoolName=_DhcpSrvHostPoolName_Object((1,3,6,1,4,1,10876,101,1,84,1,14,1,2),_DhcpSrvHostPoolName_Type())
dhcpSrvHostPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvHostPoolName.setStatus(_A)
class _DhcpSrvHostBootFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DhcpSrvHostBootFileName_Type.__name__=_I
_DhcpSrvHostBootFileName_Object=MibTableColumn
dhcpSrvHostBootFileName=_DhcpSrvHostBootFileName_Object((1,3,6,1,4,1,10876,101,1,84,1,14,1,3),_DhcpSrvHostBootFileName_Type())
dhcpSrvHostBootFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvHostBootFileName.setStatus(_A)
_DhcpSrvHostBootServerAddress_Type=IpAddress
_DhcpSrvHostBootServerAddress_Object=MibTableColumn
dhcpSrvHostBootServerAddress=_DhcpSrvHostBootServerAddress_Object((1,3,6,1,4,1,10876,101,1,84,1,14,1,4),_DhcpSrvHostBootServerAddress_Type())
dhcpSrvHostBootServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvHostBootServerAddress.setStatus(_A)
_DhcpSrvHostConfigRowStatus_Type=RowStatus
_DhcpSrvHostConfigRowStatus_Object=MibTableColumn
dhcpSrvHostConfigRowStatus=_DhcpSrvHostConfigRowStatus_Object((1,3,6,1,4,1,10876,101,1,84,1,14,1,5),_DhcpSrvHostConfigRowStatus_Type())
dhcpSrvHostConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvHostConfigRowStatus.setStatus(_A)
_DhcpSrvBinding_ObjectIdentity=ObjectIdentity
dhcpSrvBinding=_DhcpSrvBinding_ObjectIdentity((1,3,6,1,4,1,10876,101,1,84,2))
_DhcpSrvBindingTable_Object=MibTable
dhcpSrvBindingTable=_DhcpSrvBindingTable_Object((1,3,6,1,4,1,10876,101,1,84,2,1))
if mibBuilder.loadTexts:dhcpSrvBindingTable.setStatus(_A)
_DhcpSrvBindingEntry_Object=MibTableRow
dhcpSrvBindingEntry=_DhcpSrvBindingEntry_Object((1,3,6,1,4,1,10876,101,1,84,2,1,1))
dhcpSrvBindingEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:dhcpSrvBindingEntry.setStatus(_A)
_DhcpSrvBindIpAddress_Type=IpAddress
_DhcpSrvBindIpAddress_Object=MibTableColumn
dhcpSrvBindIpAddress=_DhcpSrvBindIpAddress_Object((1,3,6,1,4,1,10876,101,1,84,2,1,1,1),_DhcpSrvBindIpAddress_Type())
dhcpSrvBindIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpSrvBindIpAddress.setStatus(_A)
class _DhcpSrvBindHwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('clientid',0),('ethernet',1)))
_DhcpSrvBindHwType_Type.__name__=_E
_DhcpSrvBindHwType_Object=MibTableColumn
dhcpSrvBindHwType=_DhcpSrvBindHwType_Object((1,3,6,1,4,1,10876,101,1,84,2,1,1,2),_DhcpSrvBindHwType_Type())
dhcpSrvBindHwType.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSrvBindHwType.setStatus(_A)
_DhcpSrvBindHwAddress_Type=OctetString
_DhcpSrvBindHwAddress_Object=MibTableColumn
dhcpSrvBindHwAddress=_DhcpSrvBindHwAddress_Object((1,3,6,1,4,1,10876,101,1,84,2,1,1,3),_DhcpSrvBindHwAddress_Type())
dhcpSrvBindHwAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSrvBindHwAddress.setStatus(_A)
_DhcpSrvBindExpireTime_Type=Integer32
_DhcpSrvBindExpireTime_Object=MibTableColumn
dhcpSrvBindExpireTime=_DhcpSrvBindExpireTime_Object((1,3,6,1,4,1,10876,101,1,84,2,1,1,4),_DhcpSrvBindExpireTime_Type())
dhcpSrvBindExpireTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSrvBindExpireTime.setStatus(_A)
class _DhcpSrvBindAllocMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('manual',2)))
_DhcpSrvBindAllocMethod_Type.__name__=_E
_DhcpSrvBindAllocMethod_Object=MibTableColumn
dhcpSrvBindAllocMethod=_DhcpSrvBindAllocMethod_Object((1,3,6,1,4,1,10876,101,1,84,2,1,1,5),_DhcpSrvBindAllocMethod_Type())
dhcpSrvBindAllocMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSrvBindAllocMethod.setStatus(_A)
class _DhcpSrvBindState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5)));namedValues=NamedValues(*(('offered',1),('assigned',2),('probing',5)))
_DhcpSrvBindState_Type.__name__=_E
_DhcpSrvBindState_Object=MibTableColumn
dhcpSrvBindState=_DhcpSrvBindState_Object((1,3,6,1,4,1,10876,101,1,84,2,1,1,6),_DhcpSrvBindState_Type())
dhcpSrvBindState.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSrvBindState.setStatus(_A)
_DhcpSrvBindXid_Type=Unsigned32
_DhcpSrvBindXid_Object=MibTableColumn
dhcpSrvBindXid=_DhcpSrvBindXid_Object((1,3,6,1,4,1,10876,101,1,84,2,1,1,7),_DhcpSrvBindXid_Type())
dhcpSrvBindXid.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSrvBindXid.setStatus(_A)
_DhcpSrvBindEntryStatus_Type=RowStatus
_DhcpSrvBindEntryStatus_Object=MibTableColumn
dhcpSrvBindEntryStatus=_DhcpSrvBindEntryStatus_Object((1,3,6,1,4,1,10876,101,1,84,2,1,1,8),_DhcpSrvBindEntryStatus_Type())
dhcpSrvBindEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSrvBindEntryStatus.setStatus(_A)
_DhcpSrvCounters_ObjectIdentity=ObjectIdentity
dhcpSrvCounters=_DhcpSrvCounters_ObjectIdentity((1,3,6,1,4,1,10876,101,1,84,3))
_DhcpCountDiscovers_Type=Counter32
_DhcpCountDiscovers_Object=MibScalar
dhcpCountDiscovers=_DhcpCountDiscovers_Object((1,3,6,1,4,1,10876,101,1,84,3,1),_DhcpCountDiscovers_Type())
dhcpCountDiscovers.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountDiscovers.setStatus(_A)
_DhcpCountRequests_Type=Counter32
_DhcpCountRequests_Object=MibScalar
dhcpCountRequests=_DhcpCountRequests_Object((1,3,6,1,4,1,10876,101,1,84,3,2),_DhcpCountRequests_Type())
dhcpCountRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountRequests.setStatus(_A)
_DhcpCountReleases_Type=Counter32
_DhcpCountReleases_Object=MibScalar
dhcpCountReleases=_DhcpCountReleases_Object((1,3,6,1,4,1,10876,101,1,84,3,3),_DhcpCountReleases_Type())
dhcpCountReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountReleases.setStatus(_A)
_DhcpCountDeclines_Type=Counter32
_DhcpCountDeclines_Object=MibScalar
dhcpCountDeclines=_DhcpCountDeclines_Object((1,3,6,1,4,1,10876,101,1,84,3,4),_DhcpCountDeclines_Type())
dhcpCountDeclines.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountDeclines.setStatus(_A)
_DhcpCountInforms_Type=Counter32
_DhcpCountInforms_Object=MibScalar
dhcpCountInforms=_DhcpCountInforms_Object((1,3,6,1,4,1,10876,101,1,84,3,5),_DhcpCountInforms_Type())
dhcpCountInforms.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountInforms.setStatus(_A)
_DhcpCountInvalids_Type=Counter32
_DhcpCountInvalids_Object=MibScalar
dhcpCountInvalids=_DhcpCountInvalids_Object((1,3,6,1,4,1,10876,101,1,84,3,6),_DhcpCountInvalids_Type())
dhcpCountInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountInvalids.setStatus(_A)
_DhcpCountOffers_Type=Counter32
_DhcpCountOffers_Object=MibScalar
dhcpCountOffers=_DhcpCountOffers_Object((1,3,6,1,4,1,10876,101,1,84,3,7),_DhcpCountOffers_Type())
dhcpCountOffers.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountOffers.setStatus(_A)
_DhcpCountAcks_Type=Counter32
_DhcpCountAcks_Object=MibScalar
dhcpCountAcks=_DhcpCountAcks_Object((1,3,6,1,4,1,10876,101,1,84,3,8),_DhcpCountAcks_Type())
dhcpCountAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountAcks.setStatus(_A)
_DhcpCountNacks_Type=Counter32
_DhcpCountNacks_Object=MibScalar
dhcpCountNacks=_DhcpCountNacks_Object((1,3,6,1,4,1,10876,101,1,84,3,9),_DhcpCountNacks_Type())
dhcpCountNacks.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountNacks.setStatus(_A)
_DhcpCountDroppedUnknownClient_Type=Counter32
_DhcpCountDroppedUnknownClient_Object=MibScalar
dhcpCountDroppedUnknownClient=_DhcpCountDroppedUnknownClient_Object((1,3,6,1,4,1,10876,101,1,84,3,10),_DhcpCountDroppedUnknownClient_Type())
dhcpCountDroppedUnknownClient.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountDroppedUnknownClient.setStatus(_A)
_DhcpCountDroppedNotServingSubnet_Type=Counter32
_DhcpCountDroppedNotServingSubnet_Object=MibScalar
dhcpCountDroppedNotServingSubnet=_DhcpCountDroppedNotServingSubnet_Object((1,3,6,1,4,1,10876,101,1,84,3,11),_DhcpCountDroppedNotServingSubnet_Type())
dhcpCountDroppedNotServingSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpCountDroppedNotServingSubnet.setStatus(_A)
class _DhcpCountResetCounters_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set',1),('notset',2)))
_DhcpCountResetCounters_Type.__name__=_E
_DhcpCountResetCounters_Object=MibScalar
dhcpCountResetCounters=_DhcpCountResetCounters_Object((1,3,6,1,4,1,10876,101,1,84,3,12),_DhcpCountResetCounters_Type())
dhcpCountResetCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountResetCounters.setStatus(_A)
_DhcpSrvTrapGroup_ObjectIdentity=ObjectIdentity
dhcpSrvTrapGroup=_DhcpSrvTrapGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,84,4))
_DhcpSrvTraps_ObjectIdentity=ObjectIdentity
dhcpSrvTraps=_DhcpSrvTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,84,4,0))
dhcpSrvPoolUtlTrap=NotificationType((1,3,6,1,4,1,10876,101,1,84,4,0,1))
dhcpSrvPoolUtlTrap.setObjects((_D,_S))
if mibBuilder.loadTexts:dhcpSrvPoolUtlTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'futureDhcpSrvMIB':futureDhcpSrvMIB,'dhcpSrvConfig':dhcpSrvConfig,'dhcpSrvEnable':dhcpSrvEnable,'dhcpSrvDebugLevel':dhcpSrvDebugLevel,'dhcpSrvOfferReuseTimeOut':dhcpSrvOfferReuseTimeOut,'dhcpSrvIcmpEchoEnable':dhcpSrvIcmpEchoEnable,'dhcpSrvBootServerAddress':dhcpSrvBootServerAddress,'dhcpSrvDefBootFilename':dhcpSrvDefBootFilename,'dhcpSrvBootpClientsSupported':dhcpSrvBootpClientsSupported,'dhcpSrvAutomaticBootpEnabled':dhcpSrvAutomaticBootpEnabled,'dhcpSrvSubnetPoolConfigTable':dhcpSrvSubnetPoolConfigTable,'dhcpSrvSubnetPoolConfigEntry':dhcpSrvSubnetPoolConfigEntry,_G:dhcpSrvSubnetPoolIndex,'dhcpSrvSubnetSubnet':dhcpSrvSubnetSubnet,'dhcpSrvSubnetPortNumber':dhcpSrvSubnetPortNumber,'dhcpSrvSubnetMask':dhcpSrvSubnetMask,'dhcpSrvSubnetStartIpAddress':dhcpSrvSubnetStartIpAddress,'dhcpSrvSubnetEndIpAddress':dhcpSrvSubnetEndIpAddress,'dhcpSrvSubnetLeaseTime':dhcpSrvSubnetLeaseTime,'dhcpSrvSubnetPoolName':dhcpSrvSubnetPoolName,_S:dhcpSrvSubnetUtlThreshold,'dhcpSrvSubnetPoolRowStatus':dhcpSrvSubnetPoolRowStatus,'dhcpSrvExcludeIpAddressTable':dhcpSrvExcludeIpAddressTable,'dhcpSrvExcludeIpAddressEntry':dhcpSrvExcludeIpAddressEntry,_N:dhcpSrvExcludeStartIpAddress,'dhcpSrvExcludeEndIpAddress':dhcpSrvExcludeEndIpAddress,'dhcpSrvExcludeAddressRowStatus':dhcpSrvExcludeAddressRowStatus,'dhcpSrvGblOptTable':dhcpSrvGblOptTable,'dhcpSrvGblOptEntry':dhcpSrvGblOptEntry,_O:dhcpSrvGblOptType,'dhcpSrvGblOptLen':dhcpSrvGblOptLen,'dhcpSrvGblOptVal':dhcpSrvGblOptVal,'dhcpSrvGblOptRowStatus':dhcpSrvGblOptRowStatus,'dhcpSrvSubnetOptTable':dhcpSrvSubnetOptTable,'dhcpSrvSubnetOptEntry':dhcpSrvSubnetOptEntry,_P:dhcpSrvSubnetOptType,'dhcpSrvSubnetOptLen':dhcpSrvSubnetOptLen,'dhcpSrvSubnetOptVal':dhcpSrvSubnetOptVal,'dhcpSrvSubnetOptRowStatus':dhcpSrvSubnetOptRowStatus,'dhcpSrvHostOptTable':dhcpSrvHostOptTable,'dhcpSrvHostOptEntry':dhcpSrvHostOptEntry,_J:dhcpSrvHostType,_K:dhcpSrvHostId,_Q:dhcpSrvHostOptType,'dhcpSrvHostOptLen':dhcpSrvHostOptLen,'dhcpSrvHostOptVal':dhcpSrvHostOptVal,'dhcpSrvHostOptRowStatus':dhcpSrvHostOptRowStatus,'dhcpSrvHostConfigTable':dhcpSrvHostConfigTable,'dhcpSrvHostConfigEntry':dhcpSrvHostConfigEntry,'dhcpSrvHostIpAddress':dhcpSrvHostIpAddress,'dhcpSrvHostPoolName':dhcpSrvHostPoolName,'dhcpSrvHostBootFileName':dhcpSrvHostBootFileName,'dhcpSrvHostBootServerAddress':dhcpSrvHostBootServerAddress,'dhcpSrvHostConfigRowStatus':dhcpSrvHostConfigRowStatus,'dhcpSrvBinding':dhcpSrvBinding,'dhcpSrvBindingTable':dhcpSrvBindingTable,'dhcpSrvBindingEntry':dhcpSrvBindingEntry,_R:dhcpSrvBindIpAddress,'dhcpSrvBindHwType':dhcpSrvBindHwType,'dhcpSrvBindHwAddress':dhcpSrvBindHwAddress,'dhcpSrvBindExpireTime':dhcpSrvBindExpireTime,'dhcpSrvBindAllocMethod':dhcpSrvBindAllocMethod,'dhcpSrvBindState':dhcpSrvBindState,'dhcpSrvBindXid':dhcpSrvBindXid,'dhcpSrvBindEntryStatus':dhcpSrvBindEntryStatus,'dhcpSrvCounters':dhcpSrvCounters,'dhcpCountDiscovers':dhcpCountDiscovers,'dhcpCountRequests':dhcpCountRequests,'dhcpCountReleases':dhcpCountReleases,'dhcpCountDeclines':dhcpCountDeclines,'dhcpCountInforms':dhcpCountInforms,'dhcpCountInvalids':dhcpCountInvalids,'dhcpCountOffers':dhcpCountOffers,'dhcpCountAcks':dhcpCountAcks,'dhcpCountNacks':dhcpCountNacks,'dhcpCountDroppedUnknownClient':dhcpCountDroppedUnknownClient,'dhcpCountDroppedNotServingSubnet':dhcpCountDroppedNotServingSubnet,'dhcpCountResetCounters':dhcpCountResetCounters,'dhcpSrvTrapGroup':dhcpSrvTrapGroup,'dhcpSrvTraps':dhcpSrvTraps,'dhcpSrvPoolUtlTrap':dhcpSrvPoolUtlTrap})