_F='scmDiagnosticsDeviceIndex'
_E='SAMSUNG-DIAGNOSTICS-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
samsungCommonMIB,=mibBuilder.importSymbols('SAMSUNG-COMMON-MIB','samsungCommonMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
scmDiagnostics=ModuleIdentity((1,3,6,1,4,1,236,11,5,11,64))
_ScmDiagnosticsDevice_ObjectIdentity=ObjectIdentity
scmDiagnosticsDevice=_ScmDiagnosticsDevice_ObjectIdentity((1,3,6,1,4,1,236,11,5,11,64,1))
_ScmDiagnosticsDeviceTable_Object=MibTable
scmDiagnosticsDeviceTable=_ScmDiagnosticsDeviceTable_Object((1,3,6,1,4,1,236,11,5,11,64,1,2))
if mibBuilder.loadTexts:scmDiagnosticsDeviceTable.setStatus(_A)
_ScmDiagnosticsDeviceEntry_Object=MibTableRow
scmDiagnosticsDeviceEntry=_ScmDiagnosticsDeviceEntry_Object((1,3,6,1,4,1,236,11,5,11,64,1,2,1))
scmDiagnosticsDeviceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:scmDiagnosticsDeviceEntry.setStatus(_A)
class _ScmDiagnosticsDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ScmDiagnosticsDeviceIndex_Type.__name__=_C
_ScmDiagnosticsDeviceIndex_Object=MibTableColumn
scmDiagnosticsDeviceIndex=_ScmDiagnosticsDeviceIndex_Object((1,3,6,1,4,1,236,11,5,11,64,1,2,1,1),_ScmDiagnosticsDeviceIndex_Type())
scmDiagnosticsDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:scmDiagnosticsDeviceIndex.setStatus(_A)
class _ScmDiagnosticsDeviceItem_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ScmDiagnosticsDeviceItem_Type.__name__=_D
_ScmDiagnosticsDeviceItem_Object=MibTableColumn
scmDiagnosticsDeviceItem=_ScmDiagnosticsDeviceItem_Object((1,3,6,1,4,1,236,11,5,11,64,1,2,1,2),_ScmDiagnosticsDeviceItem_Type())
scmDiagnosticsDeviceItem.setMaxAccess(_B)
if mibBuilder.loadTexts:scmDiagnosticsDeviceItem.setStatus(_A)
class _ScmDiagnosticsDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,21,22,23,24,25,26,41,42,43)));namedValues=NamedValues(*(('input',1),('output',2),('cover',3),('geeralPrinter',4),('mediaPath',5),('marker',6),('markerSupplies',7),('markerColorant',8),('fax',21),('scanner',22),('network',23),('usb',24),('parallel',25),('finisher',26),('motor',41),('smps',42),('memory',43)))
_ScmDiagnosticsDeviceType_Type.__name__=_C
_ScmDiagnosticsDeviceType_Object=MibTableColumn
scmDiagnosticsDeviceType=_ScmDiagnosticsDeviceType_Object((1,3,6,1,4,1,236,11,5,11,64,1,2,1,3),_ScmDiagnosticsDeviceType_Type())
scmDiagnosticsDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:scmDiagnosticsDeviceType.setStatus(_A)
class _ScmDiagnosticsDeviceDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ScmDiagnosticsDeviceDescr_Type.__name__=_D
_ScmDiagnosticsDeviceDescr_Object=MibTableColumn
scmDiagnosticsDeviceDescr=_ScmDiagnosticsDeviceDescr_Object((1,3,6,1,4,1,236,11,5,11,64,1,2,1,4),_ScmDiagnosticsDeviceDescr_Type())
scmDiagnosticsDeviceDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:scmDiagnosticsDeviceDescr.setStatus(_A)
class _ScmDiagnosticsDeviceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ScmDiagnosticsDeviceID_Type.__name__=_C
_ScmDiagnosticsDeviceID_Object=MibTableColumn
scmDiagnosticsDeviceID=_ScmDiagnosticsDeviceID_Object((1,3,6,1,4,1,236,11,5,11,64,1,2,1,5),_ScmDiagnosticsDeviceID_Type())
scmDiagnosticsDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:scmDiagnosticsDeviceID.setStatus(_A)
class _ScmDiagnosticsDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('running',2),('warning',3),('testing',4),('down',5),('printing',6)))
_ScmDiagnosticsDeviceStatus_Type.__name__=_C
_ScmDiagnosticsDeviceStatus_Object=MibTableColumn
scmDiagnosticsDeviceStatus=_ScmDiagnosticsDeviceStatus_Object((1,3,6,1,4,1,236,11,5,11,64,1,2,1,6),_ScmDiagnosticsDeviceStatus_Type())
scmDiagnosticsDeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scmDiagnosticsDeviceStatus.setStatus(_A)
_ScmDiagnosticsDeviceErrors_Type=Counter32
_ScmDiagnosticsDeviceErrors_Object=MibTableColumn
scmDiagnosticsDeviceErrors=_ScmDiagnosticsDeviceErrors_Object((1,3,6,1,4,1,236,11,5,11,64,1,2,1,7),_ScmDiagnosticsDeviceErrors_Type())
scmDiagnosticsDeviceErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:scmDiagnosticsDeviceErrors.setStatus(_A)
class _ScmDiagnosticsRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_ScmDiagnosticsRequest_Type.__name__=_C
_ScmDiagnosticsRequest_Object=MibTableColumn
scmDiagnosticsRequest=_ScmDiagnosticsRequest_Object((1,3,6,1,4,1,236,11,5,11,64,1,2,1,8),_ScmDiagnosticsRequest_Type())
scmDiagnosticsRequest.setMaxAccess('read-write')
if mibBuilder.loadTexts:scmDiagnosticsRequest.setStatus(_A)
class _ScmGenBaseDeviceImageFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ScmGenBaseDeviceImageFileName_Type.__name__=_D
_ScmGenBaseDeviceImageFileName_Object=MibTableColumn
scmGenBaseDeviceImageFileName=_ScmGenBaseDeviceImageFileName_Object((1,3,6,1,4,1,236,11,5,11,64,1,2,1,999),_ScmGenBaseDeviceImageFileName_Type())
scmGenBaseDeviceImageFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:scmGenBaseDeviceImageFileName.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'scmDiagnostics':scmDiagnostics,'scmDiagnosticsDevice':scmDiagnosticsDevice,'scmDiagnosticsDeviceTable':scmDiagnosticsDeviceTable,'scmDiagnosticsDeviceEntry':scmDiagnosticsDeviceEntry,_F:scmDiagnosticsDeviceIndex,'scmDiagnosticsDeviceItem':scmDiagnosticsDeviceItem,'scmDiagnosticsDeviceType':scmDiagnosticsDeviceType,'scmDiagnosticsDeviceDescr':scmDiagnosticsDeviceDescr,'scmDiagnosticsDeviceID':scmDiagnosticsDeviceID,'scmDiagnosticsDeviceStatus':scmDiagnosticsDeviceStatus,'scmDiagnosticsDeviceErrors':scmDiagnosticsDeviceErrors,'scmDiagnosticsRequest':scmDiagnosticsRequest,'scmGenBaseDeviceImageFileName':scmGenBaseDeviceImageFileName})