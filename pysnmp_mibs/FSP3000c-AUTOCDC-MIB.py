_K='fsp3000cAutoCDCObjectGroup'
_J='autoCdcStatusTodcValue'
_I='autoCdcStatusTodcValueSet'
_H='autoCdcStatusResultType'
_G='autoCdcStatusPercentComplete'
_F='autoCdcStatusControlType'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='FSP3000c-AUTOCDC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aosCommon,fsp3000c=mibBuilder.importSymbols('ADVA-MIB','aosCommon','fsp3000c')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fsp3000cAutoCDCMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,20,2,1,1))
if mibBuilder.loadTexts:fsp3000cAutoCDCMIB.setRevisions(('2016-09-27 00:00',))
class AutoCdcControlType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('idle',1),('init',2),('measure',3),('validate',4)))
class AutoCdcResultType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',0),('standby',1),('progress',2),('initfail',3),('timeout',4),('rngerr',5),('valerr',6),('success',7)))
_Fsp3000cAutoCDCObjects_ObjectIdentity=ObjectIdentity
fsp3000cAutoCDCObjects=_Fsp3000cAutoCDCObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,20,2,1,1,1))
_AutoCdcStatusTable_Object=MibTable
autoCdcStatusTable=_AutoCdcStatusTable_Object((1,3,6,1,4,1,2544,1,20,2,1,1,1,1))
if mibBuilder.loadTexts:autoCdcStatusTable.setStatus(_A)
_AutoCdcStatusEntry_Object=MibTableRow
autoCdcStatusEntry=_AutoCdcStatusEntry_Object((1,3,6,1,4,1,2544,1,20,2,1,1,1,1,1))
autoCdcStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:autoCdcStatusEntry.setStatus(_A)
_AutoCdcStatusControlType_Type=AutoCdcControlType
_AutoCdcStatusControlType_Object=MibTableColumn
autoCdcStatusControlType=_AutoCdcStatusControlType_Object((1,3,6,1,4,1,2544,1,20,2,1,1,1,1,1,1),_AutoCdcStatusControlType_Type())
autoCdcStatusControlType.setMaxAccess(_C)
if mibBuilder.loadTexts:autoCdcStatusControlType.setStatus(_A)
_AutoCdcStatusPercentComplete_Type=Integer32
_AutoCdcStatusPercentComplete_Object=MibTableColumn
autoCdcStatusPercentComplete=_AutoCdcStatusPercentComplete_Object((1,3,6,1,4,1,2544,1,20,2,1,1,1,1,1,2),_AutoCdcStatusPercentComplete_Type())
autoCdcStatusPercentComplete.setMaxAccess(_C)
if mibBuilder.loadTexts:autoCdcStatusPercentComplete.setStatus(_A)
_AutoCdcStatusResultType_Type=AutoCdcResultType
_AutoCdcStatusResultType_Object=MibTableColumn
autoCdcStatusResultType=_AutoCdcStatusResultType_Object((1,3,6,1,4,1,2544,1,20,2,1,1,1,1,1,3),_AutoCdcStatusResultType_Type())
autoCdcStatusResultType.setMaxAccess(_C)
if mibBuilder.loadTexts:autoCdcStatusResultType.setStatus(_A)
_AutoCdcStatusTodcValueSet_Type=TruthValue
_AutoCdcStatusTodcValueSet_Object=MibTableColumn
autoCdcStatusTodcValueSet=_AutoCdcStatusTodcValueSet_Object((1,3,6,1,4,1,2544,1,20,2,1,1,1,1,1,4),_AutoCdcStatusTodcValueSet_Type())
autoCdcStatusTodcValueSet.setMaxAccess(_C)
if mibBuilder.loadTexts:autoCdcStatusTodcValueSet.setStatus(_A)
_AutoCdcStatusTodcValue_Type=Integer32
_AutoCdcStatusTodcValue_Object=MibTableColumn
autoCdcStatusTodcValue=_AutoCdcStatusTodcValue_Object((1,3,6,1,4,1,2544,1,20,2,1,1,1,1,1,5),_AutoCdcStatusTodcValue_Type())
autoCdcStatusTodcValue.setMaxAccess(_C)
if mibBuilder.loadTexts:autoCdcStatusTodcValue.setStatus(_A)
if mibBuilder.loadTexts:autoCdcStatusTodcValue.setUnits('ps/nm')
_Fsp3000cAutoCDCConformance_ObjectIdentity=ObjectIdentity
fsp3000cAutoCDCConformance=_Fsp3000cAutoCDCConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,20,2,1,1,2))
_Fsp3000cAutoCDCCompliances_ObjectIdentity=ObjectIdentity
fsp3000cAutoCDCCompliances=_Fsp3000cAutoCDCCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,20,2,1,1,2,1))
_Fsp3000cAutoCDCGroups_ObjectIdentity=ObjectIdentity
fsp3000cAutoCDCGroups=_Fsp3000cAutoCDCGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,20,2,1,1,2,2))
fsp3000cAutoCDCObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,20,2,1,1,2,2,1))
fsp3000cAutoCDCObjectGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fsp3000cAutoCDCObjectGroup.setStatus(_A)
fsp3000cAutoCDCCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,20,2,1,1,2,1,1))
fsp3000cAutoCDCCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:fsp3000cAutoCDCCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AutoCdcControlType':AutoCdcControlType,'AutoCdcResultType':AutoCdcResultType,'fsp3000cAutoCDCMIB':fsp3000cAutoCDCMIB,'fsp3000cAutoCDCObjects':fsp3000cAutoCDCObjects,'autoCdcStatusTable':autoCdcStatusTable,'autoCdcStatusEntry':autoCdcStatusEntry,_F:autoCdcStatusControlType,_G:autoCdcStatusPercentComplete,_H:autoCdcStatusResultType,_I:autoCdcStatusTodcValueSet,_J:autoCdcStatusTodcValue,'fsp3000cAutoCDCConformance':fsp3000cAutoCDCConformance,'fsp3000cAutoCDCCompliances':fsp3000cAutoCDCCompliances,'fsp3000cAutoCDCCompliance':fsp3000cAutoCDCCompliance,'fsp3000cAutoCDCGroups':fsp3000cAutoCDCGroups,_K:fsp3000cAutoCDCObjectGroup})