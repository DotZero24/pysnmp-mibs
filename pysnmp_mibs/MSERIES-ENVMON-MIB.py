_H='smartEnvMonTemperatureGroupV1'
_G='smartEnvMonTemperatureValue'
_F='smartEnvMonTemperatureDescr'
_E='Unsigned32'
_D='read-only'
_C='smartEnvMonTemperatureIndex'
_B='MSERIES-ENVMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mseries,=mibBuilder.importSymbols('MSERIES-MIB','mseries')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
smartEnvMon=ModuleIdentity((1,3,6,1,4,1,30826,1,4))
if mibBuilder.loadTexts:smartEnvMon.setRevisions(('2014-02-15 10:34',))
_SmartEnvMonObjects_ObjectIdentity=ObjectIdentity
smartEnvMonObjects=_SmartEnvMonObjects_ObjectIdentity((1,3,6,1,4,1,30826,1,4,1))
_SmartEnvMonTemperatureTable_Object=MibTable
smartEnvMonTemperatureTable=_SmartEnvMonTemperatureTable_Object((1,3,6,1,4,1,30826,1,4,1,1))
if mibBuilder.loadTexts:smartEnvMonTemperatureTable.setStatus(_A)
_SmartEnvMonTemperatureEntry_Object=MibTableRow
smartEnvMonTemperatureEntry=_SmartEnvMonTemperatureEntry_Object((1,3,6,1,4,1,30826,1,4,1,1,1))
smartEnvMonTemperatureEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:smartEnvMonTemperatureEntry.setStatus(_A)
class _SmartEnvMonTemperatureIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SmartEnvMonTemperatureIndex_Type.__name__=_E
_SmartEnvMonTemperatureIndex_Object=MibTableColumn
smartEnvMonTemperatureIndex=_SmartEnvMonTemperatureIndex_Object((1,3,6,1,4,1,30826,1,4,1,1,1,1),_SmartEnvMonTemperatureIndex_Type())
smartEnvMonTemperatureIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:smartEnvMonTemperatureIndex.setStatus(_A)
_SmartEnvMonTemperatureDescr_Type=DisplayString
_SmartEnvMonTemperatureDescr_Object=MibTableColumn
smartEnvMonTemperatureDescr=_SmartEnvMonTemperatureDescr_Object((1,3,6,1,4,1,30826,1,4,1,1,1,2),_SmartEnvMonTemperatureDescr_Type())
smartEnvMonTemperatureDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:smartEnvMonTemperatureDescr.setStatus(_A)
_SmartEnvMonTemperatureValue_Type=Integer32
_SmartEnvMonTemperatureValue_Object=MibTableColumn
smartEnvMonTemperatureValue=_SmartEnvMonTemperatureValue_Object((1,3,6,1,4,1,30826,1,4,1,1,1,3),_SmartEnvMonTemperatureValue_Type())
smartEnvMonTemperatureValue.setMaxAccess(_D)
if mibBuilder.loadTexts:smartEnvMonTemperatureValue.setStatus(_A)
if mibBuilder.loadTexts:smartEnvMonTemperatureValue.setUnits('degrees Celsius')
_SmartEnvMonMIBConformance_ObjectIdentity=ObjectIdentity
smartEnvMonMIBConformance=_SmartEnvMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,30826,1,4,2))
_SmartEnvMonGroups_ObjectIdentity=ObjectIdentity
smartEnvMonGroups=_SmartEnvMonGroups_ObjectIdentity((1,3,6,1,4,1,30826,1,4,2,1))
_SmartEnvMonCompliances_ObjectIdentity=ObjectIdentity
smartEnvMonCompliances=_SmartEnvMonCompliances_ObjectIdentity((1,3,6,1,4,1,30826,1,4,2,2))
smartEnvMonTemperatureGroupV1=ObjectGroup((1,3,6,1,4,1,30826,1,4,2,1,1))
smartEnvMonTemperatureGroupV1.setObjects(*((_B,_C),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:smartEnvMonTemperatureGroupV1.setStatus(_A)
smartEnvMonBasicComplV1=ModuleCompliance((1,3,6,1,4,1,30826,1,4,2,2,1))
smartEnvMonBasicComplV1.setObjects((_B,_H))
if mibBuilder.loadTexts:smartEnvMonBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'smartEnvMon':smartEnvMon,'smartEnvMonObjects':smartEnvMonObjects,'smartEnvMonTemperatureTable':smartEnvMonTemperatureTable,'smartEnvMonTemperatureEntry':smartEnvMonTemperatureEntry,_C:smartEnvMonTemperatureIndex,_F:smartEnvMonTemperatureDescr,_G:smartEnvMonTemperatureValue,'smartEnvMonMIBConformance':smartEnvMonMIBConformance,'smartEnvMonGroups':smartEnvMonGroups,_H:smartEnvMonTemperatureGroupV1,'smartEnvMonCompliances':smartEnvMonCompliances,'smartEnvMonBasicComplV1':smartEnvMonBasicComplV1})