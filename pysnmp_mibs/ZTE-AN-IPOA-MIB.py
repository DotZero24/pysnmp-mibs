_G='zxAnIpoaIfIndex'
_F='ZTE-AN-IPOA-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnIpoaMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,33))
_ZxAnIpoaMibObjects_ObjectIdentity=ObjectIdentity
zxAnIpoaMibObjects=_ZxAnIpoaMibObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,33,1))
_ZxAnIpoaDefGateway_Type=IpAddress
_ZxAnIpoaDefGateway_Object=MibScalar
zxAnIpoaDefGateway=_ZxAnIpoaDefGateway_Object((1,3,6,1,4,1,3902,1015,33,1,1),_ZxAnIpoaDefGateway_Type())
zxAnIpoaDefGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIpoaDefGateway.setStatus(_A)
_ZxAnIpoaQueryInterval_Type=Integer32
_ZxAnIpoaQueryInterval_Object=MibScalar
zxAnIpoaQueryInterval=_ZxAnIpoaQueryInterval_Object((1,3,6,1,4,1,3902,1015,33,1,2),_ZxAnIpoaQueryInterval_Type())
zxAnIpoaQueryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIpoaQueryInterval.setStatus(_A)
_ZxAnIpoaGatewayARPInterval_Type=Integer32
_ZxAnIpoaGatewayARPInterval_Object=MibScalar
zxAnIpoaGatewayARPInterval=_ZxAnIpoaGatewayARPInterval_Object((1,3,6,1,4,1,3902,1015,33,1,3),_ZxAnIpoaGatewayARPInterval_Type())
zxAnIpoaGatewayARPInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIpoaGatewayARPInterval.setStatus(_A)
_ZxAnIpoaUserConfTable_Object=MibTable
zxAnIpoaUserConfTable=_ZxAnIpoaUserConfTable_Object((1,3,6,1,4,1,3902,1015,33,1,10))
if mibBuilder.loadTexts:zxAnIpoaUserConfTable.setStatus(_A)
_ZxAnIpoaUserConfEntry_Object=MibTableRow
zxAnIpoaUserConfEntry=_ZxAnIpoaUserConfEntry_Object((1,3,6,1,4,1,3902,1015,33,1,10,1))
zxAnIpoaUserConfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAnIpoaUserConfEntry.setStatus(_A)
_ZxAnIpoaIfIndex_Type=ZxAnIfindex
_ZxAnIpoaIfIndex_Object=MibTableColumn
zxAnIpoaIfIndex=_ZxAnIpoaIfIndex_Object((1,3,6,1,4,1,3902,1015,33,1,10,1,1),_ZxAnIpoaIfIndex_Type())
zxAnIpoaIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxAnIpoaIfIndex.setStatus(_A)
_ZxAnIpoaUserConfIp_Type=IpAddress
_ZxAnIpoaUserConfIp_Object=MibTableColumn
zxAnIpoaUserConfIp=_ZxAnIpoaUserConfIp_Object((1,3,6,1,4,1,3902,1015,33,1,10,1,2),_ZxAnIpoaUserConfIp_Type())
zxAnIpoaUserConfIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnIpoaUserConfIp.setStatus(_A)
class _ZxAnIpoaUserConfInAtmArp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxAnIpoaUserConfInAtmArp_Type.__name__=_D
_ZxAnIpoaUserConfInAtmArp_Object=MibTableColumn
zxAnIpoaUserConfInAtmArp=_ZxAnIpoaUserConfInAtmArp_Object((1,3,6,1,4,1,3902,1015,33,1,10,1,3),_ZxAnIpoaUserConfInAtmArp_Type())
zxAnIpoaUserConfInAtmArp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnIpoaUserConfInAtmArp.setStatus(_A)
class _ZxAnIpoaUserConfLayer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('layer2',1),('layer3',2)))
_ZxAnIpoaUserConfLayer_Type.__name__=_D
_ZxAnIpoaUserConfLayer_Object=MibTableColumn
zxAnIpoaUserConfLayer=_ZxAnIpoaUserConfLayer_Object((1,3,6,1,4,1,3902,1015,33,1,10,1,4),_ZxAnIpoaUserConfLayer_Type())
zxAnIpoaUserConfLayer.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnIpoaUserConfLayer.setStatus(_A)
_ZxAnIpoaUserConfL2gatewayIp_Type=IpAddress
_ZxAnIpoaUserConfL2gatewayIp_Object=MibTableColumn
zxAnIpoaUserConfL2gatewayIp=_ZxAnIpoaUserConfL2gatewayIp_Object((1,3,6,1,4,1,3902,1015,33,1,10,1,5),_ZxAnIpoaUserConfL2gatewayIp_Type())
zxAnIpoaUserConfL2gatewayIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnIpoaUserConfL2gatewayIp.setStatus(_A)
_ZxAnIpoaUserConfL2gatewayMac_Type=MacAddress
_ZxAnIpoaUserConfL2gatewayMac_Object=MibTableColumn
zxAnIpoaUserConfL2gatewayMac=_ZxAnIpoaUserConfL2gatewayMac_Object((1,3,6,1,4,1,3902,1015,33,1,10,1,6),_ZxAnIpoaUserConfL2gatewayMac_Type())
zxAnIpoaUserConfL2gatewayMac.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnIpoaUserConfL2gatewayMac.setStatus(_A)
_ZxAnIpoaUserConfRowStatus_Type=RowStatus
_ZxAnIpoaUserConfRowStatus_Object=MibTableColumn
zxAnIpoaUserConfRowStatus=_ZxAnIpoaUserConfRowStatus_Object((1,3,6,1,4,1,3902,1015,33,1,10,1,7),_ZxAnIpoaUserConfRowStatus_Type())
zxAnIpoaUserConfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnIpoaUserConfRowStatus.setStatus(_A)
_ZxAnIpoaUserInfoTable_Object=MibTable
zxAnIpoaUserInfoTable=_ZxAnIpoaUserInfoTable_Object((1,3,6,1,4,1,3902,1015,33,1,11))
if mibBuilder.loadTexts:zxAnIpoaUserInfoTable.setStatus(_A)
_ZxAnIpoaUserInfoEntry_Object=MibTableRow
zxAnIpoaUserInfoEntry=_ZxAnIpoaUserInfoEntry_Object((1,3,6,1,4,1,3902,1015,33,1,11,1))
zxAnIpoaUserInfoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAnIpoaUserInfoEntry.setStatus(_A)
_ZxAnIpoaUserInfoVlan_Type=Integer32
_ZxAnIpoaUserInfoVlan_Object=MibTableColumn
zxAnIpoaUserInfoVlan=_ZxAnIpoaUserInfoVlan_Object((1,3,6,1,4,1,3902,1015,33,1,11,1,1),_ZxAnIpoaUserInfoVlan_Type())
zxAnIpoaUserInfoVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnIpoaUserInfoVlan.setStatus(_A)
_ZxAnIpoaUserInfoIp_Type=IpAddress
_ZxAnIpoaUserInfoIp_Object=MibTableColumn
zxAnIpoaUserInfoIp=_ZxAnIpoaUserInfoIp_Object((1,3,6,1,4,1,3902,1015,33,1,11,1,2),_ZxAnIpoaUserInfoIp_Type())
zxAnIpoaUserInfoIp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnIpoaUserInfoIp.setStatus(_A)
_ZxAnIpoaUserInfoMac_Type=MacAddress
_ZxAnIpoaUserInfoMac_Object=MibTableColumn
zxAnIpoaUserInfoMac=_ZxAnIpoaUserInfoMac_Object((1,3,6,1,4,1,3902,1015,33,1,11,1,3),_ZxAnIpoaUserInfoMac_Type())
zxAnIpoaUserInfoMac.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnIpoaUserInfoMac.setStatus(_A)
_ZxAnIpoaUserInfoGatewayIp_Type=IpAddress
_ZxAnIpoaUserInfoGatewayIp_Object=MibTableColumn
zxAnIpoaUserInfoGatewayIp=_ZxAnIpoaUserInfoGatewayIp_Object((1,3,6,1,4,1,3902,1015,33,1,11,1,4),_ZxAnIpoaUserInfoGatewayIp_Type())
zxAnIpoaUserInfoGatewayIp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnIpoaUserInfoGatewayIp.setStatus(_A)
_ZxAnIpoaUserInfoGatewayMac_Type=MacAddress
_ZxAnIpoaUserInfoGatewayMac_Object=MibTableColumn
zxAnIpoaUserInfoGatewayMac=_ZxAnIpoaUserInfoGatewayMac_Object((1,3,6,1,4,1,3902,1015,33,1,11,1,5),_ZxAnIpoaUserInfoGatewayMac_Type())
zxAnIpoaUserInfoGatewayMac.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnIpoaUserInfoGatewayMac.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zxAnIpoaMib':zxAnIpoaMib,'zxAnIpoaMibObjects':zxAnIpoaMibObjects,'zxAnIpoaDefGateway':zxAnIpoaDefGateway,'zxAnIpoaQueryInterval':zxAnIpoaQueryInterval,'zxAnIpoaGatewayARPInterval':zxAnIpoaGatewayARPInterval,'zxAnIpoaUserConfTable':zxAnIpoaUserConfTable,'zxAnIpoaUserConfEntry':zxAnIpoaUserConfEntry,_G:zxAnIpoaIfIndex,'zxAnIpoaUserConfIp':zxAnIpoaUserConfIp,'zxAnIpoaUserConfInAtmArp':zxAnIpoaUserConfInAtmArp,'zxAnIpoaUserConfLayer':zxAnIpoaUserConfLayer,'zxAnIpoaUserConfL2gatewayIp':zxAnIpoaUserConfL2gatewayIp,'zxAnIpoaUserConfL2gatewayMac':zxAnIpoaUserConfL2gatewayMac,'zxAnIpoaUserConfRowStatus':zxAnIpoaUserConfRowStatus,'zxAnIpoaUserInfoTable':zxAnIpoaUserInfoTable,'zxAnIpoaUserInfoEntry':zxAnIpoaUserInfoEntry,'zxAnIpoaUserInfoVlan':zxAnIpoaUserInfoVlan,'zxAnIpoaUserInfoIp':zxAnIpoaUserInfoIp,'zxAnIpoaUserInfoMac':zxAnIpoaUserInfoMac,'zxAnIpoaUserInfoGatewayIp':zxAnIpoaUserInfoGatewayIp,'zxAnIpoaUserInfoGatewayMac':zxAnIpoaUserInfoGatewayMac})