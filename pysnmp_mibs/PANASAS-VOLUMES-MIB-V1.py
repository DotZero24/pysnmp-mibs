_D='panVolPath'
_C='PANASAS-VOLUMES-MIB-V1'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
panFs,=mibBuilder.importSymbols('PANASAS-PANFS-MIB-V1','panFs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
panVol=ModuleIdentity((1,3,6,1,4,1,10159,1,3,4))
if mibBuilder.loadTexts:panVol.setRevisions(('2011-04-07 00:00',))
_PanVolTable_Object=MibTable
panVolTable=_PanVolTable_Object((1,3,6,1,4,1,10159,1,3,4,1))
if mibBuilder.loadTexts:panVolTable.setStatus(_A)
_PanVolEntry_Object=MibTableRow
panVolEntry=_PanVolEntry_Object((1,3,6,1,4,1,10159,1,3,4,1,1))
panVolEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:panVolEntry.setStatus(_A)
_PanVolPath_Type=DisplayString
_PanVolPath_Object=MibTableColumn
panVolPath=_PanVolPath_Object((1,3,6,1,4,1,10159,1,3,4,1,1,1),_PanVolPath_Type())
panVolPath.setMaxAccess(_B)
if mibBuilder.loadTexts:panVolPath.setStatus(_A)
_PanVolBladeSet_Type=DisplayString
_PanVolBladeSet_Object=MibTableColumn
panVolBladeSet=_PanVolBladeSet_Object((1,3,6,1,4,1,10159,1,3,4,1,1,2),_PanVolBladeSet_Type())
panVolBladeSet.setMaxAccess(_B)
if mibBuilder.loadTexts:panVolBladeSet.setStatus(_A)
_PanVolSoftQuota_Type=Unsigned32
_PanVolSoftQuota_Object=MibTableColumn
panVolSoftQuota=_PanVolSoftQuota_Object((1,3,6,1,4,1,10159,1,3,4,1,1,3),_PanVolSoftQuota_Type())
panVolSoftQuota.setMaxAccess(_B)
if mibBuilder.loadTexts:panVolSoftQuota.setStatus(_A)
_PanVolHardQuota_Type=Unsigned32
_PanVolHardQuota_Object=MibTableColumn
panVolHardQuota=_PanVolHardQuota_Object((1,3,6,1,4,1,10159,1,3,4,1,1,4),_PanVolHardQuota_Type())
panVolHardQuota.setMaxAccess(_B)
if mibBuilder.loadTexts:panVolHardQuota.setStatus(_A)
_PanVolUsed_Type=Unsigned32
_PanVolUsed_Object=MibTableColumn
panVolUsed=_PanVolUsed_Object((1,3,6,1,4,1,10159,1,3,4,1,1,5),_PanVolUsed_Type())
panVolUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:panVolUsed.setStatus(_A)
_PanVolRaid_Type=DisplayString
_PanVolRaid_Object=MibTableColumn
panVolRaid=_PanVolRaid_Object((1,3,6,1,4,1,10159,1,3,4,1,1,6),_PanVolRaid_Type())
panVolRaid.setMaxAccess(_B)
if mibBuilder.loadTexts:panVolRaid.setStatus(_A)
_PanVolInfo_Type=DisplayString
_PanVolInfo_Object=MibTableColumn
panVolInfo=_PanVolInfo_Object((1,3,6,1,4,1,10159,1,3,4,1,1,7),_PanVolInfo_Type())
panVolInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:panVolInfo.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'panVol':panVol,'panVolTable':panVolTable,'panVolEntry':panVolEntry,_D:panVolPath,'panVolBladeSet':panVolBladeSet,'panVolSoftQuota':panVolSoftQuota,'panVolHardQuota':panVolHardQuota,'panVolUsed':panVolUsed,'panVolRaid':panVolRaid,'panVolInfo':panVolInfo})