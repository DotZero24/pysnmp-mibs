_G='notAllowed'
_F='sfpsSizeServiceName'
_E='CTRON-SFPS-SIZE-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsSizeService,sfpsSizeServiceAPI=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsSizeService','sfpsSizeServiceAPI')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_SfpsSizeServiceTable_Object=MibTable
sfpsSizeServiceTable=_SfpsSizeServiceTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1))
if mibBuilder.loadTexts:sfpsSizeServiceTable.setStatus(_A)
_SfpsSizeServiceEntry_Object=MibTableRow
sfpsSizeServiceEntry=_SfpsSizeServiceEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1))
sfpsSizeServiceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sfpsSizeServiceEntry.setStatus(_A)
_SfpsSizeServiceName_Type=DisplayString
_SfpsSizeServiceName_Object=MibTableColumn
sfpsSizeServiceName=_SfpsSizeServiceName_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1,1),_SfpsSizeServiceName_Type())
sfpsSizeServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceName.setStatus(_A)
_SfpsSizeServiceId_Type=Integer32
_SfpsSizeServiceId_Object=MibTableColumn
sfpsSizeServiceId=_SfpsSizeServiceId_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1,2),_SfpsSizeServiceId_Type())
sfpsSizeServiceId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceId.setStatus(_A)
_SfpsSizeServiceElemSize_Type=Integer32
_SfpsSizeServiceElemSize_Object=MibTableColumn
sfpsSizeServiceElemSize=_SfpsSizeServiceElemSize_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1,3),_SfpsSizeServiceElemSize_Type())
sfpsSizeServiceElemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceElemSize.setStatus(_A)
_SfpsSizeServiceDesired_Type=Integer32
_SfpsSizeServiceDesired_Object=MibTableColumn
sfpsSizeServiceDesired=_SfpsSizeServiceDesired_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1,4),_SfpsSizeServiceDesired_Type())
sfpsSizeServiceDesired.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceDesired.setStatus(_A)
_SfpsSizeServiceGranted_Type=Integer32
_SfpsSizeServiceGranted_Object=MibTableColumn
sfpsSizeServiceGranted=_SfpsSizeServiceGranted_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1,5),_SfpsSizeServiceGranted_Type())
sfpsSizeServiceGranted.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceGranted.setStatus(_A)
_SfpsSizeServiceIncrement_Type=Integer32
_SfpsSizeServiceIncrement_Object=MibTableColumn
sfpsSizeServiceIncrement=_SfpsSizeServiceIncrement_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1,6),_SfpsSizeServiceIncrement_Type())
sfpsSizeServiceIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceIncrement.setStatus(_A)
_SfpsSizeServiceTotalBytes_Type=Integer32
_SfpsSizeServiceTotalBytes_Object=MibTableColumn
sfpsSizeServiceTotalBytes=_SfpsSizeServiceTotalBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1,7),_SfpsSizeServiceTotalBytes_Type())
sfpsSizeServiceTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceTotalBytes.setStatus(_A)
_SfpsSizeServiceNbrCalls_Type=Integer32
_SfpsSizeServiceNbrCalls_Object=MibTableColumn
sfpsSizeServiceNbrCalls=_SfpsSizeServiceNbrCalls_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1,8),_SfpsSizeServiceNbrCalls_Type())
sfpsSizeServiceNbrCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceNbrCalls.setStatus(_A)
class _SfpsSizeServiceRtnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ok',1),('nvramOk',2),('unknown',3),(_G,4),('nonApiOk',5)))
_SfpsSizeServiceRtnStatus_Type.__name__=_D
_SfpsSizeServiceRtnStatus_Object=MibTableColumn
sfpsSizeServiceRtnStatus=_SfpsSizeServiceRtnStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1,9),_SfpsSizeServiceRtnStatus_Type())
sfpsSizeServiceRtnStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceRtnStatus.setStatus(_A)
class _SfpsSizeServiceHowGranted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('elements',1),('memory',2),('other',3),(_G,4)))
_SfpsSizeServiceHowGranted_Type.__name__=_D
_SfpsSizeServiceHowGranted_Object=MibTableColumn
sfpsSizeServiceHowGranted=_SfpsSizeServiceHowGranted_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,1,1,1,10),_SfpsSizeServiceHowGranted_Type())
sfpsSizeServiceHowGranted.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceHowGranted.setStatus(_A)
class _SfpsSizeServiceAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('next',2),('prev',3),('set',4),('clear',5),('clearAll',6)))
_SfpsSizeServiceAPIVerb_Type.__name__=_D
_SfpsSizeServiceAPIVerb_Object=MibScalar
sfpsSizeServiceAPIVerb=_SfpsSizeServiceAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,2,1),_SfpsSizeServiceAPIVerb_Type())
sfpsSizeServiceAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSizeServiceAPIVerb.setStatus(_A)
_SfpsSizeServiceAPIName_Type=DisplayString
_SfpsSizeServiceAPIName_Object=MibScalar
sfpsSizeServiceAPIName=_SfpsSizeServiceAPIName_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,2,2),_SfpsSizeServiceAPIName_Type())
sfpsSizeServiceAPIName.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSizeServiceAPIName.setStatus(_A)
_SfpsSizeServiceAPIId_Type=Integer32
_SfpsSizeServiceAPIId_Object=MibScalar
sfpsSizeServiceAPIId=_SfpsSizeServiceAPIId_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,2,3),_SfpsSizeServiceAPIId_Type())
sfpsSizeServiceAPIId.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSizeServiceAPIId.setStatus(_A)
_SfpsSizeServiceAPIGrant_Type=DisplayString
_SfpsSizeServiceAPIGrant_Object=MibScalar
sfpsSizeServiceAPIGrant=_SfpsSizeServiceAPIGrant_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,2,4),_SfpsSizeServiceAPIGrant_Type())
sfpsSizeServiceAPIGrant.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSizeServiceAPIGrant.setStatus(_A)
_SfpsSizeServiceAPIIncrement_Type=Integer32
_SfpsSizeServiceAPIIncrement_Object=MibScalar
sfpsSizeServiceAPIIncrement=_SfpsSizeServiceAPIIncrement_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,2,5),_SfpsSizeServiceAPIIncrement_Type())
sfpsSizeServiceAPIIncrement.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSizeServiceAPIIncrement.setStatus(_A)
_SfpsSizeServiceAPINumberSet_Type=Integer32
_SfpsSizeServiceAPINumberSet_Object=MibScalar
sfpsSizeServiceAPINumberSet=_SfpsSizeServiceAPINumberSet_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,2,6),_SfpsSizeServiceAPINumberSet_Type())
sfpsSizeServiceAPINumberSet.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceAPINumberSet.setStatus(_A)
_SfpsSizeServiceAPIVersion_Type=Integer32
_SfpsSizeServiceAPIVersion_Object=MibScalar
sfpsSizeServiceAPIVersion=_SfpsSizeServiceAPIVersion_Object((1,3,6,1,4,1,52,4,2,4,2,1,14,2,7),_SfpsSizeServiceAPIVersion_Type())
sfpsSizeServiceAPIVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSizeServiceAPIVersion.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'sfpsSizeServiceTable':sfpsSizeServiceTable,'sfpsSizeServiceEntry':sfpsSizeServiceEntry,_F:sfpsSizeServiceName,'sfpsSizeServiceId':sfpsSizeServiceId,'sfpsSizeServiceElemSize':sfpsSizeServiceElemSize,'sfpsSizeServiceDesired':sfpsSizeServiceDesired,'sfpsSizeServiceGranted':sfpsSizeServiceGranted,'sfpsSizeServiceIncrement':sfpsSizeServiceIncrement,'sfpsSizeServiceTotalBytes':sfpsSizeServiceTotalBytes,'sfpsSizeServiceNbrCalls':sfpsSizeServiceNbrCalls,'sfpsSizeServiceRtnStatus':sfpsSizeServiceRtnStatus,'sfpsSizeServiceHowGranted':sfpsSizeServiceHowGranted,'sfpsSizeServiceAPIVerb':sfpsSizeServiceAPIVerb,'sfpsSizeServiceAPIName':sfpsSizeServiceAPIName,'sfpsSizeServiceAPIId':sfpsSizeServiceAPIId,'sfpsSizeServiceAPIGrant':sfpsSizeServiceAPIGrant,'sfpsSizeServiceAPIIncrement':sfpsSizeServiceAPIIncrement,'sfpsSizeServiceAPINumberSet':sfpsSizeServiceAPINumberSet,'sfpsSizeServiceAPIVersion':sfpsSizeServiceAPIVersion})