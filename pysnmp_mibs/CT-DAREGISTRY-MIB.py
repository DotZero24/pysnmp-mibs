_H='testing'
_G='ctDARegistryInstance'
_F='ctDARegistryIndex'
_E='CT-DAREGISTRY-MIB'
_D='DisplayString'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cabletron,=mibBuilder.importSymbols('CTRON-OIDS','cabletron')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_CtSSA_ObjectIdentity=ObjectIdentity
ctSSA=_CtSSA_ObjectIdentity((1,3,6,1,4,1,52,4497))
_CtDARegistryTable_Object=MibTable
ctDARegistryTable=_CtDARegistryTable_Object((1,3,6,1,4,1,52,4497,1))
if mibBuilder.loadTexts:ctDARegistryTable.setStatus(_A)
_CtDARegistryEntry_Object=MibTableRow
ctDARegistryEntry=_CtDARegistryEntry_Object((1,3,6,1,4,1,52,4497,1,1))
ctDARegistryEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:ctDARegistryEntry.setStatus(_A)
class _CtDARegistryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtDARegistryIndex_Type.__name__=_B
_CtDARegistryIndex_Object=MibTableColumn
ctDARegistryIndex=_CtDARegistryIndex_Object((1,3,6,1,4,1,52,4497,1,1,1),_CtDARegistryIndex_Type())
ctDARegistryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDARegistryIndex.setStatus(_A)
class _CtDARegistryInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtDARegistryInstance_Type.__name__=_B
_CtDARegistryInstance_Object=MibTableColumn
ctDARegistryInstance=_CtDARegistryInstance_Object((1,3,6,1,4,1,52,4497,1,1,2),_CtDARegistryInstance_Type())
ctDARegistryInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDARegistryInstance.setStatus(_A)
class _CtDARegistryAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_H,3)))
_CtDARegistryAdminStatus_Type.__name__=_B
_CtDARegistryAdminStatus_Object=MibTableColumn
ctDARegistryAdminStatus=_CtDARegistryAdminStatus_Object((1,3,6,1,4,1,52,4497,1,1,3),_CtDARegistryAdminStatus_Type())
ctDARegistryAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:ctDARegistryAdminStatus.setStatus(_A)
class _CtDARegistryOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),(_H,3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_CtDARegistryOperStatus_Type.__name__=_B
_CtDARegistryOperStatus_Object=MibTableColumn
ctDARegistryOperStatus=_CtDARegistryOperStatus_Object((1,3,6,1,4,1,52,4497,1,1,4),_CtDARegistryOperStatus_Type())
ctDARegistryOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDARegistryOperStatus.setStatus(_A)
_CtDARegistryLastChange_Type=TimeTicks
_CtDARegistryLastChange_Object=MibTableColumn
ctDARegistryLastChange=_CtDARegistryLastChange_Object((1,3,6,1,4,1,52,4497,1,1,5),_CtDARegistryLastChange_Type())
ctDARegistryLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDARegistryLastChange.setStatus(_A)
class _CtDARegistryDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtDARegistryDescr_Type.__name__=_D
_CtDARegistryDescr_Object=MibTableColumn
ctDARegistryDescr=_CtDARegistryDescr_Object((1,3,6,1,4,1,52,4497,1,1,6),_CtDARegistryDescr_Type())
ctDARegistryDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDARegistryDescr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_D:DisplayString,'ctSSA':ctSSA,'ctDARegistryTable':ctDARegistryTable,'ctDARegistryEntry':ctDARegistryEntry,_F:ctDARegistryIndex,_G:ctDARegistryInstance,'ctDARegistryAdminStatus':ctDARegistryAdminStatus,'ctDARegistryOperStatus':ctDARegistryOperStatus,'ctDARegistryLastChange':ctDARegistryLastChange,'ctDARegistryDescr':ctDARegistryDescr})