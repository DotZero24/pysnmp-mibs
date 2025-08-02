_c='hpicfDhcpClientTR069OptionsGroup'
_b='hpicfDhcpv6ClientGroup'
_a='hpicfDhcpClientAuthGroup'
_Z='hpicfDhcpClientVendorSpecOptionsGroup'
_Y='hpicfDhcpClientOptionsGroup'
_X='hpicfDhcpClientTR069AcsUrlOptionStatus'
_W='hpicfDhcpv6ClientDuid'
_V='hpicfDhcpClientPktAuthFailed'
_U='hpicfDhcpClientPktRx'
_T='hpicfDhcpClientPktTx'
_S='hpicfDhcpClientKeyChain'
_R='hpicfDhcpClientAuthType'
_Q='hpicfDhcpClientImageFileUpdate'
_P='hpicfDhcpClientHostNameOption'
_O='hpicfDhcpClientVendorSpecOptionStatus'
_N='hpicfIPVersion'
_M='disabled'
_L='enabled'
_K='disable'
_J='enable'
_I='DisplayString'
_H='OctetString'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='HP-ICF-DHCPCLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_F,_G)
InetVersion,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetVersion')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
hpicfDhcpClient=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,57))
if mibBuilder.loadTexts:hpicfDhcpClient.setRevisions(('2013-06-01 00:00','2012-05-31 00:00','2010-08-09 00:00','2009-03-18 00:00','2008-10-30 00:00','2008-08-27 00:38'))
_HpicfDhcpClientOptions_ObjectIdentity=ObjectIdentity
hpicfDhcpClientOptions=_HpicfDhcpClientOptions_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,57,1))
class _HpicfDhcpClientVendorSpecOptionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpicfDhcpClientVendorSpecOptionStatus_Type.__name__=_C
_HpicfDhcpClientVendorSpecOptionStatus_Object=MibScalar
hpicfDhcpClientVendorSpecOptionStatus=_HpicfDhcpClientVendorSpecOptionStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,1),_HpicfDhcpClientVendorSpecOptionStatus_Type())
hpicfDhcpClientVendorSpecOptionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpClientVendorSpecOptionStatus.setStatus(_A)
class _HpicfDhcpClientHostNameOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpicfDhcpClientHostNameOption_Type.__name__=_C
_HpicfDhcpClientHostNameOption_Object=MibScalar
hpicfDhcpClientHostNameOption=_HpicfDhcpClientHostNameOption_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,2),_HpicfDhcpClientHostNameOption_Type())
hpicfDhcpClientHostNameOption.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpClientHostNameOption.setStatus(_A)
class _HpicfDhcpClientImageFileUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_HpicfDhcpClientImageFileUpdate_Type.__name__=_C
_HpicfDhcpClientImageFileUpdate_Object=MibScalar
hpicfDhcpClientImageFileUpdate=_HpicfDhcpClientImageFileUpdate_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,3),_HpicfDhcpClientImageFileUpdate_Type())
hpicfDhcpClientImageFileUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpClientImageFileUpdate.setStatus(_A)
_HpicfDhcpClientintfTable_Object=MibTable
hpicfDhcpClientintfTable=_HpicfDhcpClientintfTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,4))
if mibBuilder.loadTexts:hpicfDhcpClientintfTable.setStatus(_A)
_HpicfDhcpClientintfEntry_Object=MibTableRow
hpicfDhcpClientintfEntry=_HpicfDhcpClientintfEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,4,1))
hpicfDhcpClientintfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpicfDhcpClientintfEntry.setStatus(_A)
class _HpicfDhcpClientAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('md5',1)))
_HpicfDhcpClientAuthType_Type.__name__=_C
_HpicfDhcpClientAuthType_Object=MibTableColumn
hpicfDhcpClientAuthType=_HpicfDhcpClientAuthType_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,4,1,1),_HpicfDhcpClientAuthType_Type())
hpicfDhcpClientAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpClientAuthType.setStatus(_A)
class _HpicfDhcpClientKeyChain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_HpicfDhcpClientKeyChain_Type.__name__=_I
_HpicfDhcpClientKeyChain_Object=MibTableColumn
hpicfDhcpClientKeyChain=_HpicfDhcpClientKeyChain_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,4,1,2),_HpicfDhcpClientKeyChain_Type())
hpicfDhcpClientKeyChain.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpClientKeyChain.setStatus(_A)
_HpicfDhcpClientStatisticsTable_Object=MibTable
hpicfDhcpClientStatisticsTable=_HpicfDhcpClientStatisticsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,5))
if mibBuilder.loadTexts:hpicfDhcpClientStatisticsTable.setStatus(_A)
_HpicfDhcpClientStatisticsEntry_Object=MibTableRow
hpicfDhcpClientStatisticsEntry=_HpicfDhcpClientStatisticsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,5,1))
hpicfDhcpClientStatisticsEntry.setIndexNames((0,_F,_G),(0,_B,_N))
if mibBuilder.loadTexts:hpicfDhcpClientStatisticsEntry.setStatus(_A)
_HpicfIPVersion_Type=InetVersion
_HpicfIPVersion_Object=MibTableColumn
hpicfIPVersion=_HpicfIPVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,5,1,1),_HpicfIPVersion_Type())
hpicfIPVersion.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfIPVersion.setStatus(_A)
_HpicfDhcpClientPktTx_Type=Counter32
_HpicfDhcpClientPktTx_Object=MibTableColumn
hpicfDhcpClientPktTx=_HpicfDhcpClientPktTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,5,1,2),_HpicfDhcpClientPktTx_Type())
hpicfDhcpClientPktTx.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDhcpClientPktTx.setStatus(_A)
_HpicfDhcpClientPktRx_Type=Counter32
_HpicfDhcpClientPktRx_Object=MibTableColumn
hpicfDhcpClientPktRx=_HpicfDhcpClientPktRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,5,1,3),_HpicfDhcpClientPktRx_Type())
hpicfDhcpClientPktRx.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDhcpClientPktRx.setStatus(_A)
_HpicfDhcpClientPktAuthFailed_Type=Counter32
_HpicfDhcpClientPktAuthFailed_Object=MibTableColumn
hpicfDhcpClientPktAuthFailed=_HpicfDhcpClientPktAuthFailed_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,5,1,4),_HpicfDhcpClientPktAuthFailed_Type())
hpicfDhcpClientPktAuthFailed.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDhcpClientPktAuthFailed.setStatus(_A)
class _HpicfDhcpv6ClientDuid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(25,128))
_HpicfDhcpv6ClientDuid_Type.__name__=_H
_HpicfDhcpv6ClientDuid_Object=MibScalar
hpicfDhcpv6ClientDuid=_HpicfDhcpv6ClientDuid_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,6),_HpicfDhcpv6ClientDuid_Type())
hpicfDhcpv6ClientDuid.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDhcpv6ClientDuid.setStatus(_A)
class _HpicfDhcpClientTR069AcsUrlOptionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_HpicfDhcpClientTR069AcsUrlOptionStatus_Type.__name__=_C
_HpicfDhcpClientTR069AcsUrlOptionStatus_Object=MibScalar
hpicfDhcpClientTR069AcsUrlOptionStatus=_HpicfDhcpClientTR069AcsUrlOptionStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,57,1,7),_HpicfDhcpClientTR069AcsUrlOptionStatus_Type())
hpicfDhcpClientTR069AcsUrlOptionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpClientTR069AcsUrlOptionStatus.setStatus(_A)
_HpicfDhcpClientOptionsConf_ObjectIdentity=ObjectIdentity
hpicfDhcpClientOptionsConf=_HpicfDhcpClientOptionsConf_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,57,2))
_HpicfDhcpClientGroups_ObjectIdentity=ObjectIdentity
hpicfDhcpClientGroups=_HpicfDhcpClientGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,57,2,1))
_HpicfDhcpClientCompliances_ObjectIdentity=ObjectIdentity
hpicfDhcpClientCompliances=_HpicfDhcpClientCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,57,2,2))
hpicfDhcpClientOptionsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,57,2,1,1))
hpicfDhcpClientOptionsGroup.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:hpicfDhcpClientOptionsGroup.setStatus(_A)
hpicfDhcpClientVendorSpecOptionsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,57,2,1,2))
hpicfDhcpClientVendorSpecOptionsGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:hpicfDhcpClientVendorSpecOptionsGroup.setStatus(_A)
hpicfDhcpClientAuthGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,57,2,1,3))
hpicfDhcpClientAuthGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:hpicfDhcpClientAuthGroup.setStatus(_A)
hpicfDhcpv6ClientGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,57,2,1,4))
hpicfDhcpv6ClientGroup.setObjects((_B,_W))
if mibBuilder.loadTexts:hpicfDhcpv6ClientGroup.setStatus(_A)
hpicfDhcpClientTR069OptionsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,57,2,1,5))
hpicfDhcpClientTR069OptionsGroup.setObjects((_B,_X))
if mibBuilder.loadTexts:hpicfDhcpClientTR069OptionsGroup.setStatus(_A)
hpicfDhcpClientCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,57,2,2,1))
hpicfDhcpClientCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:hpicfDhcpClientCompliance.setStatus(_A)
hpicfDhcpClientVendorSpecOptionsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,57,2,2,2))
hpicfDhcpClientVendorSpecOptionsCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:hpicfDhcpClientVendorSpecOptionsCompliance.setStatus(_A)
hpicfDhcpClientAuthCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,57,2,2,3))
hpicfDhcpClientAuthCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:hpicfDhcpClientAuthCompliance.setStatus(_A)
hpicfDhcpv6ClientCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,57,2,2,4))
hpicfDhcpv6ClientCompliance.setObjects((_B,_b))
if mibBuilder.loadTexts:hpicfDhcpv6ClientCompliance.setStatus(_A)
hpicfDhcpClientTR069OptionsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,57,2,2,5))
hpicfDhcpClientTR069OptionsCompliance.setObjects((_B,_c))
if mibBuilder.loadTexts:hpicfDhcpClientTR069OptionsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfDhcpClient':hpicfDhcpClient,'hpicfDhcpClientOptions':hpicfDhcpClientOptions,_O:hpicfDhcpClientVendorSpecOptionStatus,_P:hpicfDhcpClientHostNameOption,_Q:hpicfDhcpClientImageFileUpdate,'hpicfDhcpClientintfTable':hpicfDhcpClientintfTable,'hpicfDhcpClientintfEntry':hpicfDhcpClientintfEntry,_R:hpicfDhcpClientAuthType,_S:hpicfDhcpClientKeyChain,'hpicfDhcpClientStatisticsTable':hpicfDhcpClientStatisticsTable,'hpicfDhcpClientStatisticsEntry':hpicfDhcpClientStatisticsEntry,_N:hpicfIPVersion,_T:hpicfDhcpClientPktTx,_U:hpicfDhcpClientPktRx,_V:hpicfDhcpClientPktAuthFailed,_W:hpicfDhcpv6ClientDuid,_X:hpicfDhcpClientTR069AcsUrlOptionStatus,'hpicfDhcpClientOptionsConf':hpicfDhcpClientOptionsConf,'hpicfDhcpClientGroups':hpicfDhcpClientGroups,_Y:hpicfDhcpClientOptionsGroup,_Z:hpicfDhcpClientVendorSpecOptionsGroup,_a:hpicfDhcpClientAuthGroup,_b:hpicfDhcpv6ClientGroup,_c:hpicfDhcpClientTR069OptionsGroup,'hpicfDhcpClientCompliances':hpicfDhcpClientCompliances,'hpicfDhcpClientCompliance':hpicfDhcpClientCompliance,'hpicfDhcpClientVendorSpecOptionsCompliance':hpicfDhcpClientVendorSpecOptionsCompliance,'hpicfDhcpClientAuthCompliance':hpicfDhcpClientAuthCompliance,'hpicfDhcpv6ClientCompliance':hpicfDhcpv6ClientCompliance,'hpicfDhcpClientTR069OptionsCompliance':hpicfDhcpClientTR069OptionsCompliance})