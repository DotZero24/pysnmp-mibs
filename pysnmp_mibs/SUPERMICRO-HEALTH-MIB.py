_O='smHealthMonitorGroup'
_N='smHealthMonitorMonitor'
_M='smHealthMonitorMinReading'
_L='smHealthMonitorMaxReading'
_K='smHealthMonitorLowLimit'
_J='smHealthMonitorHighLimit'
_I='smHealthMonitorReading'
_H='smHealthMonitorName'
_G='smHealthMonitorType'
_F='smHealthMonitorIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='SUPERMICRO-HEALTH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
smHealth,=mibBuilder.importSymbols('SUPERMICRO-SMI','smHealth')
smHealthMIB=ModuleIdentity((1,3,6,1,4,1,10876,2,1))
class SMHealthInfoTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_SmHealthObjects_ObjectIdentity=ObjectIdentity
smHealthObjects=_SmHealthObjects_ObjectIdentity((1,3,6,1,4,1,10876,2,1,1))
_SmHealthMonitorTable_Object=MibTable
smHealthMonitorTable=_SmHealthMonitorTable_Object((1,3,6,1,4,1,10876,2,1,1,1))
if mibBuilder.loadTexts:smHealthMonitorTable.setStatus(_A)
_SmHealthMonitorEntry_Object=MibTableRow
smHealthMonitorEntry=_SmHealthMonitorEntry_Object((1,3,6,1,4,1,10876,2,1,1,1,1))
smHealthMonitorEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:smHealthMonitorEntry.setStatus(_A)
class _SmHealthMonitorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SmHealthMonitorIndex_Type.__name__=_D
_SmHealthMonitorIndex_Object=MibTableColumn
smHealthMonitorIndex=_SmHealthMonitorIndex_Object((1,3,6,1,4,1,10876,2,1,1,1,1,1),_SmHealthMonitorIndex_Type())
smHealthMonitorIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:smHealthMonitorIndex.setStatus(_A)
_SmHealthMonitorName_Type=DisplayString
_SmHealthMonitorName_Object=MibTableColumn
smHealthMonitorName=_SmHealthMonitorName_Object((1,3,6,1,4,1,10876,2,1,1,1,1,2),_SmHealthMonitorName_Type())
smHealthMonitorName.setMaxAccess(_C)
if mibBuilder.loadTexts:smHealthMonitorName.setStatus(_A)
_SmHealthMonitorType_Type=SMHealthInfoTypes
_SmHealthMonitorType_Object=MibTableColumn
smHealthMonitorType=_SmHealthMonitorType_Object((1,3,6,1,4,1,10876,2,1,1,1,1,3),_SmHealthMonitorType_Type())
smHealthMonitorType.setMaxAccess(_C)
if mibBuilder.loadTexts:smHealthMonitorType.setStatus(_A)
class _SmHealthMonitorReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SmHealthMonitorReading_Type.__name__=_D
_SmHealthMonitorReading_Object=MibTableColumn
smHealthMonitorReading=_SmHealthMonitorReading_Object((1,3,6,1,4,1,10876,2,1,1,1,1,4),_SmHealthMonitorReading_Type())
smHealthMonitorReading.setMaxAccess(_C)
if mibBuilder.loadTexts:smHealthMonitorReading.setStatus(_A)
class _SmHealthMonitorHighLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SmHealthMonitorHighLimit_Type.__name__=_D
_SmHealthMonitorHighLimit_Object=MibTableColumn
smHealthMonitorHighLimit=_SmHealthMonitorHighLimit_Object((1,3,6,1,4,1,10876,2,1,1,1,1,5),_SmHealthMonitorHighLimit_Type())
smHealthMonitorHighLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:smHealthMonitorHighLimit.setStatus(_A)
class _SmHealthMonitorLowLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SmHealthMonitorLowLimit_Type.__name__=_D
_SmHealthMonitorLowLimit_Object=MibTableColumn
smHealthMonitorLowLimit=_SmHealthMonitorLowLimit_Object((1,3,6,1,4,1,10876,2,1,1,1,1,6),_SmHealthMonitorLowLimit_Type())
smHealthMonitorLowLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:smHealthMonitorLowLimit.setStatus(_A)
class _SmHealthMonitorMaxReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SmHealthMonitorMaxReading_Type.__name__=_D
_SmHealthMonitorMaxReading_Object=MibTableColumn
smHealthMonitorMaxReading=_SmHealthMonitorMaxReading_Object((1,3,6,1,4,1,10876,2,1,1,1,1,7),_SmHealthMonitorMaxReading_Type())
smHealthMonitorMaxReading.setMaxAccess(_C)
if mibBuilder.loadTexts:smHealthMonitorMaxReading.setStatus(_A)
class _SmHealthMonitorMinReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SmHealthMonitorMinReading_Type.__name__=_D
_SmHealthMonitorMinReading_Object=MibTableColumn
smHealthMonitorMinReading=_SmHealthMonitorMinReading_Object((1,3,6,1,4,1,10876,2,1,1,1,1,8),_SmHealthMonitorMinReading_Type())
smHealthMonitorMinReading.setMaxAccess(_C)
if mibBuilder.loadTexts:smHealthMonitorMinReading.setStatus(_A)
_SmHealthMonitorDivisor_Type=Integer32
_SmHealthMonitorDivisor_Object=MibTableColumn
smHealthMonitorDivisor=_SmHealthMonitorDivisor_Object((1,3,6,1,4,1,10876,2,1,1,1,1,9),_SmHealthMonitorDivisor_Type())
smHealthMonitorDivisor.setMaxAccess(_E)
if mibBuilder.loadTexts:smHealthMonitorDivisor.setStatus(_A)
_SmHealthMonitorMonitor_Type=TruthValue
_SmHealthMonitorMonitor_Object=MibTableColumn
smHealthMonitorMonitor=_SmHealthMonitorMonitor_Object((1,3,6,1,4,1,10876,2,1,1,1,1,10),_SmHealthMonitorMonitor_Type())
smHealthMonitorMonitor.setMaxAccess(_E)
if mibBuilder.loadTexts:smHealthMonitorMonitor.setStatus(_A)
_SmHealthMonitorReadingUnit_Type=DisplayString
_SmHealthMonitorReadingUnit_Object=MibTableColumn
smHealthMonitorReadingUnit=_SmHealthMonitorReadingUnit_Object((1,3,6,1,4,1,10876,2,1,1,1,1,11),_SmHealthMonitorReadingUnit_Type())
smHealthMonitorReadingUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:smHealthMonitorReadingUnit.setStatus(_A)
_SmHealthMonitorStatus_Type=Integer32
_SmHealthMonitorStatus_Object=MibTableColumn
smHealthMonitorStatus=_SmHealthMonitorStatus_Object((1,3,6,1,4,1,10876,2,1,1,1,1,12),_SmHealthMonitorStatus_Type())
smHealthMonitorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:smHealthMonitorStatus.setStatus(_A)
_SmHealthNotifications_ObjectIdentity=ObjectIdentity
smHealthNotifications=_SmHealthNotifications_ObjectIdentity((1,3,6,1,4,1,10876,2,1,2))
_SmHealthConformance_ObjectIdentity=ObjectIdentity
smHealthConformance=_SmHealthConformance_ObjectIdentity((1,3,6,1,4,1,10876,2,1,3))
_SmHealthCompliances_ObjectIdentity=ObjectIdentity
smHealthCompliances=_SmHealthCompliances_ObjectIdentity((1,3,6,1,4,1,10876,2,1,3,1))
_SmHealthGroups_ObjectIdentity=ObjectIdentity
smHealthGroups=_SmHealthGroups_ObjectIdentity((1,3,6,1,4,1,10876,2,1,3,2))
_SmHealthAllinoneStatus_Type=Integer32
_SmHealthAllinoneStatus_Object=MibScalar
smHealthAllinoneStatus=_SmHealthAllinoneStatus_Object((1,3,6,1,4,1,10876,2,2),_SmHealthAllinoneStatus_Type())
smHealthAllinoneStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:smHealthAllinoneStatus.setStatus(_A)
_SmHealthAllinoneMsg_Type=DisplayString
_SmHealthAllinoneMsg_Object=MibScalar
smHealthAllinoneMsg=_SmHealthAllinoneMsg_Object((1,3,6,1,4,1,10876,2,3),_SmHealthAllinoneMsg_Type())
smHealthAllinoneMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:smHealthAllinoneMsg.setStatus(_A)
smHealthMonitorGroup=ObjectGroup((1,3,6,1,4,1,10876,2,1,3,2,1))
smHealthMonitorGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:smHealthMonitorGroup.setStatus(_A)
smHealthCompliance=ModuleCompliance((1,3,6,1,4,1,10876,2,1,3,1,1))
smHealthCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:smHealthCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SMHealthInfoTypes':SMHealthInfoTypes,'smHealthMIB':smHealthMIB,'smHealthObjects':smHealthObjects,'smHealthMonitorTable':smHealthMonitorTable,'smHealthMonitorEntry':smHealthMonitorEntry,_F:smHealthMonitorIndex,_H:smHealthMonitorName,_G:smHealthMonitorType,_I:smHealthMonitorReading,_J:smHealthMonitorHighLimit,_K:smHealthMonitorLowLimit,_L:smHealthMonitorMaxReading,_M:smHealthMonitorMinReading,'smHealthMonitorDivisor':smHealthMonitorDivisor,_N:smHealthMonitorMonitor,'smHealthMonitorReadingUnit':smHealthMonitorReadingUnit,'smHealthMonitorStatus':smHealthMonitorStatus,'smHealthNotifications':smHealthNotifications,'smHealthConformance':smHealthConformance,'smHealthCompliances':smHealthCompliances,'smHealthCompliance':smHealthCompliance,'smHealthGroups':smHealthGroups,_O:smHealthMonitorGroup,'smHealthAllinoneStatus':smHealthAllinoneStatus,'smHealthAllinoneMsg':smHealthAllinoneMsg})