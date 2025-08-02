_F='zxDslLineTestServerIndex'
_E='ZTE-DSL-LINE-TEST-MIB'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zxDsl,=mibBuilder.importSymbols('ZTE-DSL-MIB','zxDsl')
zxDslLineTestMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,29))
_ZxDslLineTestMibObjects_ObjectIdentity=ObjectIdentity
zxDslLineTestMibObjects=_ZxDslLineTestMibObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,29,1))
class _ZxDslLineTestUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tam',1),('ltc',2)))
_ZxDslLineTestUnitType_Type.__name__=_B
_ZxDslLineTestUnitType_Object=MibScalar
zxDslLineTestUnitType=_ZxDslLineTestUnitType_Object((1,3,6,1,4,1,3902,1004,29,1,5),_ZxDslLineTestUnitType_Type())
zxDslLineTestUnitType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslLineTestUnitType.setStatus(_A)
_ZxDslLineTestTam_ObjectIdentity=ObjectIdentity
zxDslLineTestTam=_ZxDslLineTestTam_ObjectIdentity((1,3,6,1,4,1,3902,1004,29,1,10))
_ZxDslLineTestTamIp_Type=IpAddress
_ZxDslLineTestTamIp_Object=MibScalar
zxDslLineTestTamIp=_ZxDslLineTestTamIp_Object((1,3,6,1,4,1,3902,1004,29,1,10,1),_ZxDslLineTestTamIp_Type())
zxDslLineTestTamIp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslLineTestTamIp.setStatus(_A)
_ZxDslLineTestTamIpMask_Type=IpAddress
_ZxDslLineTestTamIpMask_Object=MibScalar
zxDslLineTestTamIpMask=_ZxDslLineTestTamIpMask_Object((1,3,6,1,4,1,3902,1004,29,1,10,2),_ZxDslLineTestTamIpMask_Type())
zxDslLineTestTamIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslLineTestTamIpMask.setStatus(_A)
_ZxDslLineTestServerTable_Object=MibTable
zxDslLineTestServerTable=_ZxDslLineTestServerTable_Object((1,3,6,1,4,1,3902,1004,29,1,50))
if mibBuilder.loadTexts:zxDslLineTestServerTable.setStatus(_A)
_ZxDslLineTestServerEntry_Object=MibTableRow
zxDslLineTestServerEntry=_ZxDslLineTestServerEntry_Object((1,3,6,1,4,1,3902,1004,29,1,50,1))
zxDslLineTestServerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxDslLineTestServerEntry.setStatus(_A)
class _ZxDslLineTestServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_ZxDslLineTestServerIndex_Type.__name__=_B
_ZxDslLineTestServerIndex_Object=MibTableColumn
zxDslLineTestServerIndex=_ZxDslLineTestServerIndex_Object((1,3,6,1,4,1,3902,1004,29,1,50,1,1),_ZxDslLineTestServerIndex_Type())
zxDslLineTestServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxDslLineTestServerIndex.setStatus(_A)
_ZxDslLineTestServerIp_Type=IpAddress
_ZxDslLineTestServerIp_Object=MibTableColumn
zxDslLineTestServerIp=_ZxDslLineTestServerIp_Object((1,3,6,1,4,1,3902,1004,29,1,50,1,2),_ZxDslLineTestServerIp_Type())
zxDslLineTestServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslLineTestServerIp.setStatus(_A)
class _ZxDslLineTestServerNatMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noNAT',1),('inBandNAT',2),('outBandNAT',3),('bridging_in_out_band',4)))
_ZxDslLineTestServerNatMode_Type.__name__=_B
_ZxDslLineTestServerNatMode_Object=MibTableColumn
zxDslLineTestServerNatMode=_ZxDslLineTestServerNatMode_Object((1,3,6,1,4,1,3902,1004,29,1,50,1,3),_ZxDslLineTestServerNatMode_Type())
zxDslLineTestServerNatMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslLineTestServerNatMode.setStatus(_A)
_ZxDslLineTestServerRowStatus_Type=RowStatus
_ZxDslLineTestServerRowStatus_Object=MibTableColumn
zxDslLineTestServerRowStatus=_ZxDslLineTestServerRowStatus_Object((1,3,6,1,4,1,3902,1004,29,1,50,1,4),_ZxDslLineTestServerRowStatus_Type())
zxDslLineTestServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslLineTestServerRowStatus.setStatus(_A)
_ZxDslLineTestTrapObjects_ObjectIdentity=ObjectIdentity
zxDslLineTestTrapObjects=_ZxDslLineTestTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,29,2))
mibBuilder.exportSymbols(_E,**{'zxDslLineTestMib':zxDslLineTestMib,'zxDslLineTestMibObjects':zxDslLineTestMibObjects,'zxDslLineTestUnitType':zxDslLineTestUnitType,'zxDslLineTestTam':zxDslLineTestTam,'zxDslLineTestTamIp':zxDslLineTestTamIp,'zxDslLineTestTamIpMask':zxDslLineTestTamIpMask,'zxDslLineTestServerTable':zxDslLineTestServerTable,'zxDslLineTestServerEntry':zxDslLineTestServerEntry,_F:zxDslLineTestServerIndex,'zxDslLineTestServerIp':zxDslLineTestServerIp,'zxDslLineTestServerNatMode':zxDslLineTestServerNatMode,'zxDslLineTestServerRowStatus':zxDslLineTestServerRowStatus,'zxDslLineTestTrapObjects':zxDslLineTestTrapObjects})