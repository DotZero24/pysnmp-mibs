_E='Integer32'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
extremeEntity=ModuleIdentity((1,3,6,1,4,1,1916,1,31))
_ExtremeEntityFRUTable_Object=MibTable
extremeEntityFRUTable=_ExtremeEntityFRUTable_Object((1,3,6,1,4,1,1916,1,31,1))
if mibBuilder.loadTexts:extremeEntityFRUTable.setStatus(_A)
_ExtremeEntityFRUEntry_Object=MibTableRow
extremeEntityFRUEntry=_ExtremeEntityFRUEntry_Object((1,3,6,1,4,1,1916,1,31,1,1))
extremeEntityFRUEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:extremeEntityFRUEntry.setStatus(_A)
_ExtremeEntityFRUStartTime_Type=Unsigned32
_ExtremeEntityFRUStartTime_Object=MibTableColumn
extremeEntityFRUStartTime=_ExtremeEntityFRUStartTime_Object((1,3,6,1,4,1,1916,1,31,1,1,1),_ExtremeEntityFRUStartTime_Type())
extremeEntityFRUStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEntityFRUStartTime.setStatus(_A)
_ExtremeEntityFRUOdometer_Type=Unsigned32
_ExtremeEntityFRUOdometer_Object=MibTableColumn
extremeEntityFRUOdometer=_ExtremeEntityFRUOdometer_Object((1,3,6,1,4,1,1916,1,31,1,1,2),_ExtremeEntityFRUOdometer_Type())
extremeEntityFRUOdometer.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEntityFRUOdometer.setStatus(_A)
class _ExtremeEntityFRUOdometerUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('days',1),('seconds',2)))
_ExtremeEntityFRUOdometerUnit_Type.__name__=_E
_ExtremeEntityFRUOdometerUnit_Object=MibTableColumn
extremeEntityFRUOdometerUnit=_ExtremeEntityFRUOdometerUnit_Object((1,3,6,1,4,1,1916,1,31,1,1,3),_ExtremeEntityFRUOdometerUnit_Type())
extremeEntityFRUOdometerUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEntityFRUOdometerUnit.setStatus(_A)
mibBuilder.exportSymbols('EXTREME-ENTITY-MIB',**{'extremeEntity':extremeEntity,'extremeEntityFRUTable':extremeEntityFRUTable,'extremeEntityFRUEntry':extremeEntityFRUEntry,'extremeEntityFRUStartTime':extremeEntityFRUStartTime,'extremeEntityFRUOdometer':extremeEntityFRUOdometer,'extremeEntityFRUOdometerUnit':extremeEntityFRUOdometerUnit})