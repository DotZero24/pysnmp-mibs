_E='diskIOIndex'
_D='UCD-DISKIO-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ucdExperimental,=mibBuilder.importSymbols('UCD-SNMP-MIB','ucdExperimental')
ucdDiskIOMIB=ModuleIdentity((1,3,6,1,4,1,2021,13,15))
if mibBuilder.loadTexts:ucdDiskIOMIB.setRevisions(('2005-04-20 00:00','2002-02-13 00:00','2000-01-26 00:00'))
_DiskIOTable_Object=MibTable
diskIOTable=_DiskIOTable_Object((1,3,6,1,4,1,2021,13,15,1))
if mibBuilder.loadTexts:diskIOTable.setStatus(_A)
_DiskIOEntry_Object=MibTableRow
diskIOEntry=_DiskIOEntry_Object((1,3,6,1,4,1,2021,13,15,1,1))
diskIOEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:diskIOEntry.setStatus(_A)
class _DiskIOIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DiskIOIndex_Type.__name__=_C
_DiskIOIndex_Object=MibTableColumn
diskIOIndex=_DiskIOIndex_Object((1,3,6,1,4,1,2021,13,15,1,1,1),_DiskIOIndex_Type())
diskIOIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIOIndex.setStatus(_A)
_DiskIODevice_Type=DisplayString
_DiskIODevice_Object=MibTableColumn
diskIODevice=_DiskIODevice_Object((1,3,6,1,4,1,2021,13,15,1,1,2),_DiskIODevice_Type())
diskIODevice.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIODevice.setStatus(_A)
_DiskIONRead_Type=Counter32
_DiskIONRead_Object=MibTableColumn
diskIONRead=_DiskIONRead_Object((1,3,6,1,4,1,2021,13,15,1,1,3),_DiskIONRead_Type())
diskIONRead.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIONRead.setStatus(_A)
_DiskIONWritten_Type=Counter32
_DiskIONWritten_Object=MibTableColumn
diskIONWritten=_DiskIONWritten_Object((1,3,6,1,4,1,2021,13,15,1,1,4),_DiskIONWritten_Type())
diskIONWritten.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIONWritten.setStatus(_A)
_DiskIOReads_Type=Counter32
_DiskIOReads_Object=MibTableColumn
diskIOReads=_DiskIOReads_Object((1,3,6,1,4,1,2021,13,15,1,1,5),_DiskIOReads_Type())
diskIOReads.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIOReads.setStatus(_A)
_DiskIOWrites_Type=Counter32
_DiskIOWrites_Object=MibTableColumn
diskIOWrites=_DiskIOWrites_Object((1,3,6,1,4,1,2021,13,15,1,1,6),_DiskIOWrites_Type())
diskIOWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIOWrites.setStatus(_A)
class _DiskIOLA1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DiskIOLA1_Type.__name__=_C
_DiskIOLA1_Object=MibTableColumn
diskIOLA1=_DiskIOLA1_Object((1,3,6,1,4,1,2021,13,15,1,1,9),_DiskIOLA1_Type())
diskIOLA1.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIOLA1.setStatus(_A)
class _DiskIOLA5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DiskIOLA5_Type.__name__=_C
_DiskIOLA5_Object=MibTableColumn
diskIOLA5=_DiskIOLA5_Object((1,3,6,1,4,1,2021,13,15,1,1,10),_DiskIOLA5_Type())
diskIOLA5.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIOLA5.setStatus(_A)
class _DiskIOLA15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DiskIOLA15_Type.__name__=_C
_DiskIOLA15_Object=MibTableColumn
diskIOLA15=_DiskIOLA15_Object((1,3,6,1,4,1,2021,13,15,1,1,11),_DiskIOLA15_Type())
diskIOLA15.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIOLA15.setStatus(_A)
_DiskIONReadX_Type=Counter64
_DiskIONReadX_Object=MibTableColumn
diskIONReadX=_DiskIONReadX_Object((1,3,6,1,4,1,2021,13,15,1,1,12),_DiskIONReadX_Type())
diskIONReadX.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIONReadX.setStatus(_A)
_DiskIONWrittenX_Type=Counter64
_DiskIONWrittenX_Object=MibTableColumn
diskIONWrittenX=_DiskIONWrittenX_Object((1,3,6,1,4,1,2021,13,15,1,1,13),_DiskIONWrittenX_Type())
diskIONWrittenX.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIONWrittenX.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ucdDiskIOMIB':ucdDiskIOMIB,'diskIOTable':diskIOTable,'diskIOEntry':diskIOEntry,_E:diskIOIndex,'diskIODevice':diskIODevice,'diskIONRead':diskIONRead,'diskIONWritten':diskIONWritten,'diskIOReads':diskIOReads,'diskIOWrites':diskIOWrites,'diskIOLA1':diskIOLA1,'diskIOLA5':diskIOLA5,'diskIOLA15':diskIOLA15,'diskIONReadX':diskIONReadX,'diskIONWrittenX':diskIONWrittenX})