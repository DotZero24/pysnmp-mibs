_i='ciiHelperAddressGroup'
_h='deprecated'
_g='ciiHelperAddressStorage'
_f='ciiHelperAddressStatus'
_e='ciiIPIfAddressBroadcast'
_d='ciiIPIfAddressStatus'
_c='ciiIPIfAddressCategory'
_b='ciiIPIfAddressPrefixLength'
_a='ciiIPAddressBroadcast'
_Z='ciiIPAddressStatus'
_Y='ciiIPAddressCategory'
_X='ciiIPAddressPrefixLength'
_W='ciiHelperAddress'
_V='ciiHelperAddressType'
_U='ciiHelperAddressVrf'
_T='secondary'
_S='primary'
_R='single'
_Q='StorageType'
_P='SnmpAdminString'
_O='InetAddress'
_N='ifIndex'
_M='IF-MIB'
_L='ciscoIPIfAddressConfigurationGroup4'
_K='ciscoIPIfAddressConfigurationGroup3'
_J='ciiIPAddressCategoryCap'
_I='ciiIPAddressIfIndex'
_H='ciiIPAddress'
_G='ciiIPAddressType'
_F='ciscoIPIfAddressConfigurationGroup2'
_E='ciscoIPIfAddressConfigurationGroup1'
_D='not-accessible'
_C='read-create'
_B='current'
_A='CISCO-IP-IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_M,'InterfaceIndex',_N)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_O,'InetAddressPrefixLength','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_Q,'TextualConvention')
ciscoIPIfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,309))
if mibBuilder.loadTexts:ciscoIPIfMIB.setRevisions(('2008-08-08 00:00','2008-07-28 00:00','2002-10-12 00:00','2002-10-10 00:00'))
class IpAddressCatagory(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3)))
_CiscoIPIfMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIPIfMIBNotifs=_CiscoIPIfMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,309,0))
_CiiIPIfNotifications_ObjectIdentity=ObjectIdentity
ciiIPIfNotifications=_CiiIPIfNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,309,0,0))
_CiscoIPIfMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIPIfMIBObjects=_CiscoIPIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,309,1))
_CiiIPAddressConfiguration_ObjectIdentity=ObjectIdentity
ciiIPAddressConfiguration=_CiiIPAddressConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,309,1,1))
class _CiiIPAddressCategoryCap_Type(Bits):namedValues=NamedValues(*((_R,0),(_S,1),(_T,2)))
_CiiIPAddressCategoryCap_Type.__name__='Bits'
_CiiIPAddressCategoryCap_Object=MibScalar
ciiIPAddressCategoryCap=_CiiIPAddressCategoryCap_Object((1,3,6,1,4,1,9,9,309,1,1,1),_CiiIPAddressCategoryCap_Type())
ciiIPAddressCategoryCap.setMaxAccess('read-only')
if mibBuilder.loadTexts:ciiIPAddressCategoryCap.setStatus(_B)
_CiiIPAddressTable_Object=MibTable
ciiIPAddressTable=_CiiIPAddressTable_Object((1,3,6,1,4,1,9,9,309,1,1,2))
if mibBuilder.loadTexts:ciiIPAddressTable.setStatus(_B)
_CiiIPAddressEntry_Object=MibTableRow
ciiIPAddressEntry=_CiiIPAddressEntry_Object((1,3,6,1,4,1,9,9,309,1,1,2,1))
ciiIPAddressEntry.setIndexNames((0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:ciiIPAddressEntry.setStatus(_B)
_CiiIPAddressType_Type=InetAddressType
_CiiIPAddressType_Object=MibTableColumn
ciiIPAddressType=_CiiIPAddressType_Object((1,3,6,1,4,1,9,9,309,1,1,2,1,1),_CiiIPAddressType_Type())
ciiIPAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciiIPAddressType.setStatus(_B)
class _CiiIPAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,36))
_CiiIPAddress_Type.__name__=_O
_CiiIPAddress_Object=MibTableColumn
ciiIPAddress=_CiiIPAddress_Object((1,3,6,1,4,1,9,9,309,1,1,2,1,2),_CiiIPAddress_Type())
ciiIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ciiIPAddress.setStatus(_B)
_CiiIPAddressIfIndex_Type=InterfaceIndex
_CiiIPAddressIfIndex_Object=MibTableColumn
ciiIPAddressIfIndex=_CiiIPAddressIfIndex_Object((1,3,6,1,4,1,9,9,309,1,1,2,1,3),_CiiIPAddressIfIndex_Type())
ciiIPAddressIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiIPAddressIfIndex.setStatus(_B)
_CiiIPAddressPrefixLength_Type=InetAddressPrefixLength
_CiiIPAddressPrefixLength_Object=MibTableColumn
ciiIPAddressPrefixLength=_CiiIPAddressPrefixLength_Object((1,3,6,1,4,1,9,9,309,1,1,2,1,4),_CiiIPAddressPrefixLength_Type())
ciiIPAddressPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiIPAddressPrefixLength.setStatus(_B)
_CiiIPAddressBroadcast_Type=InetAddress
_CiiIPAddressBroadcast_Object=MibTableColumn
ciiIPAddressBroadcast=_CiiIPAddressBroadcast_Object((1,3,6,1,4,1,9,9,309,1,1,2,1,5),_CiiIPAddressBroadcast_Type())
ciiIPAddressBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiIPAddressBroadcast.setStatus(_B)
_CiiIPAddressCategory_Type=IpAddressCatagory
_CiiIPAddressCategory_Object=MibTableColumn
ciiIPAddressCategory=_CiiIPAddressCategory_Object((1,3,6,1,4,1,9,9,309,1,1,2,1,6),_CiiIPAddressCategory_Type())
ciiIPAddressCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiIPAddressCategory.setStatus(_B)
_CiiIPAddressStatus_Type=RowStatus
_CiiIPAddressStatus_Object=MibTableColumn
ciiIPAddressStatus=_CiiIPAddressStatus_Object((1,3,6,1,4,1,9,9,309,1,1,2,1,7),_CiiIPAddressStatus_Type())
ciiIPAddressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiIPAddressStatus.setStatus(_B)
_CiiIPIfAddressTable_Object=MibTable
ciiIPIfAddressTable=_CiiIPIfAddressTable_Object((1,3,6,1,4,1,9,9,309,1,1,3))
if mibBuilder.loadTexts:ciiIPIfAddressTable.setStatus(_B)
_CiiIPIfAddressEntry_Object=MibTableRow
ciiIPIfAddressEntry=_CiiIPIfAddressEntry_Object((1,3,6,1,4,1,9,9,309,1,1,3,1))
ciiIPIfAddressEntry.setIndexNames((0,_A,_I),(0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:ciiIPIfAddressEntry.setStatus(_B)
_CiiIPIfAddressPrefixLength_Type=InetAddressPrefixLength
_CiiIPIfAddressPrefixLength_Object=MibTableColumn
ciiIPIfAddressPrefixLength=_CiiIPIfAddressPrefixLength_Object((1,3,6,1,4,1,9,9,309,1,1,3,1,1),_CiiIPIfAddressPrefixLength_Type())
ciiIPIfAddressPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiIPIfAddressPrefixLength.setStatus(_B)
_CiiIPIfAddressBroadcast_Type=InetAddress
_CiiIPIfAddressBroadcast_Object=MibTableColumn
ciiIPIfAddressBroadcast=_CiiIPIfAddressBroadcast_Object((1,3,6,1,4,1,9,9,309,1,1,3,1,2),_CiiIPIfAddressBroadcast_Type())
ciiIPIfAddressBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiIPIfAddressBroadcast.setStatus(_B)
_CiiIPIfAddressCategory_Type=IpAddressCatagory
_CiiIPIfAddressCategory_Object=MibTableColumn
ciiIPIfAddressCategory=_CiiIPIfAddressCategory_Object((1,3,6,1,4,1,9,9,309,1,1,3,1,3),_CiiIPIfAddressCategory_Type())
ciiIPIfAddressCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiIPIfAddressCategory.setStatus(_B)
_CiiIPIfAddressStatus_Type=RowStatus
_CiiIPIfAddressStatus_Object=MibTableColumn
ciiIPIfAddressStatus=_CiiIPIfAddressStatus_Object((1,3,6,1,4,1,9,9,309,1,1,3,1,4),_CiiIPIfAddressStatus_Type())
ciiIPIfAddressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiIPIfAddressStatus.setStatus(_B)
_CiiHelperAddressConfiguration_ObjectIdentity=ObjectIdentity
ciiHelperAddressConfiguration=_CiiHelperAddressConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,309,1,2))
_CiiHelperAddressTable_Object=MibTable
ciiHelperAddressTable=_CiiHelperAddressTable_Object((1,3,6,1,4,1,9,9,309,1,2,1))
if mibBuilder.loadTexts:ciiHelperAddressTable.setStatus(_B)
_CiiHelperAddressEntry_Object=MibTableRow
ciiHelperAddressEntry=_CiiHelperAddressEntry_Object((1,3,6,1,4,1,9,9,309,1,2,1,1))
ciiHelperAddressEntry.setIndexNames((0,_M,_N),(0,_A,_U),(0,_A,_V),(0,_A,_W))
if mibBuilder.loadTexts:ciiHelperAddressEntry.setStatus(_B)
class _CiiHelperAddressVrf_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiiHelperAddressVrf_Type.__name__=_P
_CiiHelperAddressVrf_Object=MibTableColumn
ciiHelperAddressVrf=_CiiHelperAddressVrf_Object((1,3,6,1,4,1,9,9,309,1,2,1,1,1),_CiiHelperAddressVrf_Type())
ciiHelperAddressVrf.setMaxAccess(_D)
if mibBuilder.loadTexts:ciiHelperAddressVrf.setStatus(_B)
_CiiHelperAddressType_Type=InetAddressType
_CiiHelperAddressType_Object=MibTableColumn
ciiHelperAddressType=_CiiHelperAddressType_Object((1,3,6,1,4,1,9,9,309,1,2,1,1,2),_CiiHelperAddressType_Type())
ciiHelperAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciiHelperAddressType.setStatus(_B)
_CiiHelperAddress_Type=InetAddress
_CiiHelperAddress_Object=MibTableColumn
ciiHelperAddress=_CiiHelperAddress_Object((1,3,6,1,4,1,9,9,309,1,2,1,1,3),_CiiHelperAddress_Type())
ciiHelperAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ciiHelperAddress.setStatus(_B)
_CiiHelperAddressStatus_Type=RowStatus
_CiiHelperAddressStatus_Object=MibTableColumn
ciiHelperAddressStatus=_CiiHelperAddressStatus_Object((1,3,6,1,4,1,9,9,309,1,2,1,1,4),_CiiHelperAddressStatus_Type())
ciiHelperAddressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiHelperAddressStatus.setStatus(_B)
class _CiiHelperAddressStorage_Type(StorageType):defaultValue=2
_CiiHelperAddressStorage_Type.__name__=_Q
_CiiHelperAddressStorage_Object=MibTableColumn
ciiHelperAddressStorage=_CiiHelperAddressStorage_Object((1,3,6,1,4,1,9,9,309,1,2,1,1,5),_CiiHelperAddressStorage_Type())
ciiHelperAddressStorage.setMaxAccess(_C)
if mibBuilder.loadTexts:ciiHelperAddressStorage.setStatus(_B)
_CiscoIPIfMIBConform_ObjectIdentity=ObjectIdentity
ciscoIPIfMIBConform=_CiscoIPIfMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,309,2))
_CiscoIPIfMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIPIfMIBCompliances=_CiscoIPIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,309,2,1))
_CiscoIPIfMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIPIfMIBGroups=_CiscoIPIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,309,2,2))
ciscoIPIfAddressConfigurationGroup1=ObjectGroup((1,3,6,1,4,1,9,9,309,2,2,1))
ciscoIPIfAddressConfigurationGroup1.setObjects(*((_A,_J),(_A,_I),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoIPIfAddressConfigurationGroup1.setStatus(_B)
ciscoIPIfAddressConfigurationGroup2=ObjectGroup((1,3,6,1,4,1,9,9,309,2,2,2))
ciscoIPIfAddressConfigurationGroup2.setObjects((_A,_a))
if mibBuilder.loadTexts:ciscoIPIfAddressConfigurationGroup2.setStatus(_B)
ciscoIPIfAddressConfigurationGroup3=ObjectGroup((1,3,6,1,4,1,9,9,309,2,2,3))
ciscoIPIfAddressConfigurationGroup3.setObjects(*((_A,_J),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:ciscoIPIfAddressConfigurationGroup3.setStatus(_B)
ciscoIPIfAddressConfigurationGroup4=ObjectGroup((1,3,6,1,4,1,9,9,309,2,2,4))
ciscoIPIfAddressConfigurationGroup4.setObjects((_A,_e))
if mibBuilder.loadTexts:ciscoIPIfAddressConfigurationGroup4.setStatus(_B)
ciiHelperAddressGroup=ObjectGroup((1,3,6,1,4,1,9,9,309,2,2,5))
ciiHelperAddressGroup.setObjects(*((_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciiHelperAddressGroup.setStatus(_B)
ciscoIPIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,309,2,1,1))
ciscoIPIfMIBCompliance.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ciscoIPIfMIBCompliance.setStatus(_h)
ciscoIPIfMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,309,2,1,2))
ciscoIPIfMIBCompliance1.setObjects(*((_A,_E),(_A,_F),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoIPIfMIBCompliance1.setStatus(_h)
ciscoIPIfMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,309,2,1,3))
ciscoIPIfMIBCompliance2.setObjects(*((_A,_E),(_A,_F),(_A,_K),(_A,_L),(_A,_i)))
if mibBuilder.loadTexts:ciscoIPIfMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'IpAddressCatagory':IpAddressCatagory,'ciscoIPIfMIB':ciscoIPIfMIB,'ciscoIPIfMIBNotifs':ciscoIPIfMIBNotifs,'ciiIPIfNotifications':ciiIPIfNotifications,'ciscoIPIfMIBObjects':ciscoIPIfMIBObjects,'ciiIPAddressConfiguration':ciiIPAddressConfiguration,_J:ciiIPAddressCategoryCap,'ciiIPAddressTable':ciiIPAddressTable,'ciiIPAddressEntry':ciiIPAddressEntry,_G:ciiIPAddressType,_H:ciiIPAddress,_I:ciiIPAddressIfIndex,_X:ciiIPAddressPrefixLength,_a:ciiIPAddressBroadcast,_Y:ciiIPAddressCategory,_Z:ciiIPAddressStatus,'ciiIPIfAddressTable':ciiIPIfAddressTable,'ciiIPIfAddressEntry':ciiIPIfAddressEntry,_b:ciiIPIfAddressPrefixLength,_e:ciiIPIfAddressBroadcast,_c:ciiIPIfAddressCategory,_d:ciiIPIfAddressStatus,'ciiHelperAddressConfiguration':ciiHelperAddressConfiguration,'ciiHelperAddressTable':ciiHelperAddressTable,'ciiHelperAddressEntry':ciiHelperAddressEntry,_U:ciiHelperAddressVrf,_V:ciiHelperAddressType,_W:ciiHelperAddress,_f:ciiHelperAddressStatus,_g:ciiHelperAddressStorage,'ciscoIPIfMIBConform':ciscoIPIfMIBConform,'ciscoIPIfMIBCompliances':ciscoIPIfMIBCompliances,'ciscoIPIfMIBCompliance':ciscoIPIfMIBCompliance,'ciscoIPIfMIBCompliance1':ciscoIPIfMIBCompliance1,'ciscoIPIfMIBCompliance2':ciscoIPIfMIBCompliance2,'ciscoIPIfMIBGroups':ciscoIPIfMIBGroups,_E:ciscoIPIfAddressConfigurationGroup1,_F:ciscoIPIfAddressConfigurationGroup2,_K:ciscoIPIfAddressConfigurationGroup3,_L:ciscoIPIfAddressConfigurationGroup4,_i:ciiHelperAddressGroup})