_G='pfCopyIndex'
_F='PACKETFRONT-COPY-MIB'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pfExperiment,=mibBuilder.importSymbols('PACKETFRONT-SMI','pfExperiment')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
pfCopy=ModuleIdentity((1,3,6,1,4,1,9303,3,2))
if mibBuilder.loadTexts:pfCopy.setRevisions(('2011-01-11 17:35','2009-03-23 11:17','2008-09-10 15:38'))
_PfCopyNextState_Type=Unsigned32
_PfCopyNextState_Object=MibScalar
pfCopyNextState=_PfCopyNextState_Object((1,3,6,1,4,1,9303,3,2,1),_PfCopyNextState_Type())
pfCopyNextState.setMaxAccess(_C)
if mibBuilder.loadTexts:pfCopyNextState.setStatus(_A)
_PfCopyTable_Object=MibTable
pfCopyTable=_PfCopyTable_Object((1,3,6,1,4,1,9303,3,2,2))
if mibBuilder.loadTexts:pfCopyTable.setStatus(_A)
_PfCopyEntry_Object=MibTableRow
pfCopyEntry=_PfCopyEntry_Object((1,3,6,1,4,1,9303,3,2,2,1))
pfCopyEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pfCopyEntry.setStatus(_A)
_PfCopyIndex_Type=Unsigned32
_PfCopyIndex_Object=MibTableColumn
pfCopyIndex=_PfCopyIndex_Object((1,3,6,1,4,1,9303,3,2,2,1,1),_PfCopyIndex_Type())
pfCopyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pfCopyIndex.setStatus(_A)
class _PfCopySource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PfCopySource_Type.__name__=_B
_PfCopySource_Object=MibTableColumn
pfCopySource=_PfCopySource_Object((1,3,6,1,4,1,9303,3,2,2,1,2),_PfCopySource_Type())
pfCopySource.setMaxAccess(_D)
if mibBuilder.loadTexts:pfCopySource.setStatus(_A)
class _PfCopyDestination_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PfCopyDestination_Type.__name__=_B
_PfCopyDestination_Object=MibTableColumn
pfCopyDestination=_PfCopyDestination_Object((1,3,6,1,4,1,9303,3,2,2,1,3),_PfCopyDestination_Type())
pfCopyDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:pfCopyDestination.setStatus(_A)
class _PfCopyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notused',0),('start',1),('stop',2),('destroy',3),('init',4),('inprogress',5),('failed',6),('finished',7)))
_PfCopyStatus_Type.__name__=_E
_PfCopyStatus_Object=MibTableColumn
pfCopyStatus=_PfCopyStatus_Object((1,3,6,1,4,1,9303,3,2,2,1,4),_PfCopyStatus_Type())
pfCopyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pfCopyStatus.setStatus(_A)
class _PfCopyError_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PfCopyError_Type.__name__=_B
_PfCopyError_Object=MibTableColumn
pfCopyError=_PfCopyError_Object((1,3,6,1,4,1,9303,3,2,2,1,5),_PfCopyError_Type())
pfCopyError.setMaxAccess(_C)
if mibBuilder.loadTexts:pfCopyError.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'pfCopy':pfCopy,'pfCopyNextState':pfCopyNextState,'pfCopyTable':pfCopyTable,'pfCopyEntry':pfCopyEntry,_G:pfCopyIndex,'pfCopySource':pfCopySource,'pfCopyDestination':pfCopyDestination,'pfCopyStatus':pfCopyStatus,'pfCopyError':pfCopyError})