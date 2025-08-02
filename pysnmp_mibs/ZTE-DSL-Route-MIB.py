_E='zxDslIpStaticDestIpAddr'
_D='ZTE-DSL-Route-MIB'
_C='DisplayString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adslLineAlarmConfProfileEntry,adslLineConfProfileEntry,adslLineConfProfileName=mibBuilder.importSymbols('ADSL-LINE-MIB','adslLineAlarmConfProfileEntry','adslLineConfProfileEntry','adslLineConfProfileName')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxDsl,=mibBuilder.importSymbols('ZTE-DSL-MIB','zxDsl')
zxDslRouteMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,11))
_ZxDslIpStaticRouteTable_Object=MibTable
zxDslIpStaticRouteTable=_ZxDslIpStaticRouteTable_Object((1,3,6,1,4,1,3902,1004,11,1))
if mibBuilder.loadTexts:zxDslIpStaticRouteTable.setStatus(_A)
_ZxDslIpStaticRouteEntry_Object=MibTableRow
zxDslIpStaticRouteEntry=_ZxDslIpStaticRouteEntry_Object((1,3,6,1,4,1,3902,1004,11,1,1))
zxDslIpStaticRouteEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxDslIpStaticRouteEntry.setStatus(_A)
_ZxDslIpStaticDestIpAddr_Type=IpAddress
_ZxDslIpStaticDestIpAddr_Object=MibTableColumn
zxDslIpStaticDestIpAddr=_ZxDslIpStaticDestIpAddr_Object((1,3,6,1,4,1,3902,1004,11,1,1,1),_ZxDslIpStaticDestIpAddr_Type())
zxDslIpStaticDestIpAddr.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxDslIpStaticDestIpAddr.setStatus(_A)
_ZxDslIpStaticMask_Type=IpAddress
_ZxDslIpStaticMask_Object=MibTableColumn
zxDslIpStaticMask=_ZxDslIpStaticMask_Object((1,3,6,1,4,1,3902,1004,11,1,1,2),_ZxDslIpStaticMask_Type())
zxDslIpStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpStaticMask.setStatus(_A)
_ZxDslIpStaticNextHop_Type=IpAddress
_ZxDslIpStaticNextHop_Object=MibTableColumn
zxDslIpStaticNextHop=_ZxDslIpStaticNextHop_Object((1,3,6,1,4,1,3902,1004,11,1,1,3),_ZxDslIpStaticNextHop_Type())
zxDslIpStaticNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpStaticNextHop.setStatus(_A)
class _ZxDslIpStaticName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxDslIpStaticName_Type.__name__=_C
_ZxDslIpStaticName_Object=MibTableColumn
zxDslIpStaticName=_ZxDslIpStaticName_Object((1,3,6,1,4,1,3902,1004,11,1,1,4),_ZxDslIpStaticName_Type())
zxDslIpStaticName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpStaticName.setStatus(_A)
_ZxDslIpStaticUseHw_Type=TruthValue
_ZxDslIpStaticUseHw_Object=MibTableColumn
zxDslIpStaticUseHw=_ZxDslIpStaticUseHw_Object((1,3,6,1,4,1,3902,1004,11,1,1,5),_ZxDslIpStaticUseHw_Type())
zxDslIpStaticUseHw.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpStaticUseHw.setStatus(_A)
_ZxDslIpStaticInHw_Type=TruthValue
_ZxDslIpStaticInHw_Object=MibTableColumn
zxDslIpStaticInHw=_ZxDslIpStaticInHw_Object((1,3,6,1,4,1,3902,1004,11,1,1,6),_ZxDslIpStaticInHw_Type())
zxDslIpStaticInHw.setMaxAccess('read-only')
if mibBuilder.loadTexts:zxDslIpStaticInHw.setStatus(_A)
_ZxDslIpStaticRowStatus_Type=RowStatus
_ZxDslIpStaticRowStatus_Object=MibTableColumn
zxDslIpStaticRowStatus=_ZxDslIpStaticRowStatus_Object((1,3,6,1,4,1,3902,1004,11,1,1,7),_ZxDslIpStaticRowStatus_Type())
zxDslIpStaticRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslIpStaticRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zxDslRouteMib':zxDslRouteMib,'zxDslIpStaticRouteTable':zxDslIpStaticRouteTable,'zxDslIpStaticRouteEntry':zxDslIpStaticRouteEntry,_E:zxDslIpStaticDestIpAddr,'zxDslIpStaticMask':zxDslIpStaticMask,'zxDslIpStaticNextHop':zxDslIpStaticNextHop,'zxDslIpStaticName':zxDslIpStaticName,'zxDslIpStaticUseHw':zxDslIpStaticUseHw,'zxDslIpStaticInHw':zxDslIpStaticInHw,'zxDslIpStaticRowStatus':zxDslIpStaticRowStatus})