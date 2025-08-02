_F='read-only'
_E='hmITSysIfIndex'
_D='HMIT-SYS-IF-MIB'
_C='DisplayString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmITSystem,=mibBuilder.importSymbols('HMIT-SMI','hmITSystem')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
hmITSysIfMIB=ModuleIdentity((1,3,6,1,4,1,248,100,1,6,1,11))
if mibBuilder.loadTexts:hmITSysIfMIB.setRevisions(('2010-01-08 17:00',))
_HmITSysIfTable_Object=MibTable
hmITSysIfTable=_HmITSysIfTable_Object((1,3,6,1,4,1,248,100,1,6,1,11,1))
if mibBuilder.loadTexts:hmITSysIfTable.setStatus(_A)
_HmITSysIfEntry_Object=MibTableRow
hmITSysIfEntry=_HmITSysIfEntry_Object((1,3,6,1,4,1,248,100,1,6,1,11,1,1))
hmITSysIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hmITSysIfEntry.setStatus(_A)
class _HmITSysIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HmITSysIfIndex_Type.__name__=_B
_HmITSysIfIndex_Object=MibTableColumn
hmITSysIfIndex=_HmITSysIfIndex_Object((1,3,6,1,4,1,248,100,1,6,1,11,1,1,1),_HmITSysIfIndex_Type())
hmITSysIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hmITSysIfIndex.setStatus(_A)
class _HmITSysIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,39))
_HmITSysIfName_Type.__name__=_C
_HmITSysIfName_Object=MibTableColumn
hmITSysIfName=_HmITSysIfName_Object((1,3,6,1,4,1,248,100,1,6,1,11,1,1,2),_HmITSysIfName_Type())
hmITSysIfName.setMaxAccess(_F)
if mibBuilder.loadTexts:hmITSysIfName.setStatus(_A)
class _HmITSysIfReliability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HmITSysIfReliability_Type.__name__=_B
_HmITSysIfReliability_Object=MibTableColumn
hmITSysIfReliability=_HmITSysIfReliability_Object((1,3,6,1,4,1,248,100,1,6,1,11,1,1,3),_HmITSysIfReliability_Type())
hmITSysIfReliability.setMaxAccess(_F)
if mibBuilder.loadTexts:hmITSysIfReliability.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hmITSysIfMIB':hmITSysIfMIB,'hmITSysIfTable':hmITSysIfTable,'hmITSysIfEntry':hmITSysIfEntry,_E:hmITSysIfIndex,'hmITSysIfName':hmITSysIfName,'hmITSysIfReliability':hmITSysIfReliability})