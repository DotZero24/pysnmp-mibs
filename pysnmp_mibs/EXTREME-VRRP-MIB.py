_I='extremeVrrpOperGroup'
_H='extremeVrrpFabricRoutingMode'
_G='vrrpOperVrId'
_F='VRRP-MIB'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='EXTREME-VRRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
vrrpOperVrId,=mibBuilder.importSymbols(_F,_G)
extremeVrrpMIB=ModuleIdentity((1,3,6,1,4,1,1916,1,49))
if mibBuilder.loadTexts:extremeVrrpMIB.setRevisions(('2016-01-04 00:00',))
_ExtremeVrrpOperations_ObjectIdentity=ObjectIdentity
extremeVrrpOperations=_ExtremeVrrpOperations_ObjectIdentity((1,3,6,1,4,1,1916,1,49,1))
_ExtremeVrrpOperTable_Object=MibTable
extremeVrrpOperTable=_ExtremeVrrpOperTable_Object((1,3,6,1,4,1,1916,1,49,1,1))
if mibBuilder.loadTexts:extremeVrrpOperTable.setStatus(_A)
_ExtremeVrrpOperEntry_Object=MibTableRow
extremeVrrpOperEntry=_ExtremeVrrpOperEntry_Object((1,3,6,1,4,1,1916,1,49,1,1,1))
extremeVrrpOperEntry.setIndexNames((0,_C,_D),(0,_F,_G))
if mibBuilder.loadTexts:extremeVrrpOperEntry.setStatus(_A)
class _ExtremeVrrpFabricRoutingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ExtremeVrrpFabricRoutingMode_Type.__name__=_E
_ExtremeVrrpFabricRoutingMode_Object=MibTableColumn
extremeVrrpFabricRoutingMode=_ExtremeVrrpFabricRoutingMode_Object((1,3,6,1,4,1,1916,1,49,1,1,1,1),_ExtremeVrrpFabricRoutingMode_Type())
extremeVrrpFabricRoutingMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:extremeVrrpFabricRoutingMode.setStatus(_A)
_ExtremeVrrpConformance_ObjectIdentity=ObjectIdentity
extremeVrrpConformance=_ExtremeVrrpConformance_ObjectIdentity((1,3,6,1,4,1,1916,1,49,2))
_ExtremeVrrpMIBCompliances_ObjectIdentity=ObjectIdentity
extremeVrrpMIBCompliances=_ExtremeVrrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1916,1,49,2,1))
_ExtremeVrrpMIBGroups_ObjectIdentity=ObjectIdentity
extremeVrrpMIBGroups=_ExtremeVrrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,1916,1,49,2,2))
extremeVrrpOperGroup=ObjectGroup((1,3,6,1,4,1,1916,1,49,2,2,1))
extremeVrrpOperGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:extremeVrrpOperGroup.setStatus(_A)
extremeVrrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1916,1,49,2,1,1))
extremeVrrpMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:extremeVrrpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'extremeVrrpMIB':extremeVrrpMIB,'extremeVrrpOperations':extremeVrrpOperations,'extremeVrrpOperTable':extremeVrrpOperTable,'extremeVrrpOperEntry':extremeVrrpOperEntry,_H:extremeVrrpFabricRoutingMode,'extremeVrrpConformance':extremeVrrpConformance,'extremeVrrpMIBCompliances':extremeVrrpMIBCompliances,'extremeVrrpMIBCompliance':extremeVrrpMIBCompliance,'extremeVrrpMIBGroups':extremeVrrpMIBGroups,_I:extremeVrrpOperGroup})