_D='decodeType'
_C='CISCO-DMN-DSG-DECODE-ENABLE-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDSGDecodeEnable=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,13))
if mibBuilder.loadTexts:ciscoDSGDecodeEnable.setRevisions(('2010-08-30 06:00','2009-12-07 12:00'))
_DecodeEnableTable_Object=MibTable
decodeEnableTable=_DecodeEnableTable_Object((1,3,6,1,4,1,1429,2,2,5,13,1))
if mibBuilder.loadTexts:decodeEnableTable.setStatus(_A)
_DecodeEnableEntry_Object=MibTableRow
decodeEnableEntry=_DecodeEnableEntry_Object((1,3,6,1,4,1,1429,2,2,5,13,1,1))
decodeEnableEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:decodeEnableEntry.setStatus(_A)
class _DecodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('video',1),('audio1',2),('audio2',3),('audio3',4),('audio4',5),('vbi',6),('data',7),('mpe1',8),('mpe2',9),('mpe3',10),('mpe4',11),('mpe5',12),('stt',13),('dpi',14)))
_DecodeType_Type.__name__=_B
_DecodeType_Object=MibTableColumn
decodeType=_DecodeType_Object((1,3,6,1,4,1,1429,2,2,5,13,1,1,1),_DecodeType_Type())
decodeType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:decodeType.setStatus(_A)
class _DecodeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_DecodeEnable_Type.__name__=_B
_DecodeEnable_Object=MibTableColumn
decodeEnable=_DecodeEnable_Object((1,3,6,1,4,1,1429,2,2,5,13,1,1,2),_DecodeEnable_Type())
decodeEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:decodeEnable.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ciscoDSGDecodeEnable':ciscoDSGDecodeEnable,'decodeEnableTable':decodeEnableTable,'decodeEnableEntry':decodeEnableEntry,_D:decodeType,'decodeEnable':decodeEnable})