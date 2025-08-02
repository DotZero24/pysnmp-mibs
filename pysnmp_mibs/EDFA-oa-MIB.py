_E='oaEDFAAlarmRangeIndex'
_D='EDFA-oa-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eponeoc=ModuleIdentity((1,3,6,1,4,1,34592))
_IpProduct_ObjectIdentity=ObjectIdentity
ipProduct=_IpProduct_ObjectIdentity((1,3,6,1,4,1,34592,1))
if mibBuilder.loadTexts:ipProduct.setStatus(_A)
_MediaConverter_ObjectIdentity=ObjectIdentity
mediaConverter=_MediaConverter_ObjectIdentity((1,3,6,1,4,1,34592,1,1))
if mibBuilder.loadTexts:mediaConverter.setStatus(_A)
_Edfa_ObjectIdentity=ObjectIdentity
edfa=_Edfa_ObjectIdentity((1,3,6,1,4,1,34592,1,5))
if mibBuilder.loadTexts:edfa.setStatus(_A)
_OaEDFAAlarmRangeTable_Object=MibTable
oaEDFAAlarmRangeTable=_OaEDFAAlarmRangeTable_Object((1,3,6,1,4,1,34592,1,5,1))
if mibBuilder.loadTexts:oaEDFAAlarmRangeTable.setStatus(_A)
_OaEDFAAlarmRangeEntry_Object=MibTableRow
oaEDFAAlarmRangeEntry=_OaEDFAAlarmRangeEntry_Object((1,3,6,1,4,1,34592,1,5,1,1))
oaEDFAAlarmRangeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oaEDFAAlarmRangeEntry.setStatus(_A)
class _OaEDFAAlarmRangeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_OaEDFAAlarmRangeIndex_Type.__name__=_C
_OaEDFAAlarmRangeIndex_Object=MibTableColumn
oaEDFAAlarmRangeIndex=_OaEDFAAlarmRangeIndex_Object((1,3,6,1,4,1,34592,1,5,1,1,1),_OaEDFAAlarmRangeIndex_Type())
oaEDFAAlarmRangeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeIndex.setStatus(_A)
_OaEDFAAlarmRangeDecr_Type=DisplayString
_OaEDFAAlarmRangeDecr_Object=MibTableColumn
oaEDFAAlarmRangeDecr=_OaEDFAAlarmRangeDecr_Object((1,3,6,1,4,1,34592,1,5,1,1,2),_OaEDFAAlarmRangeDecr_Type())
oaEDFAAlarmRangeDecr.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeDecr.setStatus('mandatory')
_OaEDFAAlarmRangeHIHItoHI_Type=Integer32
_OaEDFAAlarmRangeHIHItoHI_Object=MibTableColumn
oaEDFAAlarmRangeHIHItoHI=_OaEDFAAlarmRangeHIHItoHI_Object((1,3,6,1,4,1,34592,1,5,1,1,3),_OaEDFAAlarmRangeHIHItoHI_Type())
oaEDFAAlarmRangeHIHItoHI.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeHIHItoHI.setStatus(_A)
_OaEDFAAlarmRangeHIHItoLO_Type=Integer32
_OaEDFAAlarmRangeHIHItoLO_Object=MibTableColumn
oaEDFAAlarmRangeHIHItoLO=_OaEDFAAlarmRangeHIHItoLO_Object((1,3,6,1,4,1,34592,1,5,1,1,4),_OaEDFAAlarmRangeHIHItoLO_Type())
oaEDFAAlarmRangeHIHItoLO.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeHIHItoLO.setStatus(_A)
_OaEDFAAlarmRangeHItoHI_Type=Integer32
_OaEDFAAlarmRangeHItoHI_Object=MibTableColumn
oaEDFAAlarmRangeHItoHI=_OaEDFAAlarmRangeHItoHI_Object((1,3,6,1,4,1,34592,1,5,1,1,5),_OaEDFAAlarmRangeHItoHI_Type())
oaEDFAAlarmRangeHItoHI.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeHItoHI.setStatus(_A)
_OaEDFAAlarmRangeHItoLO_Type=Integer32
_OaEDFAAlarmRangeHItoLO_Object=MibTableColumn
oaEDFAAlarmRangeHItoLO=_OaEDFAAlarmRangeHItoLO_Object((1,3,6,1,4,1,34592,1,5,1,1,6),_OaEDFAAlarmRangeHItoLO_Type())
oaEDFAAlarmRangeHItoLO.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeHItoLO.setStatus(_A)
_OaEDFAAlarmRangeLOtoHI_Type=Integer32
_OaEDFAAlarmRangeLOtoHI_Object=MibTableColumn
oaEDFAAlarmRangeLOtoHI=_OaEDFAAlarmRangeLOtoHI_Object((1,3,6,1,4,1,34592,1,5,1,1,7),_OaEDFAAlarmRangeLOtoHI_Type())
oaEDFAAlarmRangeLOtoHI.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeLOtoHI.setStatus(_A)
_OaEDFAAlarmRangeLOtoLO_Type=Integer32
_OaEDFAAlarmRangeLOtoLO_Object=MibTableColumn
oaEDFAAlarmRangeLOtoLO=_OaEDFAAlarmRangeLOtoLO_Object((1,3,6,1,4,1,34592,1,5,1,1,8),_OaEDFAAlarmRangeLOtoLO_Type())
oaEDFAAlarmRangeLOtoLO.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeLOtoLO.setStatus(_A)
_OaEDFAAlarmRangeLOLOtoHI_Type=Integer32
_OaEDFAAlarmRangeLOLOtoHI_Object=MibTableColumn
oaEDFAAlarmRangeLOLOtoHI=_OaEDFAAlarmRangeLOLOtoHI_Object((1,3,6,1,4,1,34592,1,5,1,1,9),_OaEDFAAlarmRangeLOLOtoHI_Type())
oaEDFAAlarmRangeLOLOtoHI.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeLOLOtoHI.setStatus(_A)
_OaEDFAAlarmRangeLOLOtoLO_Type=Integer32
_OaEDFAAlarmRangeLOLOtoLO_Object=MibTableColumn
oaEDFAAlarmRangeLOLOtoLO=_OaEDFAAlarmRangeLOLOtoLO_Object((1,3,6,1,4,1,34592,1,5,1,1,10),_OaEDFAAlarmRangeLOLOtoLO_Type())
oaEDFAAlarmRangeLOLOtoLO.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeLOLOtoLO.setStatus(_A)
_OaEDFAAlarmRangeDDtoHI_Type=Integer32
_OaEDFAAlarmRangeDDtoHI_Object=MibTableColumn
oaEDFAAlarmRangeDDtoHI=_OaEDFAAlarmRangeDDtoHI_Object((1,3,6,1,4,1,34592,1,5,1,1,11),_OaEDFAAlarmRangeDDtoHI_Type())
oaEDFAAlarmRangeDDtoHI.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeDDtoHI.setStatus(_A)
_OaEDFAAlarmRangeDDtoLO_Type=Integer32
_OaEDFAAlarmRangeDDtoLO_Object=MibTableColumn
oaEDFAAlarmRangeDDtoLO=_OaEDFAAlarmRangeDDtoLO_Object((1,3,6,1,4,1,34592,1,5,1,1,12),_OaEDFAAlarmRangeDDtoLO_Type())
oaEDFAAlarmRangeDDtoLO.setMaxAccess(_B)
if mibBuilder.loadTexts:oaEDFAAlarmRangeDDtoLO.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'eponeoc':eponeoc,'ipProduct':ipProduct,'mediaConverter':mediaConverter,'edfa':edfa,'oaEDFAAlarmRangeTable':oaEDFAAlarmRangeTable,'oaEDFAAlarmRangeEntry':oaEDFAAlarmRangeEntry,_E:oaEDFAAlarmRangeIndex,'oaEDFAAlarmRangeDecr':oaEDFAAlarmRangeDecr,'oaEDFAAlarmRangeHIHItoHI':oaEDFAAlarmRangeHIHItoHI,'oaEDFAAlarmRangeHIHItoLO':oaEDFAAlarmRangeHIHItoLO,'oaEDFAAlarmRangeHItoHI':oaEDFAAlarmRangeHItoHI,'oaEDFAAlarmRangeHItoLO':oaEDFAAlarmRangeHItoLO,'oaEDFAAlarmRangeLOtoHI':oaEDFAAlarmRangeLOtoHI,'oaEDFAAlarmRangeLOtoLO':oaEDFAAlarmRangeLOtoLO,'oaEDFAAlarmRangeLOLOtoHI':oaEDFAAlarmRangeLOLOtoHI,'oaEDFAAlarmRangeLOLOtoLO':oaEDFAAlarmRangeLOLOtoLO,'oaEDFAAlarmRangeDDtoHI':oaEDFAAlarmRangeDDtoHI,'oaEDFAAlarmRangeDDtoLO':oaEDFAAlarmRangeDDtoLO})