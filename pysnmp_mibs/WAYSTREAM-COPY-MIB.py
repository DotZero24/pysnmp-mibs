_G='wsCopyIndex'
_F='WAYSTREAM-COPY-MIB'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
wsExperiment,=mibBuilder.importSymbols('WAYSTREAM-SMI','wsExperiment')
wsCopy=ModuleIdentity((1,3,6,1,4,1,9303,3,2))
if mibBuilder.loadTexts:wsCopy.setRevisions(('2017-02-10 11:00','2011-01-11 17:35','2009-03-23 11:17','2008-09-10 15:38'))
_WsCopyNextState_Type=Unsigned32
_WsCopyNextState_Object=MibScalar
wsCopyNextState=_WsCopyNextState_Object((1,3,6,1,4,1,9303,3,2,1),_WsCopyNextState_Type())
wsCopyNextState.setMaxAccess(_C)
if mibBuilder.loadTexts:wsCopyNextState.setStatus(_A)
_WsCopyTable_Object=MibTable
wsCopyTable=_WsCopyTable_Object((1,3,6,1,4,1,9303,3,2,2))
if mibBuilder.loadTexts:wsCopyTable.setStatus(_A)
_WsCopyEntry_Object=MibTableRow
wsCopyEntry=_WsCopyEntry_Object((1,3,6,1,4,1,9303,3,2,2,1))
wsCopyEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wsCopyEntry.setStatus(_A)
_WsCopyIndex_Type=Unsigned32
_WsCopyIndex_Object=MibTableColumn
wsCopyIndex=_WsCopyIndex_Object((1,3,6,1,4,1,9303,3,2,2,1,1),_WsCopyIndex_Type())
wsCopyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wsCopyIndex.setStatus(_A)
class _WsCopySource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WsCopySource_Type.__name__=_B
_WsCopySource_Object=MibTableColumn
wsCopySource=_WsCopySource_Object((1,3,6,1,4,1,9303,3,2,2,1,2),_WsCopySource_Type())
wsCopySource.setMaxAccess(_D)
if mibBuilder.loadTexts:wsCopySource.setStatus(_A)
class _WsCopyDestination_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WsCopyDestination_Type.__name__=_B
_WsCopyDestination_Object=MibTableColumn
wsCopyDestination=_WsCopyDestination_Object((1,3,6,1,4,1,9303,3,2,2,1,3),_WsCopyDestination_Type())
wsCopyDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:wsCopyDestination.setStatus(_A)
class _WsCopyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notused',0),('start',1),('stop',2),('destroy',3),('init',4),('inprogress',5),('failed',6),('finished',7)))
_WsCopyStatus_Type.__name__=_E
_WsCopyStatus_Object=MibTableColumn
wsCopyStatus=_WsCopyStatus_Object((1,3,6,1,4,1,9303,3,2,2,1,4),_WsCopyStatus_Type())
wsCopyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wsCopyStatus.setStatus(_A)
class _WsCopyError_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WsCopyError_Type.__name__=_B
_WsCopyError_Object=MibTableColumn
wsCopyError=_WsCopyError_Object((1,3,6,1,4,1,9303,3,2,2,1,5),_WsCopyError_Type())
wsCopyError.setMaxAccess(_C)
if mibBuilder.loadTexts:wsCopyError.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'wsCopy':wsCopy,'wsCopyNextState':wsCopyNextState,'wsCopyTable':wsCopyTable,'wsCopyEntry':wsCopyEntry,_G:wsCopyIndex,'wsCopySource':wsCopySource,'wsCopyDestination':wsCopyDestination,'wsCopyStatus':wsCopyStatus,'wsCopyError':wsCopyError})