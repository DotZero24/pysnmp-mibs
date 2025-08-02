_L='oldpSchGroup'
_K='monitoringMode'
_J='timDetMode'
_I='expectedDAPI'
_H='expectedSAPI'
_G='recievedTTI'
_F='transmitTTI'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='INFINERA-TP-OLDPSCH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnMonitoringMode,InfnTimReptMode=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnMonitoringMode','InfnTimReptMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oldpSchMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,58))
if mibBuilder.loadTexts:oldpSchMIB.setRevisions(('2016-08-29 00:00',))
_OldpSchTable_Object=MibTable
oldpSchTable=_OldpSchTable_Object((1,3,6,1,4,1,21296,2,2,2,2,58,1))
if mibBuilder.loadTexts:oldpSchTable.setStatus(_A)
_OldpSchEntry_Object=MibTableRow
oldpSchEntry=_OldpSchEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,58,1,1))
oldpSchEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oldpSchEntry.setStatus(_A)
_TransmitTTI_Type=DisplayString
_TransmitTTI_Object=MibTableColumn
transmitTTI=_TransmitTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,58,1,1,1),_TransmitTTI_Type())
transmitTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:transmitTTI.setStatus(_A)
_RecievedTTI_Type=DisplayString
_RecievedTTI_Object=MibTableColumn
recievedTTI=_RecievedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,58,1,1,2),_RecievedTTI_Type())
recievedTTI.setMaxAccess('read-only')
if mibBuilder.loadTexts:recievedTTI.setStatus(_A)
_ExpectedSAPI_Type=DisplayString
_ExpectedSAPI_Object=MibTableColumn
expectedSAPI=_ExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,58,1,1,3),_ExpectedSAPI_Type())
expectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:expectedSAPI.setStatus(_A)
_ExpectedDAPI_Type=DisplayString
_ExpectedDAPI_Object=MibTableColumn
expectedDAPI=_ExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,58,1,1,4),_ExpectedDAPI_Type())
expectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:expectedDAPI.setStatus(_A)
_TimDetMode_Type=InfnTimReptMode
_TimDetMode_Object=MibTableColumn
timDetMode=_TimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,58,1,1,5),_TimDetMode_Type())
timDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:timDetMode.setStatus(_A)
_MonitoringMode_Type=InfnMonitoringMode
_MonitoringMode_Object=MibTableColumn
monitoringMode=_MonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,58,1,1,6),_MonitoringMode_Type())
monitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:monitoringMode.setStatus(_A)
_OldpSchConformance_ObjectIdentity=ObjectIdentity
oldpSchConformance=_OldpSchConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,58,3))
_OldpSchCompliances_ObjectIdentity=ObjectIdentity
oldpSchCompliances=_OldpSchCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,58,3,1))
_OldpSchGroups_ObjectIdentity=ObjectIdentity
oldpSchGroups=_OldpSchGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,58,3,2))
oldpSchGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,58,3,2,1))
oldpSchGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:oldpSchGroup.setStatus(_A)
oldpSchCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,58,3,1,1))
oldpSchCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:oldpSchCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oldpSchMIB':oldpSchMIB,'oldpSchTable':oldpSchTable,'oldpSchEntry':oldpSchEntry,_F:transmitTTI,_G:recievedTTI,_H:expectedSAPI,_I:expectedDAPI,_J:timDetMode,_K:monitoringMode,'oldpSchConformance':oldpSchConformance,'oldpSchCompliances':oldpSchCompliances,'oldpSchCompliance':oldpSchCompliance,'oldpSchGroups':oldpSchGroups,_L:oldpSchGroup})