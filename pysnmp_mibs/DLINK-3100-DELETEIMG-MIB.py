_E='read-write'
_D='rlDeleteImgKey'
_C='DLINK-3100-DELETEIMG-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlDeleteImg=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,142))
if mibBuilder.loadTexts:rlDeleteImg.setRevisions(('2007-11-18 00:00',))
class DELETEIMGName(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('image1',1),('image2',2)))
_RlDeleteImgTable_Object=MibTable
rlDeleteImgTable=_RlDeleteImgTable_Object((1,3,6,1,4,1,171,10,94,89,89,142,1))
if mibBuilder.loadTexts:rlDeleteImgTable.setStatus(_A)
_RlDeleteImgEntry_Object=MibTableRow
rlDeleteImgEntry=_RlDeleteImgEntry_Object((1,3,6,1,4,1,171,10,94,89,89,142,1,1))
rlDeleteImgEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:rlDeleteImgEntry.setStatus(_A)
class _RlDeleteImgKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_RlDeleteImgKey_Type.__name__=_B
_RlDeleteImgKey_Object=MibTableColumn
rlDeleteImgKey=_RlDeleteImgKey_Object((1,3,6,1,4,1,171,10,94,89,89,142,1,1,1),_RlDeleteImgKey_Type())
rlDeleteImgKey.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlDeleteImgKey.setStatus(_A)
_RlDeleteImgUnit_Type=Integer32
_RlDeleteImgUnit_Object=MibTableColumn
rlDeleteImgUnit=_RlDeleteImgUnit_Object((1,3,6,1,4,1,171,10,94,89,89,142,1,1,2),_RlDeleteImgUnit_Type())
rlDeleteImgUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:rlDeleteImgUnit.setStatus(_A)
_RlDeleteImgName_Type=DELETEIMGName
_RlDeleteImgName_Object=MibTableColumn
rlDeleteImgName=_RlDeleteImgName_Object((1,3,6,1,4,1,171,10,94,89,89,142,1,1,3),_RlDeleteImgName_Type())
rlDeleteImgName.setMaxAccess(_E)
if mibBuilder.loadTexts:rlDeleteImgName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'DELETEIMGName':DELETEIMGName,'rlDeleteImg':rlDeleteImg,'rlDeleteImgTable':rlDeleteImgTable,'rlDeleteImgEntry':rlDeleteImgEntry,_D:rlDeleteImgKey,'rlDeleteImgUnit':rlDeleteImgUnit,'rlDeleteImgName':rlDeleteImgName})