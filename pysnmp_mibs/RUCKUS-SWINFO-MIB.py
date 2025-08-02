_F='ruckusSwRevIndex'
_E='RUCKUS-SWINFO-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruckusCommonSwInfoModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonSwInfoModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'PhysAddress','TextualConvention','TruthValue')
ruckusSwInfoMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,3,1))
_RuckusSwInfoObjects_ObjectIdentity=ObjectIdentity
ruckusSwInfoObjects=_RuckusSwInfoObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,3,1,1))
_RuckusSwInfo_ObjectIdentity=ObjectIdentity
ruckusSwInfo=_RuckusSwInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,3,1,1,1))
_RuckusSwRevTable_Object=MibTable
ruckusSwRevTable=_RuckusSwRevTable_Object((1,3,6,1,4,1,25053,1,1,3,1,1,1,1))
if mibBuilder.loadTexts:ruckusSwRevTable.setStatus(_A)
_RuckusSwRevEntry_Object=MibTableRow
ruckusSwRevEntry=_RuckusSwRevEntry_Object((1,3,6,1,4,1,25053,1,1,3,1,1,1,1,1))
ruckusSwRevEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ruckusSwRevEntry.setStatus(_A)
class _RuckusSwRevIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RuckusSwRevIndex_Type.__name__=_C
_RuckusSwRevIndex_Object=MibTableColumn
ruckusSwRevIndex=_RuckusSwRevIndex_Object((1,3,6,1,4,1,25053,1,1,3,1,1,1,1,1,1),_RuckusSwRevIndex_Type())
ruckusSwRevIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSwRevIndex.setStatus(_A)
class _RuckusSwRevName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusSwRevName_Type.__name__=_D
_RuckusSwRevName_Object=MibTableColumn
ruckusSwRevName=_RuckusSwRevName_Object((1,3,6,1,4,1,25053,1,1,3,1,1,1,1,1,2),_RuckusSwRevName_Type())
ruckusSwRevName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSwRevName.setStatus(_A)
class _RuckusSwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusSwRevision_Type.__name__=_D
_RuckusSwRevision_Object=MibTableColumn
ruckusSwRevision=_RuckusSwRevision_Object((1,3,6,1,4,1,25053,1,1,3,1,1,1,1,1,3),_RuckusSwRevision_Type())
ruckusSwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSwRevision.setStatus(_A)
_RuckusSwRevSize_Type=Unsigned32
_RuckusSwRevSize_Object=MibTableColumn
ruckusSwRevSize=_RuckusSwRevSize_Object((1,3,6,1,4,1,25053,1,1,3,1,1,1,1,1,4),_RuckusSwRevSize_Type())
ruckusSwRevSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSwRevSize.setStatus(_A)
class _RuckusSwRevStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
_RuckusSwRevStatus_Type.__name__=_C
_RuckusSwRevStatus_Object=MibTableColumn
ruckusSwRevStatus=_RuckusSwRevStatus_Object((1,3,6,1,4,1,25053,1,1,3,1,1,1,1,1,5),_RuckusSwRevStatus_Type())
ruckusSwRevStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSwRevStatus.setStatus(_A)
_RuckusSwInfoEvents_ObjectIdentity=ObjectIdentity
ruckusSwInfoEvents=_RuckusSwInfoEvents_ObjectIdentity((1,3,6,1,4,1,25053,1,1,3,1,2))
mibBuilder.exportSymbols(_E,**{'ruckusSwInfoMIB':ruckusSwInfoMIB,'ruckusSwInfoObjects':ruckusSwInfoObjects,'ruckusSwInfo':ruckusSwInfo,'ruckusSwRevTable':ruckusSwRevTable,'ruckusSwRevEntry':ruckusSwRevEntry,_F:ruckusSwRevIndex,'ruckusSwRevName':ruckusSwRevName,'ruckusSwRevision':ruckusSwRevision,'ruckusSwRevSize':ruckusSwRevSize,'ruckusSwRevStatus':ruckusSwRevStatus,'ruckusSwInfoEvents':ruckusSwInfoEvents})