_L='oacPingGroup'
_K='oacPingResultsAverageJitter'
_J='oacPingResultsMaxJitter'
_I='oacPingResultsMinJitter'
_H='oacPingJitterSamples'
_G='pingCtlTestName'
_F='pingCtlOwnerIndex'
_E='microseconds'
_D='DISMAN-PING-MIB'
_C='read-only'
_B='ONEACCESS-PING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pingCtlOwnerIndex,pingCtlTestName=mibBuilder.importSymbols(_D,_F,_G)
oacExpIMPing,oacMIBModules,oneAccess=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMPing','oacMIBModules','oneAccess')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oacPingMIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,6601))
if mibBuilder.loadTexts:oacPingMIBModule.setRevisions(('2011-06-15 00:00','2010-07-08 00:01'))
_OacPingNotifications_ObjectIdentity=ObjectIdentity
oacPingNotifications=_OacPingNotifications_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,3,0))
_OacPingObjects_ObjectIdentity=ObjectIdentity
oacPingObjects=_OacPingObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,3,1))
_OacPingResultsTable_Object=MibTable
oacPingResultsTable=_OacPingResultsTable_Object((1,3,6,1,4,1,13191,10,3,4,3,1,3))
if mibBuilder.loadTexts:oacPingResultsTable.setStatus(_A)
_OacPingResultsEntry_Object=MibTableRow
oacPingResultsEntry=_OacPingResultsEntry_Object((1,3,6,1,4,1,13191,10,3,4,3,1,3,1))
oacPingResultsEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:oacPingResultsEntry.setStatus(_A)
_OacPingJitterSamples_Type=Unsigned32
_OacPingJitterSamples_Object=MibTableColumn
oacPingJitterSamples=_OacPingJitterSamples_Object((1,3,6,1,4,1,13191,10,3,4,3,1,3,1,1),_OacPingJitterSamples_Type())
oacPingJitterSamples.setMaxAccess(_C)
if mibBuilder.loadTexts:oacPingJitterSamples.setStatus(_A)
_OacPingResultsMinJitter_Type=Unsigned32
_OacPingResultsMinJitter_Object=MibTableColumn
oacPingResultsMinJitter=_OacPingResultsMinJitter_Object((1,3,6,1,4,1,13191,10,3,4,3,1,3,1,2),_OacPingResultsMinJitter_Type())
oacPingResultsMinJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacPingResultsMinJitter.setStatus(_A)
if mibBuilder.loadTexts:oacPingResultsMinJitter.setUnits(_E)
_OacPingResultsMaxJitter_Type=Unsigned32
_OacPingResultsMaxJitter_Object=MibTableColumn
oacPingResultsMaxJitter=_OacPingResultsMaxJitter_Object((1,3,6,1,4,1,13191,10,3,4,3,1,3,1,3),_OacPingResultsMaxJitter_Type())
oacPingResultsMaxJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacPingResultsMaxJitter.setStatus(_A)
if mibBuilder.loadTexts:oacPingResultsMaxJitter.setUnits(_E)
_OacPingResultsAverageJitter_Type=Unsigned32
_OacPingResultsAverageJitter_Object=MibTableColumn
oacPingResultsAverageJitter=_OacPingResultsAverageJitter_Object((1,3,6,1,4,1,13191,10,3,4,3,1,3,1,4),_OacPingResultsAverageJitter_Type())
oacPingResultsAverageJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacPingResultsAverageJitter.setStatus(_A)
if mibBuilder.loadTexts:oacPingResultsAverageJitter.setUnits(_E)
_OacPingConformance_ObjectIdentity=ObjectIdentity
oacPingConformance=_OacPingConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,3,2))
_OacPingCompliances_ObjectIdentity=ObjectIdentity
oacPingCompliances=_OacPingCompliances_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,3,2,1))
_OacPingGroups_ObjectIdentity=ObjectIdentity
oacPingGroups=_OacPingGroups_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,3,2,2))
oacPingGroup=ObjectGroup((1,3,6,1,4,1,13191,10,3,4,3,2,2,1))
oacPingGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:oacPingGroup.setStatus(_A)
oacPingCompliance=ModuleCompliance((1,3,6,1,4,1,13191,10,3,4,3,2,1,1))
oacPingCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:oacPingCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oacPingMIBModule':oacPingMIBModule,'oacPingNotifications':oacPingNotifications,'oacPingObjects':oacPingObjects,'oacPingResultsTable':oacPingResultsTable,'oacPingResultsEntry':oacPingResultsEntry,_H:oacPingJitterSamples,_I:oacPingResultsMinJitter,_J:oacPingResultsMaxJitter,_K:oacPingResultsAverageJitter,'oacPingConformance':oacPingConformance,'oacPingCompliances':oacPingCompliances,'oacPingCompliance':oacPingCompliance,'oacPingGroups':oacPingGroups,_L:oacPingGroup})