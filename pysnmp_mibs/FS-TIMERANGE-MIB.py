_I='fsPeriTRStr'
_H='fsPeriTRName'
_G='fsTRName'
_F='Integer32'
_E='read-create'
_D='read-only'
_C='FS-TIMERANGE-MIB'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_B,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsTrsMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,144))
if mibBuilder.loadTexts:fsTrsMIB.setRevisions(('2015-09-20 00:00',))
_FsTrsMIBObjects_ObjectIdentity=ObjectIdentity
fsTrsMIBObjects=_FsTrsMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,144,1))
_FsTRTable_Object=MibTable
fsTRTable=_FsTRTable_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,1))
if mibBuilder.loadTexts:fsTRTable.setStatus(_A)
_FsTREntry_Object=MibTableRow
fsTREntry=_FsTREntry_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,1,1))
fsTREntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:fsTREntry.setStatus(_A)
class _FsTRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsTRName_Type.__name__=_B
_FsTRName_Object=MibTableColumn
fsTRName=_FsTRName_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,1,1,1),_FsTRName_Type())
fsTRName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTRName.setStatus(_A)
class _FsAbsTRStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsAbsTRStr_Type.__name__=_B
_FsAbsTRStr_Object=MibTableColumn
fsAbsTRStr=_FsAbsTRStr_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,1,1,2),_FsAbsTRStr_Type())
fsAbsTRStr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsAbsTRStr.setStatus(_A)
_FsTRIndex_Type=Integer32
_FsTRIndex_Object=MibTableColumn
fsTRIndex=_FsTRIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,1,1,3),_FsTRIndex_Type())
fsTRIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTRIndex.setStatus(_A)
class _FsTRMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tr-add',1),('tr-del',2)))
_FsTRMode_Type.__name__=_F
_FsTRMode_Object=MibTableColumn
fsTRMode=_FsTRMode_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,1,1,4),_FsTRMode_Type())
fsTRMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fsTRMode.setStatus(_A)
_FsTRPeriTable_Object=MibTable
fsTRPeriTable=_FsTRPeriTable_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,3))
if mibBuilder.loadTexts:fsTRPeriTable.setStatus(_A)
_FsTRPeriEntry_Object=MibTableRow
fsTRPeriEntry=_FsTRPeriEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,3,1))
fsTRPeriEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:fsTRPeriEntry.setStatus(_A)
class _FsPeriTRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsPeriTRName_Type.__name__=_B
_FsPeriTRName_Object=MibTableColumn
fsPeriTRName=_FsPeriTRName_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,3,1,1),_FsPeriTRName_Type())
fsPeriTRName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPeriTRName.setStatus(_A)
class _FsPeriTRStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_FsPeriTRStr_Type.__name__=_B
_FsPeriTRStr_Object=MibTableColumn
fsPeriTRStr=_FsPeriTRStr_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,3,1,2),_FsPeriTRStr_Type())
fsPeriTRStr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPeriTRStr.setStatus(_A)
_FsPeriTRIndex_Type=Integer32
_FsPeriTRIndex_Object=MibTableColumn
fsPeriTRIndex=_FsPeriTRIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,3,1,3),_FsPeriTRIndex_Type())
fsPeriTRIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPeriTRIndex.setStatus(_A)
class _FsPeriTRMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('periodic-add',1),('periodic-del',2)))
_FsPeriTRMode_Type.__name__=_F
_FsPeriTRMode_Object=MibTableColumn
fsPeriTRMode=_FsPeriTRMode_Object((1,3,6,1,4,1,52642,1,1,10,2,144,1,3,1,4),_FsPeriTRMode_Type())
fsPeriTRMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPeriTRMode.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsTrsMIB':fsTrsMIB,'fsTrsMIBObjects':fsTrsMIBObjects,'fsTRTable':fsTRTable,'fsTREntry':fsTREntry,_G:fsTRName,'fsAbsTRStr':fsAbsTRStr,'fsTRIndex':fsTRIndex,'fsTRMode':fsTRMode,'fsTRPeriTable':fsTRPeriTable,'fsTRPeriEntry':fsTRPeriEntry,_H:fsPeriTRName,_I:fsPeriTRStr,'fsPeriTRIndex':fsPeriTRIndex,'fsPeriTRMode':fsPeriTRMode})