_AS='ciscoIpv6ScopeGroup'
_AR='ciscoIpv6InterfaceGroup'
_AQ='ciscoIpv6GeneralGroup'
_AP='ciscoInetIcmpMsgGroup'
_AO='ciscoInetIcmpGroup'
_AN='ciscoInetNetToMediaGroup'
_AM='ciscoIpAddressGroup'
_AL='ciscoIpAddressPfxGroup'
_AK='cIpv6ScopeIdD'
_AJ='cIpv6ScopeIdC'
_AI='cIpv6ScopeIdB'
_AH='cIpv6ScopeIdA'
_AG='cIpv6ScopeId9'
_AF='cIpv6ScopeIdOrganizationLocal'
_AE='cIpv6ScopeId7'
_AD='cIpv6ScopeId6'
_AC='cIpv6ScopeIdSiteLocal'
_AB='cIpv6ScopeIdAdminLocal'
_AA='cIpv6ScopeIdSubnetLocal'
_A9='cIpv6ScopeIdLinkLocal'
_A8='cIpv6InterfacePhysicalAddress'
_A7='cIpv6InterfaceIdentifierLength'
_A6='cIpv6InterfaceIdentifier'
_A5='cIpv6InterfaceReasmMaxSize'
_A4='cIpv6InterfaceEffectiveMtu'
_A3='cIpv6DefaultHopLimit'
_A2='cIpv6Forwarding'
_A1='cInetIcmpMsgOutPkts'
_A0='cInetIcmpMsgInPkts'
_z='cInetIcmpOutErrors'
_y='cInetIcmpOutMsgs'
_x='cInetIcmpInErrors'
_w='cInetIcmpInMsgs'
_v='cInetNetToMediaState'
_u='cInetNetToMediaType'
_t='cInetNetToMediaLastUpdated'
_s='cInetNetToMediaPhysAddress'
_r='cIpAddressStatus'
_q='cIpAddressOrigin'
_p='cIpAddressPrefix'
_o='cIpAddressType'
_n='cIpAddressIfIndex'
_m='cIpAddressPfxAdvValidLifetime'
_l='cIpAddressPfxAdvPfdLifetime'
_k='cIpAddressPfxAutonomousFlag'
_j='cIpAddressPfxOnLinkFlag'
_i='cIpAddressPfxOrigin'
_h='cInetIcmpMsgCode'
_g='cInetIcmpMsgType'
_f='cInetIcmpMsgIfIndex'
_e='cInetIcmpMsgAFType'
_d='cInetIcmpIfIndex'
_c='cInetIcmpAFType'
_b='octets'
_a='cIpv6InterfaceIfIndex'
_Z='cIpv6ScopeIdIfIndex'
_Y='read-create'
_X='cInetNetToMediaNetAddress'
_W='cInetNetToMediaNetAddressType'
_V='unknown'
_U='cIpAddressAddr'
_T='cIpAddressAddrType'
_S='seconds'
_R='wellknown'
_Q='manual'
_P='cIpAddressPfxLength'
_O='cIpAddressPfxPfx'
_N='cIpAddressPfxType'
_M='cIpAddressPfxIfIndex'
_L='Unsigned32'
_K='ifIndex'
_J='IF-MIB'
_I='invalid'
_H='other'
_G='read-write'
_F='InetAddress'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='CISCO-IETF-IP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_J,'InterfaceIndex','InterfaceIndexOrZero',_K)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp','TruthValue')
ciscoIetfIpMIB=ModuleIdentity((1,3,6,1,4,1,9,10,86))
if mibBuilder.loadTexts:ciscoIetfIpMIB.setRevisions(('2002-03-04 00:00',))
class Ipv6AddrIfIdentifier(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
class ScopeId(TextualConvention,Unsigned32):status=_A
_CiscoIetfIpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIetfIpMIBObjects=_CiscoIetfIpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,86,1))
_CIp_ObjectIdentity=ObjectIdentity
cIp=_CIp_ObjectIdentity((1,3,6,1,4,1,9,10,86,1,1))
_CIpAddressPfxTable_Object=MibTable
cIpAddressPfxTable=_CIpAddressPfxTable_Object((1,3,6,1,4,1,9,10,86,1,1,1))
if mibBuilder.loadTexts:cIpAddressPfxTable.setStatus(_A)
_CIpAddressPfxEntry_Object=MibTableRow
cIpAddressPfxEntry=_CIpAddressPfxEntry_Object((1,3,6,1,4,1,9,10,86,1,1,1,1))
cIpAddressPfxEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:cIpAddressPfxEntry.setStatus(_A)
_CIpAddressPfxIfIndex_Type=InterfaceIndex
_CIpAddressPfxIfIndex_Object=MibTableColumn
cIpAddressPfxIfIndex=_CIpAddressPfxIfIndex_Object((1,3,6,1,4,1,9,10,86,1,1,1,1,1),_CIpAddressPfxIfIndex_Type())
cIpAddressPfxIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpAddressPfxIfIndex.setStatus(_A)
_CIpAddressPfxType_Type=InetAddressType
_CIpAddressPfxType_Object=MibTableColumn
cIpAddressPfxType=_CIpAddressPfxType_Object((1,3,6,1,4,1,9,10,86,1,1,1,1,2),_CIpAddressPfxType_Type())
cIpAddressPfxType.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpAddressPfxType.setStatus(_A)
class _CIpAddressPfxPfx_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_CIpAddressPfxPfx_Type.__name__=_F
_CIpAddressPfxPfx_Object=MibTableColumn
cIpAddressPfxPfx=_CIpAddressPfxPfx_Object((1,3,6,1,4,1,9,10,86,1,1,1,1,3),_CIpAddressPfxPfx_Type())
cIpAddressPfxPfx.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpAddressPfxPfx.setStatus(_A)
_CIpAddressPfxLength_Type=InetAddressPrefixLength
_CIpAddressPfxLength_Object=MibTableColumn
cIpAddressPfxLength=_CIpAddressPfxLength_Object((1,3,6,1,4,1,9,10,86,1,1,1,1,4),_CIpAddressPfxLength_Type())
cIpAddressPfxLength.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpAddressPfxLength.setStatus(_A)
class _CIpAddressPfxOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_Q,2),(_R,3),('dhcp',4),('routeradv',5)))
_CIpAddressPfxOrigin_Type.__name__=_E
_CIpAddressPfxOrigin_Object=MibTableColumn
cIpAddressPfxOrigin=_CIpAddressPfxOrigin_Object((1,3,6,1,4,1,9,10,86,1,1,1,1,5),_CIpAddressPfxOrigin_Type())
cIpAddressPfxOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpAddressPfxOrigin.setStatus(_A)
_CIpAddressPfxOnLinkFlag_Type=TruthValue
_CIpAddressPfxOnLinkFlag_Object=MibTableColumn
cIpAddressPfxOnLinkFlag=_CIpAddressPfxOnLinkFlag_Object((1,3,6,1,4,1,9,10,86,1,1,1,1,6),_CIpAddressPfxOnLinkFlag_Type())
cIpAddressPfxOnLinkFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpAddressPfxOnLinkFlag.setStatus(_A)
_CIpAddressPfxAutonomousFlag_Type=TruthValue
_CIpAddressPfxAutonomousFlag_Object=MibTableColumn
cIpAddressPfxAutonomousFlag=_CIpAddressPfxAutonomousFlag_Object((1,3,6,1,4,1,9,10,86,1,1,1,1,7),_CIpAddressPfxAutonomousFlag_Type())
cIpAddressPfxAutonomousFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpAddressPfxAutonomousFlag.setStatus(_A)
_CIpAddressPfxAdvPfdLifetime_Type=Unsigned32
_CIpAddressPfxAdvPfdLifetime_Object=MibTableColumn
cIpAddressPfxAdvPfdLifetime=_CIpAddressPfxAdvPfdLifetime_Object((1,3,6,1,4,1,9,10,86,1,1,1,1,8),_CIpAddressPfxAdvPfdLifetime_Type())
cIpAddressPfxAdvPfdLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpAddressPfxAdvPfdLifetime.setStatus(_A)
if mibBuilder.loadTexts:cIpAddressPfxAdvPfdLifetime.setUnits(_S)
_CIpAddressPfxAdvValidLifetime_Type=Unsigned32
_CIpAddressPfxAdvValidLifetime_Object=MibTableColumn
cIpAddressPfxAdvValidLifetime=_CIpAddressPfxAdvValidLifetime_Object((1,3,6,1,4,1,9,10,86,1,1,1,1,9),_CIpAddressPfxAdvValidLifetime_Type())
cIpAddressPfxAdvValidLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpAddressPfxAdvValidLifetime.setStatus(_A)
if mibBuilder.loadTexts:cIpAddressPfxAdvValidLifetime.setUnits(_S)
_CIpAddressTable_Object=MibTable
cIpAddressTable=_CIpAddressTable_Object((1,3,6,1,4,1,9,10,86,1,1,2))
if mibBuilder.loadTexts:cIpAddressTable.setStatus(_A)
_CIpAddressEntry_Object=MibTableRow
cIpAddressEntry=_CIpAddressEntry_Object((1,3,6,1,4,1,9,10,86,1,1,2,1))
cIpAddressEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:cIpAddressEntry.setStatus(_A)
_CIpAddressAddrType_Type=InetAddressType
_CIpAddressAddrType_Object=MibTableColumn
cIpAddressAddrType=_CIpAddressAddrType_Object((1,3,6,1,4,1,9,10,86,1,1,2,1,1),_CIpAddressAddrType_Type())
cIpAddressAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpAddressAddrType.setStatus(_A)
class _CIpAddressAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_CIpAddressAddr_Type.__name__=_F
_CIpAddressAddr_Object=MibTableColumn
cIpAddressAddr=_CIpAddressAddr_Object((1,3,6,1,4,1,9,10,86,1,1,2,1,2),_CIpAddressAddr_Type())
cIpAddressAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpAddressAddr.setStatus(_A)
_CIpAddressIfIndex_Type=InterfaceIndex
_CIpAddressIfIndex_Object=MibTableColumn
cIpAddressIfIndex=_CIpAddressIfIndex_Object((1,3,6,1,4,1,9,10,86,1,1,2,1,3),_CIpAddressIfIndex_Type())
cIpAddressIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpAddressIfIndex.setStatus(_A)
class _CIpAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('anycast',2),('broadcast',3)))
_CIpAddressType_Type.__name__=_E
_CIpAddressType_Object=MibTableColumn
cIpAddressType=_CIpAddressType_Object((1,3,6,1,4,1,9,10,86,1,1,2,1,4),_CIpAddressType_Type())
cIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpAddressType.setStatus(_A)
_CIpAddressPrefix_Type=RowPointer
_CIpAddressPrefix_Object=MibTableColumn
cIpAddressPrefix=_CIpAddressPrefix_Object((1,3,6,1,4,1,9,10,86,1,1,2,1,5),_CIpAddressPrefix_Type())
cIpAddressPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpAddressPrefix.setStatus(_A)
class _CIpAddressOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_Q,2),(_R,3),('dhcp',4),('linklayer',5),('random',6)))
_CIpAddressOrigin_Type.__name__=_E
_CIpAddressOrigin_Object=MibTableColumn
cIpAddressOrigin=_CIpAddressOrigin_Object((1,3,6,1,4,1,9,10,86,1,1,2,1,6),_CIpAddressOrigin_Type())
cIpAddressOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpAddressOrigin.setStatus(_A)
class _CIpAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('preferred',1),('deprecated',2),(_I,3),('inaccessible',4),(_V,5),('tentative',6),('duplicate',7)))
_CIpAddressStatus_Type.__name__=_E
_CIpAddressStatus_Object=MibTableColumn
cIpAddressStatus=_CIpAddressStatus_Object((1,3,6,1,4,1,9,10,86,1,1,2,1,7),_CIpAddressStatus_Type())
cIpAddressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpAddressStatus.setStatus(_A)
_CInetNetToMediaTable_Object=MibTable
cInetNetToMediaTable=_CInetNetToMediaTable_Object((1,3,6,1,4,1,9,10,86,1,1,3))
if mibBuilder.loadTexts:cInetNetToMediaTable.setStatus(_A)
_CInetNetToMediaEntry_Object=MibTableRow
cInetNetToMediaEntry=_CInetNetToMediaEntry_Object((1,3,6,1,4,1,9,10,86,1,1,3,1))
cInetNetToMediaEntry.setIndexNames((0,_J,_K),(0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:cInetNetToMediaEntry.setStatus(_A)
_CInetNetToMediaNetAddressType_Type=InetAddressType
_CInetNetToMediaNetAddressType_Object=MibTableColumn
cInetNetToMediaNetAddressType=_CInetNetToMediaNetAddressType_Object((1,3,6,1,4,1,9,10,86,1,1,3,1,1),_CInetNetToMediaNetAddressType_Type())
cInetNetToMediaNetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cInetNetToMediaNetAddressType.setStatus(_A)
class _CInetNetToMediaNetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_CInetNetToMediaNetAddress_Type.__name__=_F
_CInetNetToMediaNetAddress_Object=MibTableColumn
cInetNetToMediaNetAddress=_CInetNetToMediaNetAddress_Object((1,3,6,1,4,1,9,10,86,1,1,3,1,2),_CInetNetToMediaNetAddress_Type())
cInetNetToMediaNetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cInetNetToMediaNetAddress.setStatus(_A)
_CInetNetToMediaPhysAddress_Type=PhysAddress
_CInetNetToMediaPhysAddress_Object=MibTableColumn
cInetNetToMediaPhysAddress=_CInetNetToMediaPhysAddress_Object((1,3,6,1,4,1,9,10,86,1,1,3,1,3),_CInetNetToMediaPhysAddress_Type())
cInetNetToMediaPhysAddress.setMaxAccess(_Y)
if mibBuilder.loadTexts:cInetNetToMediaPhysAddress.setStatus(_A)
_CInetNetToMediaLastUpdated_Type=TimeStamp
_CInetNetToMediaLastUpdated_Object=MibTableColumn
cInetNetToMediaLastUpdated=_CInetNetToMediaLastUpdated_Object((1,3,6,1,4,1,9,10,86,1,1,3,1,4),_CInetNetToMediaLastUpdated_Type())
cInetNetToMediaLastUpdated.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetNetToMediaLastUpdated.setStatus(_A)
class _CInetNetToMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_I,2),('dynamic',3),('static',4),('local',5)))
_CInetNetToMediaType_Type.__name__=_E
_CInetNetToMediaType_Object=MibTableColumn
cInetNetToMediaType=_CInetNetToMediaType_Object((1,3,6,1,4,1,9,10,86,1,1,3,1,5),_CInetNetToMediaType_Type())
cInetNetToMediaType.setMaxAccess(_Y)
if mibBuilder.loadTexts:cInetNetToMediaType.setStatus(_A)
class _CInetNetToMediaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reachable',1),('stale',2),('delay',3),('probe',4),(_I,5),(_V,6),('incomplete',7)))
_CInetNetToMediaState_Type.__name__=_E
_CInetNetToMediaState_Object=MibTableColumn
cInetNetToMediaState=_CInetNetToMediaState_Object((1,3,6,1,4,1,9,10,86,1,1,3,1,6),_CInetNetToMediaState_Type())
cInetNetToMediaState.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetNetToMediaState.setStatus(_A)
_CIpv6ScopeIdTable_Object=MibTable
cIpv6ScopeIdTable=_CIpv6ScopeIdTable_Object((1,3,6,1,4,1,9,10,86,1,1,4))
if mibBuilder.loadTexts:cIpv6ScopeIdTable.setStatus(_A)
_CIpv6ScopeIdEntry_Object=MibTableRow
cIpv6ScopeIdEntry=_CIpv6ScopeIdEntry_Object((1,3,6,1,4,1,9,10,86,1,1,4,1))
cIpv6ScopeIdEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:cIpv6ScopeIdEntry.setStatus(_A)
_CIpv6ScopeIdIfIndex_Type=InterfaceIndex
_CIpv6ScopeIdIfIndex_Object=MibTableColumn
cIpv6ScopeIdIfIndex=_CIpv6ScopeIdIfIndex_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,1),_CIpv6ScopeIdIfIndex_Type())
cIpv6ScopeIdIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpv6ScopeIdIfIndex.setStatus(_A)
_CIpv6ScopeIdLinkLocal_Type=ScopeId
_CIpv6ScopeIdLinkLocal_Object=MibTableColumn
cIpv6ScopeIdLinkLocal=_CIpv6ScopeIdLinkLocal_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,2),_CIpv6ScopeIdLinkLocal_Type())
cIpv6ScopeIdLinkLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeIdLinkLocal.setStatus(_A)
_CIpv6ScopeIdSubnetLocal_Type=ScopeId
_CIpv6ScopeIdSubnetLocal_Object=MibTableColumn
cIpv6ScopeIdSubnetLocal=_CIpv6ScopeIdSubnetLocal_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,3),_CIpv6ScopeIdSubnetLocal_Type())
cIpv6ScopeIdSubnetLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeIdSubnetLocal.setStatus(_A)
_CIpv6ScopeIdAdminLocal_Type=ScopeId
_CIpv6ScopeIdAdminLocal_Object=MibTableColumn
cIpv6ScopeIdAdminLocal=_CIpv6ScopeIdAdminLocal_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,4),_CIpv6ScopeIdAdminLocal_Type())
cIpv6ScopeIdAdminLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeIdAdminLocal.setStatus(_A)
_CIpv6ScopeIdSiteLocal_Type=ScopeId
_CIpv6ScopeIdSiteLocal_Object=MibTableColumn
cIpv6ScopeIdSiteLocal=_CIpv6ScopeIdSiteLocal_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,5),_CIpv6ScopeIdSiteLocal_Type())
cIpv6ScopeIdSiteLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeIdSiteLocal.setStatus(_A)
_CIpv6ScopeId6_Type=ScopeId
_CIpv6ScopeId6_Object=MibTableColumn
cIpv6ScopeId6=_CIpv6ScopeId6_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,6),_CIpv6ScopeId6_Type())
cIpv6ScopeId6.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeId6.setStatus(_A)
_CIpv6ScopeId7_Type=ScopeId
_CIpv6ScopeId7_Object=MibTableColumn
cIpv6ScopeId7=_CIpv6ScopeId7_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,7),_CIpv6ScopeId7_Type())
cIpv6ScopeId7.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeId7.setStatus(_A)
_CIpv6ScopeIdOrganizationLocal_Type=ScopeId
_CIpv6ScopeIdOrganizationLocal_Object=MibTableColumn
cIpv6ScopeIdOrganizationLocal=_CIpv6ScopeIdOrganizationLocal_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,8),_CIpv6ScopeIdOrganizationLocal_Type())
cIpv6ScopeIdOrganizationLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeIdOrganizationLocal.setStatus(_A)
_CIpv6ScopeId9_Type=ScopeId
_CIpv6ScopeId9_Object=MibTableColumn
cIpv6ScopeId9=_CIpv6ScopeId9_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,9),_CIpv6ScopeId9_Type())
cIpv6ScopeId9.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeId9.setStatus(_A)
_CIpv6ScopeIdA_Type=ScopeId
_CIpv6ScopeIdA_Object=MibTableColumn
cIpv6ScopeIdA=_CIpv6ScopeIdA_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,10),_CIpv6ScopeIdA_Type())
cIpv6ScopeIdA.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeIdA.setStatus(_A)
_CIpv6ScopeIdB_Type=ScopeId
_CIpv6ScopeIdB_Object=MibTableColumn
cIpv6ScopeIdB=_CIpv6ScopeIdB_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,11),_CIpv6ScopeIdB_Type())
cIpv6ScopeIdB.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeIdB.setStatus(_A)
_CIpv6ScopeIdC_Type=ScopeId
_CIpv6ScopeIdC_Object=MibTableColumn
cIpv6ScopeIdC=_CIpv6ScopeIdC_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,12),_CIpv6ScopeIdC_Type())
cIpv6ScopeIdC.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeIdC.setStatus(_A)
_CIpv6ScopeIdD_Type=ScopeId
_CIpv6ScopeIdD_Object=MibTableColumn
cIpv6ScopeIdD=_CIpv6ScopeIdD_Object((1,3,6,1,4,1,9,10,86,1,1,4,1,13),_CIpv6ScopeIdD_Type())
cIpv6ScopeIdD.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6ScopeIdD.setStatus(_A)
_CIpv6_ObjectIdentity=ObjectIdentity
cIpv6=_CIpv6_ObjectIdentity((1,3,6,1,4,1,9,10,86,1,2))
class _CIpv6Forwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('notForwarding',2)))
_CIpv6Forwarding_Type.__name__=_E
_CIpv6Forwarding_Object=MibScalar
cIpv6Forwarding=_CIpv6Forwarding_Object((1,3,6,1,4,1,9,10,86,1,2,1),_CIpv6Forwarding_Type())
cIpv6Forwarding.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpv6Forwarding.setStatus(_A)
class _CIpv6DefaultHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CIpv6DefaultHopLimit_Type.__name__=_E
_CIpv6DefaultHopLimit_Object=MibScalar
cIpv6DefaultHopLimit=_CIpv6DefaultHopLimit_Object((1,3,6,1,4,1,9,10,86,1,2,2),_CIpv6DefaultHopLimit_Type())
cIpv6DefaultHopLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpv6DefaultHopLimit.setStatus(_A)
_CIpv6InterfaceTable_Object=MibTable
cIpv6InterfaceTable=_CIpv6InterfaceTable_Object((1,3,6,1,4,1,9,10,86,1,2,3))
if mibBuilder.loadTexts:cIpv6InterfaceTable.setStatus(_A)
_CIpv6InterfaceEntry_Object=MibTableRow
cIpv6InterfaceEntry=_CIpv6InterfaceEntry_Object((1,3,6,1,4,1,9,10,86,1,2,3,1))
cIpv6InterfaceEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:cIpv6InterfaceEntry.setStatus(_A)
_CIpv6InterfaceIfIndex_Type=InterfaceIndex
_CIpv6InterfaceIfIndex_Object=MibTableColumn
cIpv6InterfaceIfIndex=_CIpv6InterfaceIfIndex_Object((1,3,6,1,4,1,9,10,86,1,2,3,1,1),_CIpv6InterfaceIfIndex_Type())
cIpv6InterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpv6InterfaceIfIndex.setStatus(_A)
_CIpv6InterfaceEffectiveMtu_Type=Unsigned32
_CIpv6InterfaceEffectiveMtu_Object=MibTableColumn
cIpv6InterfaceEffectiveMtu=_CIpv6InterfaceEffectiveMtu_Object((1,3,6,1,4,1,9,10,86,1,2,3,1,2),_CIpv6InterfaceEffectiveMtu_Type())
cIpv6InterfaceEffectiveMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6InterfaceEffectiveMtu.setStatus(_A)
if mibBuilder.loadTexts:cIpv6InterfaceEffectiveMtu.setUnits(_b)
class _CIpv6InterfaceReasmMaxSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CIpv6InterfaceReasmMaxSize_Type.__name__=_L
_CIpv6InterfaceReasmMaxSize_Object=MibTableColumn
cIpv6InterfaceReasmMaxSize=_CIpv6InterfaceReasmMaxSize_Object((1,3,6,1,4,1,9,10,86,1,2,3,1,3),_CIpv6InterfaceReasmMaxSize_Type())
cIpv6InterfaceReasmMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6InterfaceReasmMaxSize.setStatus(_A)
if mibBuilder.loadTexts:cIpv6InterfaceReasmMaxSize.setUnits(_b)
_CIpv6InterfaceIdentifier_Type=Ipv6AddrIfIdentifier
_CIpv6InterfaceIdentifier_Object=MibTableColumn
cIpv6InterfaceIdentifier=_CIpv6InterfaceIdentifier_Object((1,3,6,1,4,1,9,10,86,1,2,3,1,4),_CIpv6InterfaceIdentifier_Type())
cIpv6InterfaceIdentifier.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpv6InterfaceIdentifier.setStatus(_A)
class _CIpv6InterfaceIdentifierLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_CIpv6InterfaceIdentifierLength_Type.__name__=_E
_CIpv6InterfaceIdentifierLength_Object=MibTableColumn
cIpv6InterfaceIdentifierLength=_CIpv6InterfaceIdentifierLength_Object((1,3,6,1,4,1,9,10,86,1,2,3,1,5),_CIpv6InterfaceIdentifierLength_Type())
cIpv6InterfaceIdentifierLength.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpv6InterfaceIdentifierLength.setStatus(_A)
if mibBuilder.loadTexts:cIpv6InterfaceIdentifierLength.setUnits('bits')
_CIpv6InterfacePhysicalAddress_Type=PhysAddress
_CIpv6InterfacePhysicalAddress_Object=MibTableColumn
cIpv6InterfacePhysicalAddress=_CIpv6InterfacePhysicalAddress_Object((1,3,6,1,4,1,9,10,86,1,2,3,1,6),_CIpv6InterfacePhysicalAddress_Type())
cIpv6InterfacePhysicalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpv6InterfacePhysicalAddress.setStatus(_A)
_CIcmp_ObjectIdentity=ObjectIdentity
cIcmp=_CIcmp_ObjectIdentity((1,3,6,1,4,1,9,10,86,1,3))
_CInetIcmpTable_Object=MibTable
cInetIcmpTable=_CInetIcmpTable_Object((1,3,6,1,4,1,9,10,86,1,3,1))
if mibBuilder.loadTexts:cInetIcmpTable.setStatus(_A)
_CInetIcmpEntry_Object=MibTableRow
cInetIcmpEntry=_CInetIcmpEntry_Object((1,3,6,1,4,1,9,10,86,1,3,1,1))
cInetIcmpEntry.setIndexNames((0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:cInetIcmpEntry.setStatus(_A)
_CInetIcmpAFType_Type=InetAddressType
_CInetIcmpAFType_Object=MibTableColumn
cInetIcmpAFType=_CInetIcmpAFType_Object((1,3,6,1,4,1,9,10,86,1,3,1,1,1),_CInetIcmpAFType_Type())
cInetIcmpAFType.setMaxAccess(_D)
if mibBuilder.loadTexts:cInetIcmpAFType.setStatus(_A)
_CInetIcmpIfIndex_Type=InterfaceIndexOrZero
_CInetIcmpIfIndex_Object=MibTableColumn
cInetIcmpIfIndex=_CInetIcmpIfIndex_Object((1,3,6,1,4,1,9,10,86,1,3,1,1,2),_CInetIcmpIfIndex_Type())
cInetIcmpIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cInetIcmpIfIndex.setStatus(_A)
_CInetIcmpInMsgs_Type=Counter32
_CInetIcmpInMsgs_Object=MibTableColumn
cInetIcmpInMsgs=_CInetIcmpInMsgs_Object((1,3,6,1,4,1,9,10,86,1,3,1,1,3),_CInetIcmpInMsgs_Type())
cInetIcmpInMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetIcmpInMsgs.setStatus(_A)
_CInetIcmpInErrors_Type=Counter32
_CInetIcmpInErrors_Object=MibTableColumn
cInetIcmpInErrors=_CInetIcmpInErrors_Object((1,3,6,1,4,1,9,10,86,1,3,1,1,4),_CInetIcmpInErrors_Type())
cInetIcmpInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetIcmpInErrors.setStatus(_A)
_CInetIcmpOutMsgs_Type=Counter32
_CInetIcmpOutMsgs_Object=MibTableColumn
cInetIcmpOutMsgs=_CInetIcmpOutMsgs_Object((1,3,6,1,4,1,9,10,86,1,3,1,1,5),_CInetIcmpOutMsgs_Type())
cInetIcmpOutMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetIcmpOutMsgs.setStatus(_A)
_CInetIcmpOutErrors_Type=Counter32
_CInetIcmpOutErrors_Object=MibTableColumn
cInetIcmpOutErrors=_CInetIcmpOutErrors_Object((1,3,6,1,4,1,9,10,86,1,3,1,1,6),_CInetIcmpOutErrors_Type())
cInetIcmpOutErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetIcmpOutErrors.setStatus(_A)
_CInetIcmpMsgTable_Object=MibTable
cInetIcmpMsgTable=_CInetIcmpMsgTable_Object((1,3,6,1,4,1,9,10,86,1,3,2))
if mibBuilder.loadTexts:cInetIcmpMsgTable.setStatus(_A)
_CInetIcmpMsgEntry_Object=MibTableRow
cInetIcmpMsgEntry=_CInetIcmpMsgEntry_Object((1,3,6,1,4,1,9,10,86,1,3,2,1))
cInetIcmpMsgEntry.setIndexNames((0,_B,_e),(0,_B,_f),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:cInetIcmpMsgEntry.setStatus(_A)
_CInetIcmpMsgAFType_Type=InetAddressType
_CInetIcmpMsgAFType_Object=MibTableColumn
cInetIcmpMsgAFType=_CInetIcmpMsgAFType_Object((1,3,6,1,4,1,9,10,86,1,3,2,1,1),_CInetIcmpMsgAFType_Type())
cInetIcmpMsgAFType.setMaxAccess(_D)
if mibBuilder.loadTexts:cInetIcmpMsgAFType.setStatus(_A)
_CInetIcmpMsgIfIndex_Type=InterfaceIndexOrZero
_CInetIcmpMsgIfIndex_Object=MibTableColumn
cInetIcmpMsgIfIndex=_CInetIcmpMsgIfIndex_Object((1,3,6,1,4,1,9,10,86,1,3,2,1,2),_CInetIcmpMsgIfIndex_Type())
cInetIcmpMsgIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cInetIcmpMsgIfIndex.setStatus(_A)
class _CInetIcmpMsgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CInetIcmpMsgType_Type.__name__=_E
_CInetIcmpMsgType_Object=MibTableColumn
cInetIcmpMsgType=_CInetIcmpMsgType_Object((1,3,6,1,4,1,9,10,86,1,3,2,1,3),_CInetIcmpMsgType_Type())
cInetIcmpMsgType.setMaxAccess(_D)
if mibBuilder.loadTexts:cInetIcmpMsgType.setStatus(_A)
class _CInetIcmpMsgCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_CInetIcmpMsgCode_Type.__name__=_E
_CInetIcmpMsgCode_Object=MibTableColumn
cInetIcmpMsgCode=_CInetIcmpMsgCode_Object((1,3,6,1,4,1,9,10,86,1,3,2,1,4),_CInetIcmpMsgCode_Type())
cInetIcmpMsgCode.setMaxAccess(_D)
if mibBuilder.loadTexts:cInetIcmpMsgCode.setStatus(_A)
_CInetIcmpMsgInPkts_Type=Counter32
_CInetIcmpMsgInPkts_Object=MibTableColumn
cInetIcmpMsgInPkts=_CInetIcmpMsgInPkts_Object((1,3,6,1,4,1,9,10,86,1,3,2,1,5),_CInetIcmpMsgInPkts_Type())
cInetIcmpMsgInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetIcmpMsgInPkts.setStatus(_A)
_CInetIcmpMsgOutPkts_Type=Counter32
_CInetIcmpMsgOutPkts_Object=MibTableColumn
cInetIcmpMsgOutPkts=_CInetIcmpMsgOutPkts_Object((1,3,6,1,4,1,9,10,86,1,3,2,1,6),_CInetIcmpMsgOutPkts_Type())
cInetIcmpMsgOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetIcmpMsgOutPkts.setStatus(_A)
_CiscoIpMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIpMIBConformance=_CiscoIpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,86,2))
_CiscoIpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpMIBCompliances=_CiscoIpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,86,2,1))
_CiscoIpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpMIBGroups=_CiscoIpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,86,2,2))
ciscoIpAddressPfxGroup=ObjectGroup((1,3,6,1,4,1,9,10,86,2,2,1))
ciscoIpAddressPfxGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:ciscoIpAddressPfxGroup.setStatus(_A)
ciscoIpAddressGroup=ObjectGroup((1,3,6,1,4,1,9,10,86,2,2,2))
ciscoIpAddressGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:ciscoIpAddressGroup.setStatus(_A)
ciscoInetNetToMediaGroup=ObjectGroup((1,3,6,1,4,1,9,10,86,2,2,3))
ciscoInetNetToMediaGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ciscoInetNetToMediaGroup.setStatus(_A)
ciscoInetIcmpGroup=ObjectGroup((1,3,6,1,4,1,9,10,86,2,2,4))
ciscoInetIcmpGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:ciscoInetIcmpGroup.setStatus(_A)
ciscoInetIcmpMsgGroup=ObjectGroup((1,3,6,1,4,1,9,10,86,2,2,5))
ciscoInetIcmpMsgGroup.setObjects(*((_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ciscoInetIcmpMsgGroup.setStatus(_A)
ciscoIpv6GeneralGroup=ObjectGroup((1,3,6,1,4,1,9,10,86,2,2,6))
ciscoIpv6GeneralGroup.setObjects(*((_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:ciscoIpv6GeneralGroup.setStatus(_A)
ciscoIpv6InterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,10,86,2,2,7))
ciscoIpv6InterfaceGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:ciscoIpv6InterfaceGroup.setStatus(_A)
ciscoIpv6ScopeGroup=ObjectGroup((1,3,6,1,4,1,9,10,86,2,2,8))
ciscoIpv6ScopeGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:ciscoIpv6ScopeGroup.setStatus(_A)
ciscoIpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,86,2,1,1))
ciscoIpMIBCompliance.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:ciscoIpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Ipv6AddrIfIdentifier':Ipv6AddrIfIdentifier,'ScopeId':ScopeId,'ciscoIetfIpMIB':ciscoIetfIpMIB,'ciscoIetfIpMIBObjects':ciscoIetfIpMIBObjects,'cIp':cIp,'cIpAddressPfxTable':cIpAddressPfxTable,'cIpAddressPfxEntry':cIpAddressPfxEntry,_M:cIpAddressPfxIfIndex,_N:cIpAddressPfxType,_O:cIpAddressPfxPfx,_P:cIpAddressPfxLength,_i:cIpAddressPfxOrigin,_j:cIpAddressPfxOnLinkFlag,_k:cIpAddressPfxAutonomousFlag,_l:cIpAddressPfxAdvPfdLifetime,_m:cIpAddressPfxAdvValidLifetime,'cIpAddressTable':cIpAddressTable,'cIpAddressEntry':cIpAddressEntry,_T:cIpAddressAddrType,_U:cIpAddressAddr,_n:cIpAddressIfIndex,_o:cIpAddressType,_p:cIpAddressPrefix,_q:cIpAddressOrigin,_r:cIpAddressStatus,'cInetNetToMediaTable':cInetNetToMediaTable,'cInetNetToMediaEntry':cInetNetToMediaEntry,_W:cInetNetToMediaNetAddressType,_X:cInetNetToMediaNetAddress,_s:cInetNetToMediaPhysAddress,_t:cInetNetToMediaLastUpdated,_u:cInetNetToMediaType,_v:cInetNetToMediaState,'cIpv6ScopeIdTable':cIpv6ScopeIdTable,'cIpv6ScopeIdEntry':cIpv6ScopeIdEntry,_Z:cIpv6ScopeIdIfIndex,_A9:cIpv6ScopeIdLinkLocal,_AA:cIpv6ScopeIdSubnetLocal,_AB:cIpv6ScopeIdAdminLocal,_AC:cIpv6ScopeIdSiteLocal,_AD:cIpv6ScopeId6,_AE:cIpv6ScopeId7,_AF:cIpv6ScopeIdOrganizationLocal,_AG:cIpv6ScopeId9,_AH:cIpv6ScopeIdA,_AI:cIpv6ScopeIdB,_AJ:cIpv6ScopeIdC,_AK:cIpv6ScopeIdD,'cIpv6':cIpv6,_A2:cIpv6Forwarding,_A3:cIpv6DefaultHopLimit,'cIpv6InterfaceTable':cIpv6InterfaceTable,'cIpv6InterfaceEntry':cIpv6InterfaceEntry,_a:cIpv6InterfaceIfIndex,_A4:cIpv6InterfaceEffectiveMtu,_A5:cIpv6InterfaceReasmMaxSize,_A6:cIpv6InterfaceIdentifier,_A7:cIpv6InterfaceIdentifierLength,_A8:cIpv6InterfacePhysicalAddress,'cIcmp':cIcmp,'cInetIcmpTable':cInetIcmpTable,'cInetIcmpEntry':cInetIcmpEntry,_c:cInetIcmpAFType,_d:cInetIcmpIfIndex,_w:cInetIcmpInMsgs,_x:cInetIcmpInErrors,_y:cInetIcmpOutMsgs,_z:cInetIcmpOutErrors,'cInetIcmpMsgTable':cInetIcmpMsgTable,'cInetIcmpMsgEntry':cInetIcmpMsgEntry,_e:cInetIcmpMsgAFType,_f:cInetIcmpMsgIfIndex,_g:cInetIcmpMsgType,_h:cInetIcmpMsgCode,_A0:cInetIcmpMsgInPkts,_A1:cInetIcmpMsgOutPkts,'ciscoIpMIBConformance':ciscoIpMIBConformance,'ciscoIpMIBCompliances':ciscoIpMIBCompliances,'ciscoIpMIBCompliance':ciscoIpMIBCompliance,'ciscoIpMIBGroups':ciscoIpMIBGroups,_AL:ciscoIpAddressPfxGroup,_AM:ciscoIpAddressGroup,_AN:ciscoInetNetToMediaGroup,_AO:ciscoInetIcmpGroup,_AP:ciscoInetIcmpMsgGroup,_AQ:ciscoIpv6GeneralGroup,_AR:ciscoIpv6InterfaceGroup,_AS:ciscoIpv6ScopeGroup})