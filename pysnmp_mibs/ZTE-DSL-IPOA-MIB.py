_L='zxDslIpoaUserInfoBrgPortId'
_K='not-accessible'
_J='zxDslIpoaUserConfBrgPortId'
_I='minutes'
_H='ZTE-DSL-IPOA-MIB'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxDsl,=mibBuilder.importSymbols('ZTE-DSL-MIB','zxDsl')
zxDslIpoaMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,44))
_ZxDslIpoaMibObjects_ObjectIdentity=ObjectIdentity
zxDslIpoaMibObjects=_ZxDslIpoaMibObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,44,1))
_ZxDslIpoaGlobalObjects_ObjectIdentity=ObjectIdentity
zxDslIpoaGlobalObjects=_ZxDslIpoaGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,44,1,1))
_ZxDslIpoaDefGateway_Type=IpAddress
_ZxDslIpoaDefGateway_Object=MibScalar
zxDslIpoaDefGateway=_ZxDslIpoaDefGateway_Object((1,3,6,1,4,1,3902,1004,44,1,1,1),_ZxDslIpoaDefGateway_Type())
zxDslIpoaDefGateway.setMaxAccess(_G)
if mibBuilder.loadTexts:zxDslIpoaDefGateway.setStatus(_A)
class _ZxDslIpoaQueryInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_ZxDslIpoaQueryInterval_Type.__name__=_C
_ZxDslIpoaQueryInterval_Object=MibScalar
zxDslIpoaQueryInterval=_ZxDslIpoaQueryInterval_Object((1,3,6,1,4,1,3902,1004,44,1,1,2),_ZxDslIpoaQueryInterval_Type())
zxDslIpoaQueryInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:zxDslIpoaQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:zxDslIpoaQueryInterval.setUnits(_I)
class _ZxDslIpoaGatewayARPInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_ZxDslIpoaGatewayARPInterval_Type.__name__=_C
_ZxDslIpoaGatewayARPInterval_Object=MibScalar
zxDslIpoaGatewayARPInterval=_ZxDslIpoaGatewayARPInterval_Object((1,3,6,1,4,1,3902,1004,44,1,1,3),_ZxDslIpoaGatewayARPInterval_Type())
zxDslIpoaGatewayARPInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:zxDslIpoaGatewayARPInterval.setStatus(_A)
if mibBuilder.loadTexts:zxDslIpoaGatewayARPInterval.setUnits(_I)
_ZxDslIpoaUser_ObjectIdentity=ObjectIdentity
zxDslIpoaUser=_ZxDslIpoaUser_ObjectIdentity((1,3,6,1,4,1,3902,1004,44,1,2))
_ZxDslIpoaUserConfTable_Object=MibTable
zxDslIpoaUserConfTable=_ZxDslIpoaUserConfTable_Object((1,3,6,1,4,1,3902,1004,44,1,2,1))
if mibBuilder.loadTexts:zxDslIpoaUserConfTable.setStatus(_A)
_ZxDslIpoaUserConfEntry_Object=MibTableRow
zxDslIpoaUserConfEntry=_ZxDslIpoaUserConfEntry_Object((1,3,6,1,4,1,3902,1004,44,1,2,1,1))
zxDslIpoaUserConfEntry.setIndexNames((0,_E,_F),(0,_H,_J))
if mibBuilder.loadTexts:zxDslIpoaUserConfEntry.setStatus(_A)
_ZxDslIpoaUserConfBrgPortId_Type=Integer32
_ZxDslIpoaUserConfBrgPortId_Object=MibTableColumn
zxDslIpoaUserConfBrgPortId=_ZxDslIpoaUserConfBrgPortId_Object((1,3,6,1,4,1,3902,1004,44,1,2,1,1,1),_ZxDslIpoaUserConfBrgPortId_Type())
zxDslIpoaUserConfBrgPortId.setMaxAccess(_K)
if mibBuilder.loadTexts:zxDslIpoaUserConfBrgPortId.setStatus(_A)
_ZxDslIpoaUserConfIp_Type=IpAddress
_ZxDslIpoaUserConfIp_Object=MibTableColumn
zxDslIpoaUserConfIp=_ZxDslIpoaUserConfIp_Object((1,3,6,1,4,1,3902,1004,44,1,2,1,1,2),_ZxDslIpoaUserConfIp_Type())
zxDslIpoaUserConfIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpoaUserConfIp.setStatus(_A)
class _ZxDslIpoaUserConfInAtmArp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxDslIpoaUserConfInAtmArp_Type.__name__=_C
_ZxDslIpoaUserConfInAtmArp_Object=MibTableColumn
zxDslIpoaUserConfInAtmArp=_ZxDslIpoaUserConfInAtmArp_Object((1,3,6,1,4,1,3902,1004,44,1,2,1,1,3),_ZxDslIpoaUserConfInAtmArp_Type())
zxDslIpoaUserConfInAtmArp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpoaUserConfInAtmArp.setStatus(_A)
class _ZxDslIpoaUserConfLayer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('layer2',1),('layer3',2)))
_ZxDslIpoaUserConfLayer_Type.__name__=_C
_ZxDslIpoaUserConfLayer_Object=MibTableColumn
zxDslIpoaUserConfLayer=_ZxDslIpoaUserConfLayer_Object((1,3,6,1,4,1,3902,1004,44,1,2,1,1,4),_ZxDslIpoaUserConfLayer_Type())
zxDslIpoaUserConfLayer.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpoaUserConfLayer.setStatus(_A)
_ZxDslIpoaUserConfL2gatewayIp_Type=IpAddress
_ZxDslIpoaUserConfL2gatewayIp_Object=MibTableColumn
zxDslIpoaUserConfL2gatewayIp=_ZxDslIpoaUserConfL2gatewayIp_Object((1,3,6,1,4,1,3902,1004,44,1,2,1,1,5),_ZxDslIpoaUserConfL2gatewayIp_Type())
zxDslIpoaUserConfL2gatewayIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpoaUserConfL2gatewayIp.setStatus(_A)
_ZxDslIpoaUserConfL2gatewayMac_Type=MacAddress
_ZxDslIpoaUserConfL2gatewayMac_Object=MibTableColumn
zxDslIpoaUserConfL2gatewayMac=_ZxDslIpoaUserConfL2gatewayMac_Object((1,3,6,1,4,1,3902,1004,44,1,2,1,1,6),_ZxDslIpoaUserConfL2gatewayMac_Type())
zxDslIpoaUserConfL2gatewayMac.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpoaUserConfL2gatewayMac.setStatus(_A)
_ZxDslIpoaUserConfRowStatus_Type=RowStatus
_ZxDslIpoaUserConfRowStatus_Object=MibTableColumn
zxDslIpoaUserConfRowStatus=_ZxDslIpoaUserConfRowStatus_Object((1,3,6,1,4,1,3902,1004,44,1,2,1,1,10),_ZxDslIpoaUserConfRowStatus_Type())
zxDslIpoaUserConfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpoaUserConfRowStatus.setStatus(_A)
_ZxDslIpoaUserInfoTable_Object=MibTable
zxDslIpoaUserInfoTable=_ZxDslIpoaUserInfoTable_Object((1,3,6,1,4,1,3902,1004,44,1,2,2))
if mibBuilder.loadTexts:zxDslIpoaUserInfoTable.setStatus(_A)
_ZxDslIpoaUserInfoEntry_Object=MibTableRow
zxDslIpoaUserInfoEntry=_ZxDslIpoaUserInfoEntry_Object((1,3,6,1,4,1,3902,1004,44,1,2,2,1))
zxDslIpoaUserInfoEntry.setIndexNames((0,_E,_F),(0,_H,_L))
if mibBuilder.loadTexts:zxDslIpoaUserInfoEntry.setStatus(_A)
_ZxDslIpoaUserInfoBrgPortId_Type=Integer32
_ZxDslIpoaUserInfoBrgPortId_Object=MibTableColumn
zxDslIpoaUserInfoBrgPortId=_ZxDslIpoaUserInfoBrgPortId_Object((1,3,6,1,4,1,3902,1004,44,1,2,2,1,1),_ZxDslIpoaUserInfoBrgPortId_Type())
zxDslIpoaUserInfoBrgPortId.setMaxAccess(_K)
if mibBuilder.loadTexts:zxDslIpoaUserInfoBrgPortId.setStatus(_A)
_ZxDslIpoaUserInfoVlan_Type=Integer32
_ZxDslIpoaUserInfoVlan_Object=MibTableColumn
zxDslIpoaUserInfoVlan=_ZxDslIpoaUserInfoVlan_Object((1,3,6,1,4,1,3902,1004,44,1,2,2,1,2),_ZxDslIpoaUserInfoVlan_Type())
zxDslIpoaUserInfoVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslIpoaUserInfoVlan.setStatus(_A)
_ZxDslIpoaUserInfoIp_Type=IpAddress
_ZxDslIpoaUserInfoIp_Object=MibTableColumn
zxDslIpoaUserInfoIp=_ZxDslIpoaUserInfoIp_Object((1,3,6,1,4,1,3902,1004,44,1,2,2,1,3),_ZxDslIpoaUserInfoIp_Type())
zxDslIpoaUserInfoIp.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslIpoaUserInfoIp.setStatus(_A)
_ZxDslIpoaUserInfoMac_Type=MacAddress
_ZxDslIpoaUserInfoMac_Object=MibTableColumn
zxDslIpoaUserInfoMac=_ZxDslIpoaUserInfoMac_Object((1,3,6,1,4,1,3902,1004,44,1,2,2,1,4),_ZxDslIpoaUserInfoMac_Type())
zxDslIpoaUserInfoMac.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslIpoaUserInfoMac.setStatus(_A)
_ZxDslIpoaUserInfoGatewayIp_Type=IpAddress
_ZxDslIpoaUserInfoGatewayIp_Object=MibTableColumn
zxDslIpoaUserInfoGatewayIp=_ZxDslIpoaUserInfoGatewayIp_Object((1,3,6,1,4,1,3902,1004,44,1,2,2,1,5),_ZxDslIpoaUserInfoGatewayIp_Type())
zxDslIpoaUserInfoGatewayIp.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslIpoaUserInfoGatewayIp.setStatus(_A)
_ZxDslIpoaUserInfoGatewayMac_Type=MacAddress
_ZxDslIpoaUserInfoGatewayMac_Object=MibTableColumn
zxDslIpoaUserInfoGatewayMac=_ZxDslIpoaUserInfoGatewayMac_Object((1,3,6,1,4,1,3902,1004,44,1,2,2,1,6),_ZxDslIpoaUserInfoGatewayMac_Type())
zxDslIpoaUserInfoGatewayMac.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslIpoaUserInfoGatewayMac.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'zxDslIpoaMib':zxDslIpoaMib,'zxDslIpoaMibObjects':zxDslIpoaMibObjects,'zxDslIpoaGlobalObjects':zxDslIpoaGlobalObjects,'zxDslIpoaDefGateway':zxDslIpoaDefGateway,'zxDslIpoaQueryInterval':zxDslIpoaQueryInterval,'zxDslIpoaGatewayARPInterval':zxDslIpoaGatewayARPInterval,'zxDslIpoaUser':zxDslIpoaUser,'zxDslIpoaUserConfTable':zxDslIpoaUserConfTable,'zxDslIpoaUserConfEntry':zxDslIpoaUserConfEntry,_J:zxDslIpoaUserConfBrgPortId,'zxDslIpoaUserConfIp':zxDslIpoaUserConfIp,'zxDslIpoaUserConfInAtmArp':zxDslIpoaUserConfInAtmArp,'zxDslIpoaUserConfLayer':zxDslIpoaUserConfLayer,'zxDslIpoaUserConfL2gatewayIp':zxDslIpoaUserConfL2gatewayIp,'zxDslIpoaUserConfL2gatewayMac':zxDslIpoaUserConfL2gatewayMac,'zxDslIpoaUserConfRowStatus':zxDslIpoaUserConfRowStatus,'zxDslIpoaUserInfoTable':zxDslIpoaUserInfoTable,'zxDslIpoaUserInfoEntry':zxDslIpoaUserInfoEntry,_L:zxDslIpoaUserInfoBrgPortId,'zxDslIpoaUserInfoVlan':zxDslIpoaUserInfoVlan,'zxDslIpoaUserInfoIp':zxDslIpoaUserInfoIp,'zxDslIpoaUserInfoMac':zxDslIpoaUserInfoMac,'zxDslIpoaUserInfoGatewayIp':zxDslIpoaUserInfoGatewayIp,'zxDslIpoaUserInfoGatewayMac':zxDslIpoaUserInfoGatewayMac})