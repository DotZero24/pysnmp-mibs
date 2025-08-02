_F='read-only'
_E='read-write'
_D='ifIndex'
_C='IF-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenRemoteDownload,adGenRemoteDownloadID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenRemoteDownload','adGenRemoteDownloadID')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenRemoteDownloadMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,33,1))
_AdGenRemoteDownloadProvisioning_ObjectIdentity=ObjectIdentity
adGenRemoteDownloadProvisioning=_AdGenRemoteDownloadProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,33,1))
_AdGenRemoteDownloadProvTable_Object=MibTable
adGenRemoteDownloadProvTable=_AdGenRemoteDownloadProvTable_Object((1,3,6,1,4,1,664,5,70,33,1,1))
if mibBuilder.loadTexts:adGenRemoteDownloadProvTable.setStatus(_A)
_AdGenRemoteDownloadProvEntry_Object=MibTableRow
adGenRemoteDownloadProvEntry=_AdGenRemoteDownloadProvEntry_Object((1,3,6,1,4,1,664,5,70,33,1,1,1))
adGenRemoteDownloadProvEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenRemoteDownloadProvEntry.setStatus(_A)
_AdGenRemoteDownloadFilename_Type=DisplayString
_AdGenRemoteDownloadFilename_Object=MibTableColumn
adGenRemoteDownloadFilename=_AdGenRemoteDownloadFilename_Object((1,3,6,1,4,1,664,5,70,33,1,1,1,1),_AdGenRemoteDownloadFilename_Type())
adGenRemoteDownloadFilename.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenRemoteDownloadFilename.setStatus(_A)
class _AdGenRemoteDownloadInitiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('initiate',1))
_AdGenRemoteDownloadInitiate_Type.__name__=_B
_AdGenRemoteDownloadInitiate_Object=MibTableColumn
adGenRemoteDownloadInitiate=_AdGenRemoteDownloadInitiate_Object((1,3,6,1,4,1,664,5,70,33,1,1,1,2),_AdGenRemoteDownloadInitiate_Type())
adGenRemoteDownloadInitiate.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenRemoteDownloadInitiate.setStatus(_A)
class _AdGenRemoteDownloadReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reboot',1))
_AdGenRemoteDownloadReboot_Type.__name__=_B
_AdGenRemoteDownloadReboot_Object=MibTableColumn
adGenRemoteDownloadReboot=_AdGenRemoteDownloadReboot_Object((1,3,6,1,4,1,664,5,70,33,1,1,1,3),_AdGenRemoteDownloadReboot_Type())
adGenRemoteDownloadReboot.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenRemoteDownloadReboot.setStatus(_A)
_AdGenRemoteDownloadStatus_ObjectIdentity=ObjectIdentity
adGenRemoteDownloadStatus=_AdGenRemoteDownloadStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,33,2))
_AdGenRemoteDownloadStatusTable_Object=MibTable
adGenRemoteDownloadStatusTable=_AdGenRemoteDownloadStatusTable_Object((1,3,6,1,4,1,664,5,70,33,2,1))
if mibBuilder.loadTexts:adGenRemoteDownloadStatusTable.setStatus(_A)
_AdGenRemoteDownloadStatusEntry_Object=MibTableRow
adGenRemoteDownloadStatusEntry=_AdGenRemoteDownloadStatusEntry_Object((1,3,6,1,4,1,664,5,70,33,2,1,1))
adGenRemoteDownloadStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenRemoteDownloadStatusEntry.setStatus(_A)
class _AdGenRemoteDownloadStatusSummary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('inProgress',2),('error',3),('success',4)))
_AdGenRemoteDownloadStatusSummary_Type.__name__=_B
_AdGenRemoteDownloadStatusSummary_Object=MibTableColumn
adGenRemoteDownloadStatusSummary=_AdGenRemoteDownloadStatusSummary_Object((1,3,6,1,4,1,664,5,70,33,2,1,1,1),_AdGenRemoteDownloadStatusSummary_Type())
adGenRemoteDownloadStatusSummary.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenRemoteDownloadStatusSummary.setStatus(_A)
_AdGenRemoteDownloadStatusString_Type=DisplayString
_AdGenRemoteDownloadStatusString_Object=MibTableColumn
adGenRemoteDownloadStatusString=_AdGenRemoteDownloadStatusString_Object((1,3,6,1,4,1,664,5,70,33,2,1,1,2),_AdGenRemoteDownloadStatusString_Type())
adGenRemoteDownloadStatusString.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenRemoteDownloadStatusString.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GENREMOTEDOWNLOAD-MIB',**{'adGenRemoteDownloadProvisioning':adGenRemoteDownloadProvisioning,'adGenRemoteDownloadProvTable':adGenRemoteDownloadProvTable,'adGenRemoteDownloadProvEntry':adGenRemoteDownloadProvEntry,'adGenRemoteDownloadFilename':adGenRemoteDownloadFilename,'adGenRemoteDownloadInitiate':adGenRemoteDownloadInitiate,'adGenRemoteDownloadReboot':adGenRemoteDownloadReboot,'adGenRemoteDownloadStatus':adGenRemoteDownloadStatus,'adGenRemoteDownloadStatusTable':adGenRemoteDownloadStatusTable,'adGenRemoteDownloadStatusEntry':adGenRemoteDownloadStatusEntry,'adGenRemoteDownloadStatusSummary':adGenRemoteDownloadStatusSummary,'adGenRemoteDownloadStatusString':adGenRemoteDownloadStatusString,'adGenRemoteDownloadMIB':adGenRemoteDownloadMIB})