_J='dsSubnetConfRangeIndex'
_I='not-accessible'
_H='dsDomainNameServerIpIdx'
_G='current'
_F='dsSubnetConfIndex'
_E='obsolete'
_D='OctetString'
_C='DASAN-DHCP-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dasanMgmt,=mibBuilder.importSymbols('DASAN-SMI','dasanMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2','snmpModules')
DisplayString,PhysAddress,TextualConvention,TestAndIncr,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TestAndIncr','TimeStamp')
dsDhcpMIBObjects=ModuleIdentity((1,3,6,1,4,1,6296,9,1,1,5))
class SubnetConfIndex(TextualConvention,Integer32):status=_G
class SubnetConfRangeIndex(TextualConvention,Integer32):status=_G
_Org_ObjectIdentity=ObjectIdentity
org=_Org_ObjectIdentity((1,3))
_Dod_ObjectIdentity=ObjectIdentity
dod=_Dod_ObjectIdentity((1,3,6))
_Internet_ObjectIdentity=ObjectIdentity
internet=_Internet_ObjectIdentity((1,3,6,1))
_Directory_ObjectIdentity=ObjectIdentity
directory=_Directory_ObjectIdentity((1,3,6,1,1))
_Mgmt_ObjectIdentity=ObjectIdentity
mgmt=_Mgmt_ObjectIdentity((1,3,6,1,2))
_Transmission_ObjectIdentity=ObjectIdentity
transmission=_Transmission_ObjectIdentity((1,3,6,1,2,1,10))
_Experimental_ObjectIdentity=ObjectIdentity
experimental=_Experimental_ObjectIdentity((1,3,6,1,3))
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Dasan_ObjectIdentity=ObjectIdentity
dasan=_Dasan_ObjectIdentity((1,3,6,1,4,1,6296))
_DasanSwitchMIB_ObjectIdentity=ObjectIdentity
dasanSwitchMIB=_DasanSwitchMIB_ObjectIdentity((1,3,6,1,4,1,6296,9,1))
_DasanSwitchMIBObjects_ObjectIdentity=ObjectIdentity
dasanSwitchMIBObjects=_DasanSwitchMIBObjects_ObjectIdentity((1,3,6,1,4,1,6296,9,1,1))
_DsDhcpDaemonConf_ObjectIdentity=ObjectIdentity
dsDhcpDaemonConf=_DsDhcpDaemonConf_ObjectIdentity((1,3,6,1,4,1,6296,9,1,1,5,1))
_DsDefaultLeaseTime_Type=Integer32
_DsDefaultLeaseTime_Object=MibScalar
dsDefaultLeaseTime=_DsDefaultLeaseTime_Object((1,3,6,1,4,1,6296,9,1,1,5,1,1),_DsDefaultLeaseTime_Type())
dsDefaultLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dsDefaultLeaseTime.setStatus(_A)
_DsMaxLeaseTime_Type=Integer32
_DsMaxLeaseTime_Object=MibScalar
dsMaxLeaseTime=_DsMaxLeaseTime_Object((1,3,6,1,4,1,6296,9,1,1,5,1,2),_DsMaxLeaseTime_Type())
dsMaxLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dsMaxLeaseTime.setStatus(_A)
_DsSubnetMask_Type=IpAddress
_DsSubnetMask_Object=MibScalar
dsSubnetMask=_DsSubnetMask_Object((1,3,6,1,4,1,6296,9,1,1,5,1,3),_DsSubnetMask_Type())
dsSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetMask.setStatus(_A)
_DsBroadcastAddress_Type=IpAddress
_DsBroadcastAddress_Object=MibScalar
dsBroadcastAddress=_DsBroadcastAddress_Object((1,3,6,1,4,1,6296,9,1,1,5,1,4),_DsBroadcastAddress_Type())
dsBroadcastAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dsBroadcastAddress.setStatus(_E)
_DsDomainName_Type=DisplayString
_DsDomainName_Object=MibScalar
dsDomainName=_DsDomainName_Object((1,3,6,1,4,1,6296,9,1,1,5,1,5),_DsDomainName_Type())
dsDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:dsDomainName.setStatus(_A)
_DsDomainNameServerTable_Object=MibTable
dsDomainNameServerTable=_DsDomainNameServerTable_Object((1,3,6,1,4,1,6296,9,1,1,5,1,6))
if mibBuilder.loadTexts:dsDomainNameServerTable.setStatus(_A)
_DsDomainNameServerEntry_Object=MibTableRow
dsDomainNameServerEntry=_DsDomainNameServerEntry_Object((1,3,6,1,4,1,6296,9,1,1,5,1,6,1))
dsDomainNameServerEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:dsDomainNameServerEntry.setStatus(_A)
_DsDomainNameServerIpIdx_Type=Integer32
_DsDomainNameServerIpIdx_Object=MibTableColumn
dsDomainNameServerIpIdx=_DsDomainNameServerIpIdx_Object((1,3,6,1,4,1,6296,9,1,1,5,1,6,1,1),_DsDomainNameServerIpIdx_Type())
dsDomainNameServerIpIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:dsDomainNameServerIpIdx.setStatus(_A)
_DsDomainNameServerIp_Type=IpAddress
_DsDomainNameServerIp_Object=MibTableColumn
dsDomainNameServerIp=_DsDomainNameServerIp_Object((1,3,6,1,4,1,6296,9,1,1,5,1,6,1,2),_DsDomainNameServerIp_Type())
dsDomainNameServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:dsDomainNameServerIp.setStatus(_A)
_DsSubnetConfTable_Object=MibTable
dsSubnetConfTable=_DsSubnetConfTable_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7))
if mibBuilder.loadTexts:dsSubnetConfTable.setStatus(_A)
_DsSubnetConfEntry_Object=MibTableRow
dsSubnetConfEntry=_DsSubnetConfEntry_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1))
dsSubnetConfEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:dsSubnetConfEntry.setStatus(_A)
_DsSubnetConfName_Type=DisplayString
_DsSubnetConfName_Object=MibTableColumn
dsSubnetConfName=_DsSubnetConfName_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,1),_DsSubnetConfName_Type())
dsSubnetConfName.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfName.setStatus(_A)
_DsSubnetConfSubnet_Type=IpAddress
_DsSubnetConfSubnet_Object=MibTableColumn
dsSubnetConfSubnet=_DsSubnetConfSubnet_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,2),_DsSubnetConfSubnet_Type())
dsSubnetConfSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfSubnet.setStatus(_A)
_DsSubnetConfNetmask_Type=IpAddress
_DsSubnetConfNetmask_Object=MibTableColumn
dsSubnetConfNetmask=_DsSubnetConfNetmask_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,3),_DsSubnetConfNetmask_Type())
dsSubnetConfNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfNetmask.setStatus(_A)
_DsSubnetConfBroadcastAddr_Type=IpAddress
_DsSubnetConfBroadcastAddr_Object=MibTableColumn
dsSubnetConfBroadcastAddr=_DsSubnetConfBroadcastAddr_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,4),_DsSubnetConfBroadcastAddr_Type())
dsSubnetConfBroadcastAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfBroadcastAddr.setStatus(_E)
_DsSubnetConfDefaultLeaseTime_Type=Integer32
_DsSubnetConfDefaultLeaseTime_Object=MibTableColumn
dsSubnetConfDefaultLeaseTime=_DsSubnetConfDefaultLeaseTime_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,5),_DsSubnetConfDefaultLeaseTime_Type())
dsSubnetConfDefaultLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfDefaultLeaseTime.setStatus(_A)
_DsSubnetConfMaxLeaseTime_Type=Integer32
_DsSubnetConfMaxLeaseTime_Object=MibTableColumn
dsSubnetConfMaxLeaseTime=_DsSubnetConfMaxLeaseTime_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,6),_DsSubnetConfMaxLeaseTime_Type())
dsSubnetConfMaxLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfMaxLeaseTime.setStatus(_A)
_DsSubnetConfTotalCount_Type=Integer32
_DsSubnetConfTotalCount_Object=MibTableColumn
dsSubnetConfTotalCount=_DsSubnetConfTotalCount_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,7),_DsSubnetConfTotalCount_Type())
dsSubnetConfTotalCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfTotalCount.setStatus(_A)
_DsSubnetConfAllocatedCount_Type=Integer32
_DsSubnetConfAllocatedCount_Object=MibTableColumn
dsSubnetConfAllocatedCount=_DsSubnetConfAllocatedCount_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,8),_DsSubnetConfAllocatedCount_Type())
dsSubnetConfAllocatedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfAllocatedCount.setStatus(_A)
_DsSubnetConfRouters_Type=IpAddress
_DsSubnetConfRouters_Object=MibTableColumn
dsSubnetConfRouters=_DsSubnetConfRouters_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,9),_DsSubnetConfRouters_Type())
dsSubnetConfRouters.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfRouters.setStatus(_A)
class _DsSubnetConfRangeBitmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DsSubnetConfRangeBitmap_Type.__name__=_D
_DsSubnetConfRangeBitmap_Object=MibTableColumn
dsSubnetConfRangeBitmap=_DsSubnetConfRangeBitmap_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,10),_DsSubnetConfRangeBitmap_Type())
dsSubnetConfRangeBitmap.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfRangeBitmap.setStatus(_E)
_DsSubnetConfIndex_Type=SubnetConfIndex
_DsSubnetConfIndex_Object=MibTableColumn
dsSubnetConfIndex=_DsSubnetConfIndex_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,11),_DsSubnetConfIndex_Type())
dsSubnetConfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:dsSubnetConfIndex.setStatus(_A)
class _DsSubnetConfDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DsSubnetConfDomainName_Type.__name__=_D
_DsSubnetConfDomainName_Object=MibTableColumn
dsSubnetConfDomainName=_DsSubnetConfDomainName_Object((1,3,6,1,4,1,6296,9,1,1,5,1,7,1,12),_DsSubnetConfDomainName_Type())
dsSubnetConfDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfDomainName.setStatus(_A)
_DsSubnetConfRangeTable_Object=MibTable
dsSubnetConfRangeTable=_DsSubnetConfRangeTable_Object((1,3,6,1,4,1,6296,9,1,1,5,1,8))
if mibBuilder.loadTexts:dsSubnetConfRangeTable.setStatus(_A)
_DsSubnetConfRangeEntry_Object=MibTableRow
dsSubnetConfRangeEntry=_DsSubnetConfRangeEntry_Object((1,3,6,1,4,1,6296,9,1,1,5,1,8,1))
dsSubnetConfRangeEntry.setIndexNames((0,_C,_F),(0,_C,_J))
if mibBuilder.loadTexts:dsSubnetConfRangeEntry.setStatus(_A)
_DsSubnetConfRangeStart_Type=IpAddress
_DsSubnetConfRangeStart_Object=MibTableColumn
dsSubnetConfRangeStart=_DsSubnetConfRangeStart_Object((1,3,6,1,4,1,6296,9,1,1,5,1,8,1,1),_DsSubnetConfRangeStart_Type())
dsSubnetConfRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfRangeStart.setStatus(_A)
_DsSubnetConfRangeEnd_Type=IpAddress
_DsSubnetConfRangeEnd_Object=MibTableColumn
dsSubnetConfRangeEnd=_DsSubnetConfRangeEnd_Object((1,3,6,1,4,1,6296,9,1,1,5,1,8,1,2),_DsSubnetConfRangeEnd_Type())
dsSubnetConfRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsSubnetConfRangeEnd.setStatus(_A)
_DsSubnetConfRangeIndex_Type=SubnetConfRangeIndex
_DsSubnetConfRangeIndex_Object=MibTableColumn
dsSubnetConfRangeIndex=_DsSubnetConfRangeIndex_Object((1,3,6,1,4,1,6296,9,1,1,5,1,8,1,3),_DsSubnetConfRangeIndex_Type())
dsSubnetConfRangeIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:dsSubnetConfRangeIndex.setStatus(_A)
_Security_ObjectIdentity=ObjectIdentity
security=_Security_ObjectIdentity((1,3,6,1,5))
_SnmpV2_ObjectIdentity=ObjectIdentity
snmpV2=_SnmpV2_ObjectIdentity((1,3,6,1,6))
mibBuilder.exportSymbols(_C,**{'SubnetConfIndex':SubnetConfIndex,'SubnetConfRangeIndex':SubnetConfRangeIndex,'org':org,'dod':dod,'internet':internet,'directory':directory,'mgmt':mgmt,'transmission':transmission,'experimental':experimental,'private':private,'dasan':dasan,'dasanSwitchMIB':dasanSwitchMIB,'dasanSwitchMIBObjects':dasanSwitchMIBObjects,'dsDhcpMIBObjects':dsDhcpMIBObjects,'dsDhcpDaemonConf':dsDhcpDaemonConf,'dsDefaultLeaseTime':dsDefaultLeaseTime,'dsMaxLeaseTime':dsMaxLeaseTime,'dsSubnetMask':dsSubnetMask,'dsBroadcastAddress':dsBroadcastAddress,'dsDomainName':dsDomainName,'dsDomainNameServerTable':dsDomainNameServerTable,'dsDomainNameServerEntry':dsDomainNameServerEntry,_H:dsDomainNameServerIpIdx,'dsDomainNameServerIp':dsDomainNameServerIp,'dsSubnetConfTable':dsSubnetConfTable,'dsSubnetConfEntry':dsSubnetConfEntry,'dsSubnetConfName':dsSubnetConfName,'dsSubnetConfSubnet':dsSubnetConfSubnet,'dsSubnetConfNetmask':dsSubnetConfNetmask,'dsSubnetConfBroadcastAddr':dsSubnetConfBroadcastAddr,'dsSubnetConfDefaultLeaseTime':dsSubnetConfDefaultLeaseTime,'dsSubnetConfMaxLeaseTime':dsSubnetConfMaxLeaseTime,'dsSubnetConfTotalCount':dsSubnetConfTotalCount,'dsSubnetConfAllocatedCount':dsSubnetConfAllocatedCount,'dsSubnetConfRouters':dsSubnetConfRouters,'dsSubnetConfRangeBitmap':dsSubnetConfRangeBitmap,_F:dsSubnetConfIndex,'dsSubnetConfDomainName':dsSubnetConfDomainName,'dsSubnetConfRangeTable':dsSubnetConfRangeTable,'dsSubnetConfRangeEntry':dsSubnetConfRangeEntry,'dsSubnetConfRangeStart':dsSubnetConfRangeStart,'dsSubnetConfRangeEnd':dsSubnetConfRangeEnd,_J:dsSubnetConfRangeIndex,'security':security,'snmpV2':snmpV2})