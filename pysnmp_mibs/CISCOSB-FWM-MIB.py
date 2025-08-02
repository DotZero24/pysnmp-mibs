_H='read-write'
_G='rlFwmIndex'
_F='rlFwmEntity'
_E='rlFwmUnitIndex'
_D='read-only'
_C='not-accessible'
_B='CISCOSB-FWM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rlFwm=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,244))
if mibBuilder.loadTexts:rlFwm.setRevisions(('2006-02-12 00:00','2003-10-18 00:00'))
class EntityType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('not-relevant',0),('cpld',1),('fpga',2)))
_RlFwmTable_Object=MibTable
rlFwmTable=_RlFwmTable_Object((1,3,6,1,4,1,9,6,1,101,244,1))
if mibBuilder.loadTexts:rlFwmTable.setStatus(_A)
_RlFwmEntry_Object=MibTableRow
rlFwmEntry=_RlFwmEntry_Object((1,3,6,1,4,1,9,6,1,101,244,1,1))
rlFwmEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:rlFwmEntry.setStatus(_A)
_RlFwmUnitIndex_Type=Integer32
_RlFwmUnitIndex_Object=MibTableColumn
rlFwmUnitIndex=_RlFwmUnitIndex_Object((1,3,6,1,4,1,9,6,1,101,244,1,1,1),_RlFwmUnitIndex_Type())
rlFwmUnitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFwmUnitIndex.setStatus(_A)
_RlFwmEntity_Type=EntityType
_RlFwmEntity_Object=MibTableColumn
rlFwmEntity=_RlFwmEntity_Object((1,3,6,1,4,1,9,6,1,101,244,1,1,2),_RlFwmEntity_Type())
rlFwmEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFwmEntity.setStatus(_A)
_RlFwmIndex_Type=Integer32
_RlFwmIndex_Object=MibTableColumn
rlFwmIndex=_RlFwmIndex_Object((1,3,6,1,4,1,9,6,1,101,244,1,1,3),_RlFwmIndex_Type())
rlFwmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlFwmIndex.setStatus(_A)
_RlFwmVersionActive_Type=DisplayString
_RlFwmVersionActive_Object=MibTableColumn
rlFwmVersionActive=_RlFwmVersionActive_Object((1,3,6,1,4,1,9,6,1,101,244,1,1,4),_RlFwmVersionActive_Type())
rlFwmVersionActive.setMaxAccess(_D)
if mibBuilder.loadTexts:rlFwmVersionActive.setStatus(_A)
_RlFwmVersionInactive_Type=DisplayString
_RlFwmVersionInactive_Object=MibTableColumn
rlFwmVersionInactive=_RlFwmVersionInactive_Object((1,3,6,1,4,1,9,6,1,101,244,1,1,5),_RlFwmVersionInactive_Type())
rlFwmVersionInactive.setMaxAccess(_D)
if mibBuilder.loadTexts:rlFwmVersionInactive.setStatus(_A)
_RlFwmUpdateAvailable_Type=TruthValue
_RlFwmUpdateAvailable_Object=MibTableColumn
rlFwmUpdateAvailable=_RlFwmUpdateAvailable_Object((1,3,6,1,4,1,9,6,1,101,244,1,1,6),_RlFwmUpdateAvailable_Type())
rlFwmUpdateAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:rlFwmUpdateAvailable.setStatus(_A)
_RlFwmForceAutoUpdate_Type=TruthValue
_RlFwmForceAutoUpdate_Object=MibTableColumn
rlFwmForceAutoUpdate=_RlFwmForceAutoUpdate_Object((1,3,6,1,4,1,9,6,1,101,244,1,1,7),_RlFwmForceAutoUpdate_Type())
rlFwmForceAutoUpdate.setMaxAccess(_H)
if mibBuilder.loadTexts:rlFwmForceAutoUpdate.setStatus(_A)
_RlFwmVersionUpdate_Type=EntityType
_RlFwmVersionUpdate_Object=MibScalar
rlFwmVersionUpdate=_RlFwmVersionUpdate_Object((1,3,6,1,4,1,9,6,1,101,244,2),_RlFwmVersionUpdate_Type())
rlFwmVersionUpdate.setMaxAccess(_H)
if mibBuilder.loadTexts:rlFwmVersionUpdate.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EntityType':EntityType,'rlFwm':rlFwm,'rlFwmTable':rlFwmTable,'rlFwmEntry':rlFwmEntry,_E:rlFwmUnitIndex,_F:rlFwmEntity,_G:rlFwmIndex,'rlFwmVersionActive':rlFwmVersionActive,'rlFwmVersionInactive':rlFwmVersionInactive,'rlFwmUpdateAvailable':rlFwmUpdateAvailable,'rlFwmForceAutoUpdate':rlFwmForceAutoUpdate,'rlFwmVersionUpdate':rlFwmVersionUpdate})