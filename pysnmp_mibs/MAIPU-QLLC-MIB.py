_F='qllcIndex'
_E='MAIPU-QLLC-MIB'
_D='OctetString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mpQllcMib=ModuleIdentity((1,3,6,1,4,1,5651,3,100))
_QllcConfTable_Object=MibTable
qllcConfTable=_QllcConfTable_Object((1,3,6,1,4,1,5651,3,100,1))
if mibBuilder.loadTexts:qllcConfTable.setStatus(_A)
_QllcConfEntry_Object=MibTableRow
qllcConfEntry=_QllcConfEntry_Object((1,3,6,1,4,1,5651,3,100,1,1))
qllcConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qllcConfEntry.setStatus(_A)
_QllcIndex_Type=Integer32
_QllcIndex_Object=MibTableColumn
qllcIndex=_QllcIndex_Object((1,3,6,1,4,1,5651,3,100,1,1,1),_QllcIndex_Type())
qllcIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:qllcIndex.setStatus(_A)
class _QllcFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('default',1),('pvc',2),('vmacaddr',3)))
_QllcFlag_Type.__name__=_C
_QllcFlag_Object=MibTableColumn
qllcFlag=_QllcFlag_Object((1,3,6,1,4,1,5651,3,100,1,1,2),_QllcFlag_Type())
qllcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:qllcFlag.setStatus(_A)
class _QllcPartner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_QllcPartner_Type.__name__=_D
_QllcPartner_Object=MibTableColumn
qllcPartner=_QllcPartner_Object((1,3,6,1,4,1,5651,3,100,1,1,3),_QllcPartner_Type())
qllcPartner.setMaxAccess(_B)
if mibBuilder.loadTexts:qllcPartner.setStatus(_A)
class _QllcXidDivert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('divert',2)))
_QllcXidDivert_Type.__name__=_C
_QllcXidDivert_Object=MibTableColumn
qllcXidDivert=_QllcXidDivert_Object((1,3,6,1,4,1,5651,3,100,1,1,4),_QllcXidDivert_Type())
qllcXidDivert.setMaxAccess(_B)
if mibBuilder.loadTexts:qllcXidDivert.setStatus(_A)
class _QllcPvc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_QllcPvc_Type.__name__=_C
_QllcPvc_Object=MibTableColumn
qllcPvc=_QllcPvc_Object((1,3,6,1,4,1,5651,3,100,1,1,5),_QllcPvc_Type())
qllcPvc.setMaxAccess(_B)
if mibBuilder.loadTexts:qllcPvc.setStatus(_A)
class _QllcOrigin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_QllcOrigin_Type.__name__=_D
_QllcOrigin_Object=MibTableColumn
qllcOrigin=_QllcOrigin_Object((1,3,6,1,4,1,5651,3,100,1,1,6),_QllcOrigin_Type())
qllcOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:qllcOrigin.setStatus(_A)
_QllcStatus_Type=RowStatus
_QllcStatus_Object=MibTableColumn
qllcStatus=_QllcStatus_Object((1,3,6,1,4,1,5651,3,100,1,1,7),_QllcStatus_Type())
qllcStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qllcStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mpQllcMib':mpQllcMib,'qllcConfTable':qllcConfTable,'qllcConfEntry':qllcConfEntry,_F:qllcIndex,'qllcFlag':qllcFlag,'qllcPartner':qllcPartner,'qllcXidDivert':qllcXidDivert,'qllcPvc':qllcPvc,'qllcOrigin':qllcOrigin,'qllcStatus':qllcStatus})