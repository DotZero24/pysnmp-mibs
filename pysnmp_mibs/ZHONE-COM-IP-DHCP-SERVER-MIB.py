_p='dhcpTrapZhoneIpInterfaceIndex'
_o='dhcpTrapZhoneCpeSysObjectID'
_n='dhcpCountersEntry'
_m='bootpCountersEntry'
_l='dhcpServerHostOptionEntry'
_k='dhcpServerSubnetOptionEntry'
_j='dhcpServerGroupOptionEntry'
_i='dhcpHostIndex'
_h='dhcpSubnetIndex'
_g='dhcpGroupIndex'
_f='dhcpLeaseIpAddress'
_e='dhcpLeaseDomain'
_d='accessible-for-notify'
_c='zhoneSysCardSwSpecificVers'
_b='ZHONE-SYSTEM-MIB'
_a='zhoneSlotNumber'
_Z='zhoneShelfNumber'
_Y='subPortNumber'
_X='pportNumber'
_W='ipIfVpi'
_V='ipIfVci'
_U='ipIfLgId'
_T='cardPostResults'
_S='cardMfgSerialNumber'
_R='TruthValue'
_Q='ipIfAddr'
_P='ZHONE-CARD-RESOURCES-MIB'
_O='PhysAddress'
_N='not-accessible'
_M='ZHONE-INTERFACE-TRANSLATION-MIB'
_L='OctetString'
_K='ZHONE-COM-IP-REC-MIB'
_J='SnmpAdminString'
_I='00000000'
_H='seconds'
_G='ZHONE-COM-IP-DHCP-SERVER-MIB'
_F='IpAddress'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysObjectID,=mibBuilder.importSymbols('SNMPv2-MIB','sysObjectID')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_F,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_O,'TextualConvention',_R)
cardMfgSerialNumber,cardPostResults=mibBuilder.importSymbols(_P,_S,_T)
ZhoneRDIndex,rdEntry=mibBuilder.importSymbols('ZHONE-COM-IP-RD-MIB','ZhoneRDIndex','rdEntry')
ipIfAddr,ipIfLgId,ipIfVci,ipIfVpi=mibBuilder.importSymbols(_K,_Q,_U,_V,_W)
pportNumber,subPortNumber,zhoneShelfNumber,zhoneSlotNumber=mibBuilder.importSymbols(_M,_X,_Y,_Z,_a)
zhoneSysCardSwSpecificVers,=mibBuilder.importSymbols(_b,_c)
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
ZhoneAdminString,ZhoneFileName,ZhoneRowStatus,ZhoneShelfValue,ZhoneSlotValue=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString','ZhoneFileName','ZhoneRowStatus','ZhoneShelfValue','ZhoneSlotValue')
comIpDhcpServer=ModuleIdentity((1,3,6,1,4,1,5504,6,61))
if mibBuilder.loadTexts:comIpDhcpServer.setRevisions(('2003-09-10 10:47','2003-04-18 10:10','2000-12-03 14:00','2000-11-28 15:00','2000-12-05 12:11','2000-10-02 12:05','2000-09-15 16:50','2000-09-11 15:41'))
_DhcpServer_ObjectIdentity=ObjectIdentity
dhcpServer=_DhcpServer_ObjectIdentity((1,3,6,1,4,1,5504,4,1,11))
if mibBuilder.loadTexts:dhcpServer.setStatus(_A)
_DhcpServerTraps_ObjectIdentity=ObjectIdentity
dhcpServerTraps=_DhcpServerTraps_ObjectIdentity((1,3,6,1,4,1,5504,4,1,11,0))
if mibBuilder.loadTexts:dhcpServerTraps.setStatus(_A)
_DhcpTrapZhoneCpeSysObjectID_Type=ObjectIdentifier
_DhcpTrapZhoneCpeSysObjectID_Object=MibScalar
dhcpTrapZhoneCpeSysObjectID=_DhcpTrapZhoneCpeSysObjectID_Object((1,3,6,1,4,1,5504,4,1,11,0,2),_DhcpTrapZhoneCpeSysObjectID_Type())
dhcpTrapZhoneCpeSysObjectID.setMaxAccess(_d)
if mibBuilder.loadTexts:dhcpTrapZhoneCpeSysObjectID.setStatus(_A)
_DhcpTrapZhoneIpInterfaceIndex_Type=InterfaceIndex
_DhcpTrapZhoneIpInterfaceIndex_Object=MibScalar
dhcpTrapZhoneIpInterfaceIndex=_DhcpTrapZhoneIpInterfaceIndex_Object((1,3,6,1,4,1,5504,4,1,11,0,4),_DhcpTrapZhoneIpInterfaceIndex_Type())
dhcpTrapZhoneIpInterfaceIndex.setMaxAccess(_d)
if mibBuilder.loadTexts:dhcpTrapZhoneIpInterfaceIndex.setStatus(_A)
class _DhcpServerDefaultLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpServerDefaultLeaseTime_Type.__name__=_D
_DhcpServerDefaultLeaseTime_Object=MibScalar
dhcpServerDefaultLeaseTime=_DhcpServerDefaultLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,1),_DhcpServerDefaultLeaseTime_Type())
dhcpServerDefaultLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpServerDefaultLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpServerDefaultLeaseTime.setUnits(_H)
class _DhcpServerDefaultMinLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpServerDefaultMinLeaseTime_Type.__name__=_D
_DhcpServerDefaultMinLeaseTime_Object=MibScalar
dhcpServerDefaultMinLeaseTime=_DhcpServerDefaultMinLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,2),_DhcpServerDefaultMinLeaseTime_Type())
dhcpServerDefaultMinLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpServerDefaultMinLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpServerDefaultMinLeaseTime.setUnits(_H)
class _DhcpServerDefaultMaxLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpServerDefaultMaxLeaseTime_Type.__name__=_D
_DhcpServerDefaultMaxLeaseTime_Object=MibScalar
dhcpServerDefaultMaxLeaseTime=_DhcpServerDefaultMaxLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,3),_DhcpServerDefaultMaxLeaseTime_Type())
dhcpServerDefaultMaxLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpServerDefaultMaxLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpServerDefaultMaxLeaseTime.setUnits(_H)
class _DhcpServerDefaultReserveStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DhcpServerDefaultReserveStart_Type.__name__=_D
_DhcpServerDefaultReserveStart_Object=MibScalar
dhcpServerDefaultReserveStart=_DhcpServerDefaultReserveStart_Object((1,3,6,1,4,1,5504,4,1,11,4),_DhcpServerDefaultReserveStart_Type())
dhcpServerDefaultReserveStart.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpServerDefaultReserveStart.setStatus(_A)
class _DhcpServerDefaultReserveEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DhcpServerDefaultReserveEnd_Type.__name__=_D
_DhcpServerDefaultReserveEnd_Object=MibScalar
dhcpServerDefaultReserveEnd=_DhcpServerDefaultReserveEnd_Object((1,3,6,1,4,1,5504,4,1,11,5),_DhcpServerDefaultReserveEnd_Type())
dhcpServerDefaultReserveEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpServerDefaultReserveEnd.setStatus(_A)
_DhcpServerLeaseTable_Object=MibTable
dhcpServerLeaseTable=_DhcpServerLeaseTable_Object((1,3,6,1,4,1,5504,4,1,11,6))
if mibBuilder.loadTexts:dhcpServerLeaseTable.setStatus(_A)
_DhcpServerLeaseEntry_Object=MibTableRow
dhcpServerLeaseEntry=_DhcpServerLeaseEntry_Object((1,3,6,1,4,1,5504,4,1,11,6,1))
dhcpServerLeaseEntry.setIndexNames((0,_G,_e),(0,_G,_f))
if mibBuilder.loadTexts:dhcpServerLeaseEntry.setStatus(_A)
_DhcpLeaseDomain_Type=ZhoneRDIndex
_DhcpLeaseDomain_Object=MibTableColumn
dhcpLeaseDomain=_DhcpLeaseDomain_Object((1,3,6,1,4,1,5504,4,1,11,6,1,1),_DhcpLeaseDomain_Type())
dhcpLeaseDomain.setMaxAccess(_N)
if mibBuilder.loadTexts:dhcpLeaseDomain.setStatus(_A)
_DhcpLeaseIpAddress_Type=IpAddress
_DhcpLeaseIpAddress_Object=MibTableColumn
dhcpLeaseIpAddress=_DhcpLeaseIpAddress_Object((1,3,6,1,4,1,5504,4,1,11,6,1,2),_DhcpLeaseIpAddress_Type())
dhcpLeaseIpAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:dhcpLeaseIpAddress.setStatus(_A)
_DhcpLeaseStarts_Type=Unsigned32
_DhcpLeaseStarts_Object=MibTableColumn
dhcpLeaseStarts=_DhcpLeaseStarts_Object((1,3,6,1,4,1,5504,4,1,11,6,1,3),_DhcpLeaseStarts_Type())
dhcpLeaseStarts.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseStarts.setStatus(_A)
_DhcpLeaseEnds_Type=Unsigned32
_DhcpLeaseEnds_Object=MibTableColumn
dhcpLeaseEnds=_DhcpLeaseEnds_Object((1,3,6,1,4,1,5504,4,1,11,6,1,4),_DhcpLeaseEnds_Type())
dhcpLeaseEnds.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseEnds.setStatus(_A)
class _DhcpLeaseHardwareAddress_Type(PhysAddress):defaultHexValue='0000';subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DhcpLeaseHardwareAddress_Type.__name__=_O
_DhcpLeaseHardwareAddress_Object=MibTableColumn
dhcpLeaseHardwareAddress=_DhcpLeaseHardwareAddress_Object((1,3,6,1,4,1,5504,4,1,11,6,1,5),_DhcpLeaseHardwareAddress_Type())
dhcpLeaseHardwareAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseHardwareAddress.setStatus(_A)
class _DhcpLeaseFlags_Type(Bits):namedValues=NamedValues(*(('static',0),('bootp',1),('unused2',2),('unused3',3),('abandoned',4),('zhoneCPE',5)))
_DhcpLeaseFlags_Type.__name__='Bits'
_DhcpLeaseFlags_Object=MibTableColumn
dhcpLeaseFlags=_DhcpLeaseFlags_Object((1,3,6,1,4,1,5504,4,1,11,6,1,6),_DhcpLeaseFlags_Type())
dhcpLeaseFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseFlags.setStatus(_A)
class _DhcpLeaseClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DhcpLeaseClientId_Type.__name__=_L
_DhcpLeaseClientId_Object=MibTableColumn
dhcpLeaseClientId=_DhcpLeaseClientId_Object((1,3,6,1,4,1,5504,4,1,11,6,1,7),_DhcpLeaseClientId_Type())
dhcpLeaseClientId.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseClientId.setStatus(_A)
class _DhcpLeaseClientHostname_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DhcpLeaseClientHostname_Type.__name__=_J
_DhcpLeaseClientHostname_Object=MibTableColumn
dhcpLeaseClientHostname=_DhcpLeaseClientHostname_Object((1,3,6,1,4,1,5504,4,1,11,6,1,8),_DhcpLeaseClientHostname_Type())
dhcpLeaseClientHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseClientHostname.setStatus(_A)
class _DhcpLeaseHostname_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DhcpLeaseHostname_Type.__name__=_J
_DhcpLeaseHostname_Object=MibTableColumn
dhcpLeaseHostname=_DhcpLeaseHostname_Object((1,3,6,1,4,1,5504,4,1,11,6,1,9),_DhcpLeaseHostname_Type())
dhcpLeaseHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseHostname.setStatus(_A)
class _DhcpLeaseDDNSFwdName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DhcpLeaseDDNSFwdName_Type.__name__=_J
_DhcpLeaseDDNSFwdName_Object=MibTableColumn
dhcpLeaseDDNSFwdName=_DhcpLeaseDDNSFwdName_Object((1,3,6,1,4,1,5504,4,1,11,6,1,10),_DhcpLeaseDDNSFwdName_Type())
dhcpLeaseDDNSFwdName.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseDDNSFwdName.setStatus(_A)
class _DhcpLeaseDDNSRevName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DhcpLeaseDDNSRevName_Type.__name__=_J
_DhcpLeaseDDNSRevName_Object=MibTableColumn
dhcpLeaseDDNSRevName=_DhcpLeaseDDNSRevName_Object((1,3,6,1,4,1,5504,4,1,11,6,1,11),_DhcpLeaseDDNSRevName_Type())
dhcpLeaseDDNSRevName.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseDDNSRevName.setStatus(_A)
_DhcpLeaseRowStatus_Type=ZhoneRowStatus
_DhcpLeaseRowStatus_Object=MibTableColumn
dhcpLeaseRowStatus=_DhcpLeaseRowStatus_Object((1,3,6,1,4,1,5504,4,1,11,6,1,12),_DhcpLeaseRowStatus_Type())
dhcpLeaseRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseRowStatus.setStatus(_A)
class _DhcpServerNextGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpServerNextGroupIndex_Type.__name__=_D
_DhcpServerNextGroupIndex_Object=MibScalar
dhcpServerNextGroupIndex=_DhcpServerNextGroupIndex_Object((1,3,6,1,4,1,5504,4,1,11,7),_DhcpServerNextGroupIndex_Type())
dhcpServerNextGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpServerNextGroupIndex.setStatus(_A)
_DhcpServerGroupTable_Object=MibTable
dhcpServerGroupTable=_DhcpServerGroupTable_Object((1,3,6,1,4,1,5504,4,1,11,8))
if mibBuilder.loadTexts:dhcpServerGroupTable.setStatus(_A)
_DhcpServerGroupEntry_Object=MibTableRow
dhcpServerGroupEntry=_DhcpServerGroupEntry_Object((1,3,6,1,4,1,5504,4,1,11,8,1))
dhcpServerGroupEntry.setIndexNames((0,_G,_g))
if mibBuilder.loadTexts:dhcpServerGroupEntry.setStatus(_A)
class _DhcpGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpGroupIndex_Type.__name__=_D
_DhcpGroupIndex_Object=MibTableColumn
dhcpGroupIndex=_DhcpGroupIndex_Object((1,3,6,1,4,1,5504,4,1,11,8,1,1),_DhcpGroupIndex_Type())
dhcpGroupIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dhcpGroupIndex.setStatus(_A)
_DhcpGroupName_Type=ZhoneAdminString
_DhcpGroupName_Object=MibTableColumn
dhcpGroupName=_DhcpGroupName_Object((1,3,6,1,4,1,5504,4,1,11,8,1,2),_DhcpGroupName_Type())
dhcpGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpGroupName.setStatus(_A)
_DhcpGroupDomain_Type=ZhoneRDIndex
_DhcpGroupDomain_Object=MibTableColumn
dhcpGroupDomain=_DhcpGroupDomain_Object((1,3,6,1,4,1,5504,4,1,11,8,1,3),_DhcpGroupDomain_Type())
dhcpGroupDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpGroupDomain.setStatus(_A)
class _DhcpGroupVendorMatchString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DhcpGroupVendorMatchString_Type.__name__=_L
_DhcpGroupVendorMatchString_Object=MibTableColumn
dhcpGroupVendorMatchString=_DhcpGroupVendorMatchString_Object((1,3,6,1,4,1,5504,4,1,11,8,1,4),_DhcpGroupVendorMatchString_Type())
dhcpGroupVendorMatchString.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpGroupVendorMatchString.setStatus(_A)
class _DhcpGroupVendorMatchOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DhcpGroupVendorMatchOffset_Type.__name__=_D
_DhcpGroupVendorMatchOffset_Object=MibTableColumn
dhcpGroupVendorMatchOffset=_DhcpGroupVendorMatchOffset_Object((1,3,6,1,4,1,5504,4,1,11,8,1,5),_DhcpGroupVendorMatchOffset_Type())
dhcpGroupVendorMatchOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpGroupVendorMatchOffset.setStatus(_A)
class _DhcpGroupVendorMatchLength_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_DhcpGroupVendorMatchLength_Type.__name__=_D
_DhcpGroupVendorMatchLength_Object=MibTableColumn
dhcpGroupVendorMatchLength=_DhcpGroupVendorMatchLength_Object((1,3,6,1,4,1,5504,4,1,11,8,1,6),_DhcpGroupVendorMatchLength_Type())
dhcpGroupVendorMatchLength.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpGroupVendorMatchLength.setStatus(_A)
class _DhcpGroupClientMatchString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DhcpGroupClientMatchString_Type.__name__=_L
_DhcpGroupClientMatchString_Object=MibTableColumn
dhcpGroupClientMatchString=_DhcpGroupClientMatchString_Object((1,3,6,1,4,1,5504,4,1,11,8,1,7),_DhcpGroupClientMatchString_Type())
dhcpGroupClientMatchString.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpGroupClientMatchString.setStatus(_A)
class _DhcpGroupClientMatchOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DhcpGroupClientMatchOffset_Type.__name__=_D
_DhcpGroupClientMatchOffset_Object=MibTableColumn
dhcpGroupClientMatchOffset=_DhcpGroupClientMatchOffset_Object((1,3,6,1,4,1,5504,4,1,11,8,1,8),_DhcpGroupClientMatchOffset_Type())
dhcpGroupClientMatchOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpGroupClientMatchOffset.setStatus(_A)
class _DhcpGroupClientMatchLength_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_DhcpGroupClientMatchLength_Type.__name__=_D
_DhcpGroupClientMatchLength_Object=MibTableColumn
dhcpGroupClientMatchLength=_DhcpGroupClientMatchLength_Object((1,3,6,1,4,1,5504,4,1,11,8,1,9),_DhcpGroupClientMatchLength_Type())
dhcpGroupClientMatchLength.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpGroupClientMatchLength.setStatus(_A)
_DhcpGroupRowStatus_Type=ZhoneRowStatus
_DhcpGroupRowStatus_Object=MibTableColumn
dhcpGroupRowStatus=_DhcpGroupRowStatus_Object((1,3,6,1,4,1,5504,4,1,11,8,1,10),_DhcpGroupRowStatus_Type())
dhcpGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpGroupRowStatus.setStatus(_A)
_DhcpServerGroupOptionTable_Object=MibTable
dhcpServerGroupOptionTable=_DhcpServerGroupOptionTable_Object((1,3,6,1,4,1,5504,4,1,11,9))
if mibBuilder.loadTexts:dhcpServerGroupOptionTable.setStatus(_A)
_DhcpServerGroupOptionEntry_Object=MibTableRow
dhcpServerGroupOptionEntry=_DhcpServerGroupOptionEntry_Object((1,3,6,1,4,1,5504,4,1,11,9,1))
if mibBuilder.loadTexts:dhcpServerGroupOptionEntry.setStatus(_A)
class _DhcpGroupOptionDefaultLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_DhcpGroupOptionDefaultLeaseTime_Type.__name__=_D
_DhcpGroupOptionDefaultLeaseTime_Object=MibTableColumn
dhcpGroupOptionDefaultLeaseTime=_DhcpGroupOptionDefaultLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,9,1,1),_DhcpGroupOptionDefaultLeaseTime_Type())
dhcpGroupOptionDefaultLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpGroupOptionDefaultLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpGroupOptionDefaultLeaseTime.setUnits(_H)
class _DhcpGroupOptionMinLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_DhcpGroupOptionMinLeaseTime_Type.__name__=_D
_DhcpGroupOptionMinLeaseTime_Object=MibTableColumn
dhcpGroupOptionMinLeaseTime=_DhcpGroupOptionMinLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,9,1,2),_DhcpGroupOptionMinLeaseTime_Type())
dhcpGroupOptionMinLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpGroupOptionMinLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpGroupOptionMinLeaseTime.setUnits(_H)
class _DhcpGroupOptionMaxLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_DhcpGroupOptionMaxLeaseTime_Type.__name__=_D
_DhcpGroupOptionMaxLeaseTime_Object=MibTableColumn
dhcpGroupOptionMaxLeaseTime=_DhcpGroupOptionMaxLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,9,1,3),_DhcpGroupOptionMaxLeaseTime_Type())
dhcpGroupOptionMaxLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpGroupOptionMaxLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpGroupOptionMaxLeaseTime.setUnits(_H)
_DhcpGroupOptionBootFile_Type=ZhoneFileName
_DhcpGroupOptionBootFile_Object=MibTableColumn
dhcpGroupOptionBootFile=_DhcpGroupOptionBootFile_Object((1,3,6,1,4,1,5504,4,1,11,9,1,4),_DhcpGroupOptionBootFile_Type())
dhcpGroupOptionBootFile.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpGroupOptionBootFile.setStatus(_A)
_DhcpGroupOptionBootServer_Type=IpAddress
_DhcpGroupOptionBootServer_Object=MibTableColumn
dhcpGroupOptionBootServer=_DhcpGroupOptionBootServer_Object((1,3,6,1,4,1,5504,4,1,11,9,1,5),_DhcpGroupOptionBootServer_Type())
dhcpGroupOptionBootServer.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpGroupOptionBootServer.setStatus(_A)
_DhcpGroupOptionDefaultRouter_Type=IpAddress
_DhcpGroupOptionDefaultRouter_Object=MibTableColumn
dhcpGroupOptionDefaultRouter=_DhcpGroupOptionDefaultRouter_Object((1,3,6,1,4,1,5504,4,1,11,9,1,6),_DhcpGroupOptionDefaultRouter_Type())
dhcpGroupOptionDefaultRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpGroupOptionDefaultRouter.setStatus(_A)
_DhcpGroupOptionPrimaryNameServer_Type=IpAddress
_DhcpGroupOptionPrimaryNameServer_Object=MibTableColumn
dhcpGroupOptionPrimaryNameServer=_DhcpGroupOptionPrimaryNameServer_Object((1,3,6,1,4,1,5504,4,1,11,9,1,7),_DhcpGroupOptionPrimaryNameServer_Type())
dhcpGroupOptionPrimaryNameServer.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpGroupOptionPrimaryNameServer.setStatus(_A)
_DhcpGroupOptionSecondaryNameServer_Type=IpAddress
_DhcpGroupOptionSecondaryNameServer_Object=MibTableColumn
dhcpGroupOptionSecondaryNameServer=_DhcpGroupOptionSecondaryNameServer_Object((1,3,6,1,4,1,5504,4,1,11,9,1,8),_DhcpGroupOptionSecondaryNameServer_Type())
dhcpGroupOptionSecondaryNameServer.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpGroupOptionSecondaryNameServer.setStatus(_A)
class _DhcpGroupOptionDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DhcpGroupOptionDomainName_Type.__name__=_J
_DhcpGroupOptionDomainName_Object=MibTableColumn
dhcpGroupOptionDomainName=_DhcpGroupOptionDomainName_Object((1,3,6,1,4,1,5504,4,1,11,9,1,9),_DhcpGroupOptionDomainName_Type())
dhcpGroupOptionDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpGroupOptionDomainName.setStatus(_A)
class _DhcpServerNextSubnetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpServerNextSubnetIndex_Type.__name__=_D
_DhcpServerNextSubnetIndex_Object=MibScalar
dhcpServerNextSubnetIndex=_DhcpServerNextSubnetIndex_Object((1,3,6,1,4,1,5504,4,1,11,10),_DhcpServerNextSubnetIndex_Type())
dhcpServerNextSubnetIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpServerNextSubnetIndex.setStatus(_A)
_DhcpServerSubnetTable_Object=MibTable
dhcpServerSubnetTable=_DhcpServerSubnetTable_Object((1,3,6,1,4,1,5504,4,1,11,11))
if mibBuilder.loadTexts:dhcpServerSubnetTable.setStatus(_A)
_DhcpServerSubnetEntry_Object=MibTableRow
dhcpServerSubnetEntry=_DhcpServerSubnetEntry_Object((1,3,6,1,4,1,5504,4,1,11,11,1))
dhcpServerSubnetEntry.setIndexNames((0,_G,_h))
if mibBuilder.loadTexts:dhcpServerSubnetEntry.setStatus(_A)
class _DhcpSubnetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpSubnetIndex_Type.__name__=_D
_DhcpSubnetIndex_Object=MibTableColumn
dhcpSubnetIndex=_DhcpSubnetIndex_Object((1,3,6,1,4,1,5504,4,1,11,11,1,1),_DhcpSubnetIndex_Type())
dhcpSubnetIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dhcpSubnetIndex.setStatus(_A)
_DhcpSubnetNetwork_Type=IpAddress
_DhcpSubnetNetwork_Object=MibTableColumn
dhcpSubnetNetwork=_DhcpSubnetNetwork_Object((1,3,6,1,4,1,5504,4,1,11,11,1,2),_DhcpSubnetNetwork_Type())
dhcpSubnetNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetNetwork.setStatus(_A)
_DhcpSubnetNetmask_Type=IpAddress
_DhcpSubnetNetmask_Object=MibTableColumn
dhcpSubnetNetmask=_DhcpSubnetNetmask_Object((1,3,6,1,4,1,5504,4,1,11,11,1,3),_DhcpSubnetNetmask_Type())
dhcpSubnetNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetNetmask.setStatus(_A)
_DhcpSubnetDomain_Type=ZhoneRDIndex
_DhcpSubnetDomain_Object=MibTableColumn
dhcpSubnetDomain=_DhcpSubnetDomain_Object((1,3,6,1,4,1,5504,4,1,11,11,1,4),_DhcpSubnetDomain_Type())
dhcpSubnetDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetDomain.setStatus(_A)
_DhcpSubnetRange1Start_Type=IpAddress
_DhcpSubnetRange1Start_Object=MibTableColumn
dhcpSubnetRange1Start=_DhcpSubnetRange1Start_Object((1,3,6,1,4,1,5504,4,1,11,11,1,5),_DhcpSubnetRange1Start_Type())
dhcpSubnetRange1Start.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetRange1Start.setStatus(_A)
_DhcpSubnetRange1End_Type=IpAddress
_DhcpSubnetRange1End_Object=MibTableColumn
dhcpSubnetRange1End=_DhcpSubnetRange1End_Object((1,3,6,1,4,1,5504,4,1,11,11,1,6),_DhcpSubnetRange1End_Type())
dhcpSubnetRange1End.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetRange1End.setStatus(_A)
class _DhcpSubnetRange2Start_Type(IpAddress):defaultHexValue=_I
_DhcpSubnetRange2Start_Type.__name__=_F
_DhcpSubnetRange2Start_Object=MibTableColumn
dhcpSubnetRange2Start=_DhcpSubnetRange2Start_Object((1,3,6,1,4,1,5504,4,1,11,11,1,7),_DhcpSubnetRange2Start_Type())
dhcpSubnetRange2Start.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetRange2Start.setStatus(_A)
class _DhcpSubnetRange2End_Type(IpAddress):defaultHexValue=_I
_DhcpSubnetRange2End_Type.__name__=_F
_DhcpSubnetRange2End_Object=MibTableColumn
dhcpSubnetRange2End=_DhcpSubnetRange2End_Object((1,3,6,1,4,1,5504,4,1,11,11,1,8),_DhcpSubnetRange2End_Type())
dhcpSubnetRange2End.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetRange2End.setStatus(_A)
class _DhcpSubnetRange3Start_Type(IpAddress):defaultHexValue=_I
_DhcpSubnetRange3Start_Type.__name__=_F
_DhcpSubnetRange3Start_Object=MibTableColumn
dhcpSubnetRange3Start=_DhcpSubnetRange3Start_Object((1,3,6,1,4,1,5504,4,1,11,11,1,9),_DhcpSubnetRange3Start_Type())
dhcpSubnetRange3Start.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetRange3Start.setStatus(_A)
class _DhcpSubnetRange3End_Type(IpAddress):defaultHexValue=_I
_DhcpSubnetRange3End_Type.__name__=_F
_DhcpSubnetRange3End_Object=MibTableColumn
dhcpSubnetRange3End=_DhcpSubnetRange3End_Object((1,3,6,1,4,1,5504,4,1,11,11,1,10),_DhcpSubnetRange3End_Type())
dhcpSubnetRange3End.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetRange3End.setStatus(_A)
class _DhcpSubnetRange4Start_Type(IpAddress):defaultHexValue=_I
_DhcpSubnetRange4Start_Type.__name__=_F
_DhcpSubnetRange4Start_Object=MibTableColumn
dhcpSubnetRange4Start=_DhcpSubnetRange4Start_Object((1,3,6,1,4,1,5504,4,1,11,11,1,11),_DhcpSubnetRange4Start_Type())
dhcpSubnetRange4Start.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetRange4Start.setStatus(_A)
class _DhcpSubnetRange4End_Type(IpAddress):defaultHexValue=_I
_DhcpSubnetRange4End_Type.__name__=_F
_DhcpSubnetRange4End_Object=MibTableColumn
dhcpSubnetRange4End=_DhcpSubnetRange4End_Object((1,3,6,1,4,1,5504,4,1,11,11,1,12),_DhcpSubnetRange4End_Type())
dhcpSubnetRange4End.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetRange4End.setStatus(_A)
_DhcpSubnetRowStatus_Type=ZhoneRowStatus
_DhcpSubnetRowStatus_Object=MibTableColumn
dhcpSubnetRowStatus=_DhcpSubnetRowStatus_Object((1,3,6,1,4,1,5504,4,1,11,11,1,13),_DhcpSubnetRowStatus_Type())
dhcpSubnetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetRowStatus.setStatus(_A)
class _DhcpSubnetGroup2_Type(Integer32):defaultValue=0
_DhcpSubnetGroup2_Type.__name__=_D
_DhcpSubnetGroup2_Object=MibTableColumn
dhcpSubnetGroup2=_DhcpSubnetGroup2_Object((1,3,6,1,4,1,5504,4,1,11,11,1,14),_DhcpSubnetGroup2_Type())
dhcpSubnetGroup2.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSubnetGroup2.setStatus(_A)
class _DhcpStickyAddr_Type(TruthValue):defaultValue=1
_DhcpStickyAddr_Type.__name__=_R
_DhcpStickyAddr_Object=MibTableColumn
dhcpStickyAddr=_DhcpStickyAddr_Object((1,3,6,1,4,1,5504,4,1,11,11,1,15),_DhcpStickyAddr_Type())
dhcpStickyAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpStickyAddr.setStatus(_A)
class _DhcpSubnetExternalServer_Type(IpAddress):defaultHexValue=_I
_DhcpSubnetExternalServer_Type.__name__=_F
_DhcpSubnetExternalServer_Object=MibTableColumn
dhcpSubnetExternalServer=_DhcpSubnetExternalServer_Object((1,3,6,1,4,1,5504,4,1,11,11,1,16),_DhcpSubnetExternalServer_Type())
dhcpSubnetExternalServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetExternalServer.setStatus(_A)
class _DhcpSubnetExternalServerAlt_Type(IpAddress):defaultHexValue=_I
_DhcpSubnetExternalServerAlt_Type.__name__=_F
_DhcpSubnetExternalServerAlt_Object=MibTableColumn
dhcpSubnetExternalServerAlt=_DhcpSubnetExternalServerAlt_Object((1,3,6,1,4,1,5504,4,1,11,11,1,17),_DhcpSubnetExternalServerAlt_Type())
dhcpSubnetExternalServerAlt.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpSubnetExternalServerAlt.setStatus(_A)
_DhcpServerSubnetOptionTable_Object=MibTable
dhcpServerSubnetOptionTable=_DhcpServerSubnetOptionTable_Object((1,3,6,1,4,1,5504,4,1,11,12))
if mibBuilder.loadTexts:dhcpServerSubnetOptionTable.setStatus(_A)
_DhcpServerSubnetOptionEntry_Object=MibTableRow
dhcpServerSubnetOptionEntry=_DhcpServerSubnetOptionEntry_Object((1,3,6,1,4,1,5504,4,1,11,12,1))
if mibBuilder.loadTexts:dhcpServerSubnetOptionEntry.setStatus(_A)
class _DhcpSubnetOptionDefaultLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_DhcpSubnetOptionDefaultLeaseTime_Type.__name__=_D
_DhcpSubnetOptionDefaultLeaseTime_Object=MibTableColumn
dhcpSubnetOptionDefaultLeaseTime=_DhcpSubnetOptionDefaultLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,12,1,1),_DhcpSubnetOptionDefaultLeaseTime_Type())
dhcpSubnetOptionDefaultLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSubnetOptionDefaultLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpSubnetOptionDefaultLeaseTime.setUnits(_H)
class _DhcpSubnetOptionMinLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_DhcpSubnetOptionMinLeaseTime_Type.__name__=_D
_DhcpSubnetOptionMinLeaseTime_Object=MibTableColumn
dhcpSubnetOptionMinLeaseTime=_DhcpSubnetOptionMinLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,12,1,2),_DhcpSubnetOptionMinLeaseTime_Type())
dhcpSubnetOptionMinLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSubnetOptionMinLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpSubnetOptionMinLeaseTime.setUnits(_H)
class _DhcpSubnetOptionMaxLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_DhcpSubnetOptionMaxLeaseTime_Type.__name__=_D
_DhcpSubnetOptionMaxLeaseTime_Object=MibTableColumn
dhcpSubnetOptionMaxLeaseTime=_DhcpSubnetOptionMaxLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,12,1,3),_DhcpSubnetOptionMaxLeaseTime_Type())
dhcpSubnetOptionMaxLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSubnetOptionMaxLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpSubnetOptionMaxLeaseTime.setUnits(_H)
_DhcpSubnetOptionBootFile_Type=ZhoneFileName
_DhcpSubnetOptionBootFile_Object=MibTableColumn
dhcpSubnetOptionBootFile=_DhcpSubnetOptionBootFile_Object((1,3,6,1,4,1,5504,4,1,11,12,1,4),_DhcpSubnetOptionBootFile_Type())
dhcpSubnetOptionBootFile.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSubnetOptionBootFile.setStatus(_A)
_DhcpSubnetOptionBootServer_Type=IpAddress
_DhcpSubnetOptionBootServer_Object=MibTableColumn
dhcpSubnetOptionBootServer=_DhcpSubnetOptionBootServer_Object((1,3,6,1,4,1,5504,4,1,11,12,1,5),_DhcpSubnetOptionBootServer_Type())
dhcpSubnetOptionBootServer.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSubnetOptionBootServer.setStatus(_A)
_DhcpSubnetOptionDefaultRouter_Type=IpAddress
_DhcpSubnetOptionDefaultRouter_Object=MibTableColumn
dhcpSubnetOptionDefaultRouter=_DhcpSubnetOptionDefaultRouter_Object((1,3,6,1,4,1,5504,4,1,11,12,1,6),_DhcpSubnetOptionDefaultRouter_Type())
dhcpSubnetOptionDefaultRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSubnetOptionDefaultRouter.setStatus(_A)
_DhcpSubnetOptionPrimaryNameServer_Type=IpAddress
_DhcpSubnetOptionPrimaryNameServer_Object=MibTableColumn
dhcpSubnetOptionPrimaryNameServer=_DhcpSubnetOptionPrimaryNameServer_Object((1,3,6,1,4,1,5504,4,1,11,12,1,7),_DhcpSubnetOptionPrimaryNameServer_Type())
dhcpSubnetOptionPrimaryNameServer.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSubnetOptionPrimaryNameServer.setStatus(_A)
_DhcpSubnetOptionSecondaryNameServer_Type=IpAddress
_DhcpSubnetOptionSecondaryNameServer_Object=MibTableColumn
dhcpSubnetOptionSecondaryNameServer=_DhcpSubnetOptionSecondaryNameServer_Object((1,3,6,1,4,1,5504,4,1,11,12,1,8),_DhcpSubnetOptionSecondaryNameServer_Type())
dhcpSubnetOptionSecondaryNameServer.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSubnetOptionSecondaryNameServer.setStatus(_A)
class _DhcpSubnetOptionDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DhcpSubnetOptionDomainName_Type.__name__=_J
_DhcpSubnetOptionDomainName_Object=MibTableColumn
dhcpSubnetOptionDomainName=_DhcpSubnetOptionDomainName_Object((1,3,6,1,4,1,5504,4,1,11,12,1,9),_DhcpSubnetOptionDomainName_Type())
dhcpSubnetOptionDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpSubnetOptionDomainName.setStatus(_A)
class _DhcpServerNextHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpServerNextHostIndex_Type.__name__=_D
_DhcpServerNextHostIndex_Object=MibScalar
dhcpServerNextHostIndex=_DhcpServerNextHostIndex_Object((1,3,6,1,4,1,5504,4,1,11,13),_DhcpServerNextHostIndex_Type())
dhcpServerNextHostIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpServerNextHostIndex.setStatus(_A)
_DhcpServerHostTable_Object=MibTable
dhcpServerHostTable=_DhcpServerHostTable_Object((1,3,6,1,4,1,5504,4,1,11,14))
if mibBuilder.loadTexts:dhcpServerHostTable.setStatus(_A)
_DhcpServerHostEntry_Object=MibTableRow
dhcpServerHostEntry=_DhcpServerHostEntry_Object((1,3,6,1,4,1,5504,4,1,11,14,1))
dhcpServerHostEntry.setIndexNames((0,_G,_i))
if mibBuilder.loadTexts:dhcpServerHostEntry.setStatus(_A)
class _DhcpHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpHostIndex_Type.__name__=_D
_DhcpHostIndex_Object=MibTableColumn
dhcpHostIndex=_DhcpHostIndex_Object((1,3,6,1,4,1,5504,4,1,11,14,1,1),_DhcpHostIndex_Type())
dhcpHostIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dhcpHostIndex.setStatus(_A)
_DhcpHostHostname_Type=ZhoneAdminString
_DhcpHostHostname_Object=MibTableColumn
dhcpHostHostname=_DhcpHostHostname_Object((1,3,6,1,4,1,5504,4,1,11,14,1,2),_DhcpHostHostname_Type())
dhcpHostHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpHostHostname.setStatus(_A)
_DhcpHostDomain_Type=ZhoneRDIndex
_DhcpHostDomain_Object=MibTableColumn
dhcpHostDomain=_DhcpHostDomain_Object((1,3,6,1,4,1,5504,4,1,11,14,1,3),_DhcpHostDomain_Type())
dhcpHostDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpHostDomain.setStatus(_A)
class _DhcpHostHardwareAddress_Type(PhysAddress):defaultHexValue='0000';subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DhcpHostHardwareAddress_Type.__name__=_O
_DhcpHostHardwareAddress_Object=MibTableColumn
dhcpHostHardwareAddress=_DhcpHostHardwareAddress_Object((1,3,6,1,4,1,5504,4,1,11,14,1,4),_DhcpHostHardwareAddress_Type())
dhcpHostHardwareAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpHostHardwareAddress.setStatus(_A)
class _DhcpHostClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DhcpHostClientId_Type.__name__=_L
_DhcpHostClientId_Object=MibTableColumn
dhcpHostClientId=_DhcpHostClientId_Object((1,3,6,1,4,1,5504,4,1,11,14,1,5),_DhcpHostClientId_Type())
dhcpHostClientId.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpHostClientId.setStatus(_A)
class _DhcpHostIpAddress1_Type(IpAddress):defaultHexValue=_I
_DhcpHostIpAddress1_Type.__name__=_F
_DhcpHostIpAddress1_Object=MibTableColumn
dhcpHostIpAddress1=_DhcpHostIpAddress1_Object((1,3,6,1,4,1,5504,4,1,11,14,1,6),_DhcpHostIpAddress1_Type())
dhcpHostIpAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpHostIpAddress1.setStatus(_A)
class _DhcpHostIpAddress2_Type(IpAddress):defaultHexValue=_I
_DhcpHostIpAddress2_Type.__name__=_F
_DhcpHostIpAddress2_Object=MibTableColumn
dhcpHostIpAddress2=_DhcpHostIpAddress2_Object((1,3,6,1,4,1,5504,4,1,11,14,1,7),_DhcpHostIpAddress2_Type())
dhcpHostIpAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpHostIpAddress2.setStatus(_A)
class _DhcpHostIpAddress3_Type(IpAddress):defaultHexValue=_I
_DhcpHostIpAddress3_Type.__name__=_F
_DhcpHostIpAddress3_Object=MibTableColumn
dhcpHostIpAddress3=_DhcpHostIpAddress3_Object((1,3,6,1,4,1,5504,4,1,11,14,1,8),_DhcpHostIpAddress3_Type())
dhcpHostIpAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpHostIpAddress3.setStatus(_A)
class _DhcpHostIpAddress4_Type(IpAddress):defaultHexValue=_I
_DhcpHostIpAddress4_Type.__name__=_F
_DhcpHostIpAddress4_Object=MibTableColumn
dhcpHostIpAddress4=_DhcpHostIpAddress4_Object((1,3,6,1,4,1,5504,4,1,11,14,1,9),_DhcpHostIpAddress4_Type())
dhcpHostIpAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpHostIpAddress4.setStatus(_A)
_DhcpHostRowStatus_Type=ZhoneRowStatus
_DhcpHostRowStatus_Object=MibTableColumn
dhcpHostRowStatus=_DhcpHostRowStatus_Object((1,3,6,1,4,1,5504,4,1,11,14,1,10),_DhcpHostRowStatus_Type())
dhcpHostRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpHostRowStatus.setStatus(_A)
_DhcpServerHostOptionTable_Object=MibTable
dhcpServerHostOptionTable=_DhcpServerHostOptionTable_Object((1,3,6,1,4,1,5504,4,1,11,15))
if mibBuilder.loadTexts:dhcpServerHostOptionTable.setStatus(_A)
_DhcpServerHostOptionEntry_Object=MibTableRow
dhcpServerHostOptionEntry=_DhcpServerHostOptionEntry_Object((1,3,6,1,4,1,5504,4,1,11,15,1))
if mibBuilder.loadTexts:dhcpServerHostOptionEntry.setStatus(_A)
class _DhcpHostOptionDefaultLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_DhcpHostOptionDefaultLeaseTime_Type.__name__=_D
_DhcpHostOptionDefaultLeaseTime_Object=MibTableColumn
dhcpHostOptionDefaultLeaseTime=_DhcpHostOptionDefaultLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,15,1,1),_DhcpHostOptionDefaultLeaseTime_Type())
dhcpHostOptionDefaultLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpHostOptionDefaultLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpHostOptionDefaultLeaseTime.setUnits(_H)
class _DhcpHostOptionMinLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_DhcpHostOptionMinLeaseTime_Type.__name__=_D
_DhcpHostOptionMinLeaseTime_Object=MibTableColumn
dhcpHostOptionMinLeaseTime=_DhcpHostOptionMinLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,15,1,2),_DhcpHostOptionMinLeaseTime_Type())
dhcpHostOptionMinLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpHostOptionMinLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpHostOptionMinLeaseTime.setUnits(_H)
class _DhcpHostOptionMaxLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_DhcpHostOptionMaxLeaseTime_Type.__name__=_D
_DhcpHostOptionMaxLeaseTime_Object=MibTableColumn
dhcpHostOptionMaxLeaseTime=_DhcpHostOptionMaxLeaseTime_Object((1,3,6,1,4,1,5504,4,1,11,15,1,3),_DhcpHostOptionMaxLeaseTime_Type())
dhcpHostOptionMaxLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpHostOptionMaxLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:dhcpHostOptionMaxLeaseTime.setUnits(_H)
_DhcpHostOptionBootFile_Type=ZhoneFileName
_DhcpHostOptionBootFile_Object=MibTableColumn
dhcpHostOptionBootFile=_DhcpHostOptionBootFile_Object((1,3,6,1,4,1,5504,4,1,11,15,1,4),_DhcpHostOptionBootFile_Type())
dhcpHostOptionBootFile.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpHostOptionBootFile.setStatus(_A)
_DhcpHostOptionBootServer_Type=IpAddress
_DhcpHostOptionBootServer_Object=MibTableColumn
dhcpHostOptionBootServer=_DhcpHostOptionBootServer_Object((1,3,6,1,4,1,5504,4,1,11,15,1,5),_DhcpHostOptionBootServer_Type())
dhcpHostOptionBootServer.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpHostOptionBootServer.setStatus(_A)
_DhcpHostOptionDefaultRouter_Type=IpAddress
_DhcpHostOptionDefaultRouter_Object=MibTableColumn
dhcpHostOptionDefaultRouter=_DhcpHostOptionDefaultRouter_Object((1,3,6,1,4,1,5504,4,1,11,15,1,6),_DhcpHostOptionDefaultRouter_Type())
dhcpHostOptionDefaultRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpHostOptionDefaultRouter.setStatus(_A)
_DhcpHostOptionPrimaryNameServer_Type=IpAddress
_DhcpHostOptionPrimaryNameServer_Object=MibTableColumn
dhcpHostOptionPrimaryNameServer=_DhcpHostOptionPrimaryNameServer_Object((1,3,6,1,4,1,5504,4,1,11,15,1,7),_DhcpHostOptionPrimaryNameServer_Type())
dhcpHostOptionPrimaryNameServer.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpHostOptionPrimaryNameServer.setStatus(_A)
_DhcpHostOptionSecondaryNameServer_Type=IpAddress
_DhcpHostOptionSecondaryNameServer_Object=MibTableColumn
dhcpHostOptionSecondaryNameServer=_DhcpHostOptionSecondaryNameServer_Object((1,3,6,1,4,1,5504,4,1,11,15,1,8),_DhcpHostOptionSecondaryNameServer_Type())
dhcpHostOptionSecondaryNameServer.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpHostOptionSecondaryNameServer.setStatus(_A)
class _DhcpHostOptionDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DhcpHostOptionDomainName_Type.__name__=_J
_DhcpHostOptionDomainName_Object=MibTableColumn
dhcpHostOptionDomainName=_DhcpHostOptionDomainName_Object((1,3,6,1,4,1,5504,4,1,11,15,1,9),_DhcpHostOptionDomainName_Type())
dhcpHostOptionDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpHostOptionDomainName.setStatus(_A)
_DhcpServerStatistics_ObjectIdentity=ObjectIdentity
dhcpServerStatistics=_DhcpServerStatistics_ObjectIdentity((1,3,6,1,4,1,5504,4,1,11,16))
if mibBuilder.loadTexts:dhcpServerStatistics.setStatus(_A)
_ServerSystem_ObjectIdentity=ObjectIdentity
serverSystem=_ServerSystem_ObjectIdentity((1,3,6,1,4,1,5504,4,1,11,16,1))
if mibBuilder.loadTexts:serverSystem.setStatus(_A)
_ServerSystemDescr_Type=ZhoneAdminString
_ServerSystemDescr_Object=MibScalar
serverSystemDescr=_ServerSystemDescr_Object((1,3,6,1,4,1,5504,4,1,11,16,1,1),_ServerSystemDescr_Type())
serverSystemDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:serverSystemDescr.setStatus(_A)
_ServerSystemObjectID_Type=ObjectIdentifier
_ServerSystemObjectID_Object=MibScalar
serverSystemObjectID=_ServerSystemObjectID_Object((1,3,6,1,4,1,5504,4,1,11,16,1,2),_ServerSystemObjectID_Type())
serverSystemObjectID.setMaxAccess(_E)
if mibBuilder.loadTexts:serverSystemObjectID.setStatus(_A)
_ServerUptime_Type=TimeTicks
_ServerUptime_Object=MibScalar
serverUptime=_ServerUptime_Object((1,3,6,1,4,1,5504,4,1,11,16,1,3),_ServerUptime_Type())
serverUptime.setMaxAccess(_E)
if mibBuilder.loadTexts:serverUptime.setStatus(_A)
_ServerActiveShelf_Type=ZhoneShelfValue
_ServerActiveShelf_Object=MibScalar
serverActiveShelf=_ServerActiveShelf_Object((1,3,6,1,4,1,5504,4,1,11,16,1,4),_ServerActiveShelf_Type())
serverActiveShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:serverActiveShelf.setStatus(_A)
_ServerActiveSlot_Type=ZhoneSlotValue
_ServerActiveSlot_Object=MibScalar
serverActiveSlot=_ServerActiveSlot_Object((1,3,6,1,4,1,5504,4,1,11,16,1,5),_ServerActiveSlot_Type())
serverActiveSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:serverActiveSlot.setStatus(_A)
_ServerStandbyShelf_Type=ZhoneShelfValue
_ServerStandbyShelf_Object=MibScalar
serverStandbyShelf=_ServerStandbyShelf_Object((1,3,6,1,4,1,5504,4,1,11,16,1,6),_ServerStandbyShelf_Type())
serverStandbyShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:serverStandbyShelf.setStatus(_A)
_ServerStandbySlot_Type=ZhoneSlotValue
_ServerStandbySlot_Object=MibScalar
serverStandbySlot=_ServerStandbySlot_Object((1,3,6,1,4,1,5504,4,1,11,16,1,7),_ServerStandbySlot_Type())
serverStandbySlot.setMaxAccess(_E)
if mibBuilder.loadTexts:serverStandbySlot.setStatus(_A)
_BootpCountersTable_Object=MibTable
bootpCountersTable=_BootpCountersTable_Object((1,3,6,1,4,1,5504,4,1,11,16,2))
if mibBuilder.loadTexts:bootpCountersTable.setStatus(_A)
_BootpCountersEntry_Object=MibTableRow
bootpCountersEntry=_BootpCountersEntry_Object((1,3,6,1,4,1,5504,4,1,11,16,2,1))
if mibBuilder.loadTexts:bootpCountersEntry.setStatus(_A)
_BootpCountRequests_Type=Counter32
_BootpCountRequests_Object=MibTableColumn
bootpCountRequests=_BootpCountRequests_Object((1,3,6,1,4,1,5504,4,1,11,16,2,1,1),_BootpCountRequests_Type())
bootpCountRequests.setMaxAccess(_E)
if mibBuilder.loadTexts:bootpCountRequests.setStatus(_A)
_BootpCountInvalids_Type=Counter32
_BootpCountInvalids_Object=MibTableColumn
bootpCountInvalids=_BootpCountInvalids_Object((1,3,6,1,4,1,5504,4,1,11,16,2,1,2),_BootpCountInvalids_Type())
bootpCountInvalids.setMaxAccess(_E)
if mibBuilder.loadTexts:bootpCountInvalids.setStatus(_A)
_BootpCountReplies_Type=Counter32
_BootpCountReplies_Object=MibTableColumn
bootpCountReplies=_BootpCountReplies_Object((1,3,6,1,4,1,5504,4,1,11,16,2,1,3),_BootpCountReplies_Type())
bootpCountReplies.setMaxAccess(_E)
if mibBuilder.loadTexts:bootpCountReplies.setStatus(_A)
_BootpCountDroppedUnknownClients_Type=Counter32
_BootpCountDroppedUnknownClients_Object=MibTableColumn
bootpCountDroppedUnknownClients=_BootpCountDroppedUnknownClients_Object((1,3,6,1,4,1,5504,4,1,11,16,2,1,4),_BootpCountDroppedUnknownClients_Type())
bootpCountDroppedUnknownClients.setMaxAccess(_E)
if mibBuilder.loadTexts:bootpCountDroppedUnknownClients.setStatus(_A)
_BootpCountDroppedNotServingSubnet_Type=Counter32
_BootpCountDroppedNotServingSubnet_Object=MibTableColumn
bootpCountDroppedNotServingSubnet=_BootpCountDroppedNotServingSubnet_Object((1,3,6,1,4,1,5504,4,1,11,16,2,1,5),_BootpCountDroppedNotServingSubnet_Type())
bootpCountDroppedNotServingSubnet.setMaxAccess(_E)
if mibBuilder.loadTexts:bootpCountDroppedNotServingSubnet.setStatus(_A)
_DhcpCountersTable_Object=MibTable
dhcpCountersTable=_DhcpCountersTable_Object((1,3,6,1,4,1,5504,4,1,11,16,3))
if mibBuilder.loadTexts:dhcpCountersTable.setStatus(_A)
_DhcpCountersEntry_Object=MibTableRow
dhcpCountersEntry=_DhcpCountersEntry_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1))
if mibBuilder.loadTexts:dhcpCountersEntry.setStatus(_A)
_DhcpCountDiscovers_Type=Counter32
_DhcpCountDiscovers_Object=MibTableColumn
dhcpCountDiscovers=_DhcpCountDiscovers_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,1),_DhcpCountDiscovers_Type())
dhcpCountDiscovers.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountDiscovers.setStatus(_A)
_DhcpCountRequests_Type=Counter32
_DhcpCountRequests_Object=MibTableColumn
dhcpCountRequests=_DhcpCountRequests_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,2),_DhcpCountRequests_Type())
dhcpCountRequests.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountRequests.setStatus(_A)
_DhcpCountReleases_Type=Counter32
_DhcpCountReleases_Object=MibTableColumn
dhcpCountReleases=_DhcpCountReleases_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,3),_DhcpCountReleases_Type())
dhcpCountReleases.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountReleases.setStatus(_A)
_DhcpCountDeclines_Type=Counter32
_DhcpCountDeclines_Object=MibTableColumn
dhcpCountDeclines=_DhcpCountDeclines_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,4),_DhcpCountDeclines_Type())
dhcpCountDeclines.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountDeclines.setStatus(_A)
_DhcpCountInforms_Type=Counter32
_DhcpCountInforms_Object=MibTableColumn
dhcpCountInforms=_DhcpCountInforms_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,5),_DhcpCountInforms_Type())
dhcpCountInforms.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountInforms.setStatus(_A)
_DhcpCountInvalids_Type=Counter32
_DhcpCountInvalids_Object=MibTableColumn
dhcpCountInvalids=_DhcpCountInvalids_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,6),_DhcpCountInvalids_Type())
dhcpCountInvalids.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountInvalids.setStatus(_A)
_DhcpCountOffers_Type=Counter32
_DhcpCountOffers_Object=MibTableColumn
dhcpCountOffers=_DhcpCountOffers_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,7),_DhcpCountOffers_Type())
dhcpCountOffers.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountOffers.setStatus(_A)
_DhcpCountAcks_Type=Counter32
_DhcpCountAcks_Object=MibTableColumn
dhcpCountAcks=_DhcpCountAcks_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,8),_DhcpCountAcks_Type())
dhcpCountAcks.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountAcks.setStatus(_A)
_DhcpCountNacks_Type=Counter32
_DhcpCountNacks_Object=MibTableColumn
dhcpCountNacks=_DhcpCountNacks_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,9),_DhcpCountNacks_Type())
dhcpCountNacks.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountNacks.setStatus(_A)
_DhcpCountDroppedUnknownClient_Type=Counter32
_DhcpCountDroppedUnknownClient_Object=MibTableColumn
dhcpCountDroppedUnknownClient=_DhcpCountDroppedUnknownClient_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,10),_DhcpCountDroppedUnknownClient_Type())
dhcpCountDroppedUnknownClient.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountDroppedUnknownClient.setStatus(_A)
_DhcpCountDroppedNotServingSubnet_Type=Counter32
_DhcpCountDroppedNotServingSubnet_Object=MibTableColumn
dhcpCountDroppedNotServingSubnet=_DhcpCountDroppedNotServingSubnet_Object((1,3,6,1,4,1,5504,4,1,11,16,3,1,11),_DhcpCountDroppedNotServingSubnet_Type())
dhcpCountDroppedNotServingSubnet.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpCountDroppedNotServingSubnet.setStatus(_A)
_DhcpServerConfigurationVersion_Type=Unsigned32
_DhcpServerConfigurationVersion_Object=MibScalar
dhcpServerConfigurationVersion=_DhcpServerConfigurationVersion_Object((1,3,6,1,4,1,5504,4,1,11,17),_DhcpServerConfigurationVersion_Type())
dhcpServerConfigurationVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpServerConfigurationVersion.setStatus('deprecated')
class _DhcpServerRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_DhcpServerRestart_Type.__name__=_D
_DhcpServerRestart_Object=MibScalar
dhcpServerRestart=_DhcpServerRestart_Object((1,3,6,1,4,1,5504,4,1,11,18),_DhcpServerRestart_Type())
dhcpServerRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpServerRestart.setStatus(_A)
dhcpServerGroupEntry.registerAugmentions((_G,_j))
dhcpServerGroupOptionEntry.setIndexNames(*dhcpServerGroupEntry.getIndexNames())
dhcpServerSubnetEntry.registerAugmentions((_G,_k))
dhcpServerSubnetOptionEntry.setIndexNames(*dhcpServerSubnetEntry.getIndexNames())
dhcpServerHostEntry.registerAugmentions((_G,_l))
dhcpServerHostOptionEntry.setIndexNames(*dhcpServerHostEntry.getIndexNames())
rdEntry.registerAugmentions((_G,_m))
bootpCountersEntry.setIndexNames(*rdEntry.getIndexNames())
rdEntry.registerAugmentions((_G,_n))
dhcpCountersEntry.setIndexNames(*rdEntry.getIndexNames())
dhcpTrapZhoneCpeDetected=NotificationType((1,3,6,1,4,1,5504,4,1,11,0,1))
dhcpTrapZhoneCpeDetected.setObjects(*((_M,_Z),(_M,_a),(_M,_X),(_M,_Y),(_K,_W),(_K,_V),(_K,_U),(_G,_o),(_P,_S),(_P,_T),(_b,_c),(_K,_Q)))
if mibBuilder.loadTexts:dhcpTrapZhoneCpeDetected.setStatus(_A)
dhcpTrapZhoneIpAddressUpdate=NotificationType((1,3,6,1,4,1,5504,4,1,11,0,3))
dhcpTrapZhoneIpAddressUpdate.setObjects(*((_G,_p),(_K,_Q)))
if mibBuilder.loadTexts:dhcpTrapZhoneIpAddressUpdate.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'dhcpServer':dhcpServer,'dhcpServerTraps':dhcpServerTraps,'dhcpTrapZhoneCpeDetected':dhcpTrapZhoneCpeDetected,_o:dhcpTrapZhoneCpeSysObjectID,'dhcpTrapZhoneIpAddressUpdate':dhcpTrapZhoneIpAddressUpdate,_p:dhcpTrapZhoneIpInterfaceIndex,'dhcpServerDefaultLeaseTime':dhcpServerDefaultLeaseTime,'dhcpServerDefaultMinLeaseTime':dhcpServerDefaultMinLeaseTime,'dhcpServerDefaultMaxLeaseTime':dhcpServerDefaultMaxLeaseTime,'dhcpServerDefaultReserveStart':dhcpServerDefaultReserveStart,'dhcpServerDefaultReserveEnd':dhcpServerDefaultReserveEnd,'dhcpServerLeaseTable':dhcpServerLeaseTable,'dhcpServerLeaseEntry':dhcpServerLeaseEntry,_e:dhcpLeaseDomain,_f:dhcpLeaseIpAddress,'dhcpLeaseStarts':dhcpLeaseStarts,'dhcpLeaseEnds':dhcpLeaseEnds,'dhcpLeaseHardwareAddress':dhcpLeaseHardwareAddress,'dhcpLeaseFlags':dhcpLeaseFlags,'dhcpLeaseClientId':dhcpLeaseClientId,'dhcpLeaseClientHostname':dhcpLeaseClientHostname,'dhcpLeaseHostname':dhcpLeaseHostname,'dhcpLeaseDDNSFwdName':dhcpLeaseDDNSFwdName,'dhcpLeaseDDNSRevName':dhcpLeaseDDNSRevName,'dhcpLeaseRowStatus':dhcpLeaseRowStatus,'dhcpServerNextGroupIndex':dhcpServerNextGroupIndex,'dhcpServerGroupTable':dhcpServerGroupTable,'dhcpServerGroupEntry':dhcpServerGroupEntry,_g:dhcpGroupIndex,'dhcpGroupName':dhcpGroupName,'dhcpGroupDomain':dhcpGroupDomain,'dhcpGroupVendorMatchString':dhcpGroupVendorMatchString,'dhcpGroupVendorMatchOffset':dhcpGroupVendorMatchOffset,'dhcpGroupVendorMatchLength':dhcpGroupVendorMatchLength,'dhcpGroupClientMatchString':dhcpGroupClientMatchString,'dhcpGroupClientMatchOffset':dhcpGroupClientMatchOffset,'dhcpGroupClientMatchLength':dhcpGroupClientMatchLength,'dhcpGroupRowStatus':dhcpGroupRowStatus,'dhcpServerGroupOptionTable':dhcpServerGroupOptionTable,_j:dhcpServerGroupOptionEntry,'dhcpGroupOptionDefaultLeaseTime':dhcpGroupOptionDefaultLeaseTime,'dhcpGroupOptionMinLeaseTime':dhcpGroupOptionMinLeaseTime,'dhcpGroupOptionMaxLeaseTime':dhcpGroupOptionMaxLeaseTime,'dhcpGroupOptionBootFile':dhcpGroupOptionBootFile,'dhcpGroupOptionBootServer':dhcpGroupOptionBootServer,'dhcpGroupOptionDefaultRouter':dhcpGroupOptionDefaultRouter,'dhcpGroupOptionPrimaryNameServer':dhcpGroupOptionPrimaryNameServer,'dhcpGroupOptionSecondaryNameServer':dhcpGroupOptionSecondaryNameServer,'dhcpGroupOptionDomainName':dhcpGroupOptionDomainName,'dhcpServerNextSubnetIndex':dhcpServerNextSubnetIndex,'dhcpServerSubnetTable':dhcpServerSubnetTable,'dhcpServerSubnetEntry':dhcpServerSubnetEntry,_h:dhcpSubnetIndex,'dhcpSubnetNetwork':dhcpSubnetNetwork,'dhcpSubnetNetmask':dhcpSubnetNetmask,'dhcpSubnetDomain':dhcpSubnetDomain,'dhcpSubnetRange1Start':dhcpSubnetRange1Start,'dhcpSubnetRange1End':dhcpSubnetRange1End,'dhcpSubnetRange2Start':dhcpSubnetRange2Start,'dhcpSubnetRange2End':dhcpSubnetRange2End,'dhcpSubnetRange3Start':dhcpSubnetRange3Start,'dhcpSubnetRange3End':dhcpSubnetRange3End,'dhcpSubnetRange4Start':dhcpSubnetRange4Start,'dhcpSubnetRange4End':dhcpSubnetRange4End,'dhcpSubnetRowStatus':dhcpSubnetRowStatus,'dhcpSubnetGroup2':dhcpSubnetGroup2,'dhcpStickyAddr':dhcpStickyAddr,'dhcpSubnetExternalServer':dhcpSubnetExternalServer,'dhcpSubnetExternalServerAlt':dhcpSubnetExternalServerAlt,'dhcpServerSubnetOptionTable':dhcpServerSubnetOptionTable,_k:dhcpServerSubnetOptionEntry,'dhcpSubnetOptionDefaultLeaseTime':dhcpSubnetOptionDefaultLeaseTime,'dhcpSubnetOptionMinLeaseTime':dhcpSubnetOptionMinLeaseTime,'dhcpSubnetOptionMaxLeaseTime':dhcpSubnetOptionMaxLeaseTime,'dhcpSubnetOptionBootFile':dhcpSubnetOptionBootFile,'dhcpSubnetOptionBootServer':dhcpSubnetOptionBootServer,'dhcpSubnetOptionDefaultRouter':dhcpSubnetOptionDefaultRouter,'dhcpSubnetOptionPrimaryNameServer':dhcpSubnetOptionPrimaryNameServer,'dhcpSubnetOptionSecondaryNameServer':dhcpSubnetOptionSecondaryNameServer,'dhcpSubnetOptionDomainName':dhcpSubnetOptionDomainName,'dhcpServerNextHostIndex':dhcpServerNextHostIndex,'dhcpServerHostTable':dhcpServerHostTable,'dhcpServerHostEntry':dhcpServerHostEntry,_i:dhcpHostIndex,'dhcpHostHostname':dhcpHostHostname,'dhcpHostDomain':dhcpHostDomain,'dhcpHostHardwareAddress':dhcpHostHardwareAddress,'dhcpHostClientId':dhcpHostClientId,'dhcpHostIpAddress1':dhcpHostIpAddress1,'dhcpHostIpAddress2':dhcpHostIpAddress2,'dhcpHostIpAddress3':dhcpHostIpAddress3,'dhcpHostIpAddress4':dhcpHostIpAddress4,'dhcpHostRowStatus':dhcpHostRowStatus,'dhcpServerHostOptionTable':dhcpServerHostOptionTable,_l:dhcpServerHostOptionEntry,'dhcpHostOptionDefaultLeaseTime':dhcpHostOptionDefaultLeaseTime,'dhcpHostOptionMinLeaseTime':dhcpHostOptionMinLeaseTime,'dhcpHostOptionMaxLeaseTime':dhcpHostOptionMaxLeaseTime,'dhcpHostOptionBootFile':dhcpHostOptionBootFile,'dhcpHostOptionBootServer':dhcpHostOptionBootServer,'dhcpHostOptionDefaultRouter':dhcpHostOptionDefaultRouter,'dhcpHostOptionPrimaryNameServer':dhcpHostOptionPrimaryNameServer,'dhcpHostOptionSecondaryNameServer':dhcpHostOptionSecondaryNameServer,'dhcpHostOptionDomainName':dhcpHostOptionDomainName,'dhcpServerStatistics':dhcpServerStatistics,'serverSystem':serverSystem,'serverSystemDescr':serverSystemDescr,'serverSystemObjectID':serverSystemObjectID,'serverUptime':serverUptime,'serverActiveShelf':serverActiveShelf,'serverActiveSlot':serverActiveSlot,'serverStandbyShelf':serverStandbyShelf,'serverStandbySlot':serverStandbySlot,'bootpCountersTable':bootpCountersTable,_m:bootpCountersEntry,'bootpCountRequests':bootpCountRequests,'bootpCountInvalids':bootpCountInvalids,'bootpCountReplies':bootpCountReplies,'bootpCountDroppedUnknownClients':bootpCountDroppedUnknownClients,'bootpCountDroppedNotServingSubnet':bootpCountDroppedNotServingSubnet,'dhcpCountersTable':dhcpCountersTable,_n:dhcpCountersEntry,'dhcpCountDiscovers':dhcpCountDiscovers,'dhcpCountRequests':dhcpCountRequests,'dhcpCountReleases':dhcpCountReleases,'dhcpCountDeclines':dhcpCountDeclines,'dhcpCountInforms':dhcpCountInforms,'dhcpCountInvalids':dhcpCountInvalids,'dhcpCountOffers':dhcpCountOffers,'dhcpCountAcks':dhcpCountAcks,'dhcpCountNacks':dhcpCountNacks,'dhcpCountDroppedUnknownClient':dhcpCountDroppedUnknownClient,'dhcpCountDroppedNotServingSubnet':dhcpCountDroppedNotServingSubnet,'dhcpServerConfigurationVersion':dhcpServerConfigurationVersion,'dhcpServerRestart':dhcpServerRestart,'comIpDhcpServer':comIpDhcpServer})