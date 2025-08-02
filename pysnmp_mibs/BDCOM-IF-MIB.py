_G='testing'
_F='vifIndex'
_E='BDCOM-IF-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bdMgmt,=mibBuilder.importSymbols('BDCOM-SMI','bdMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
bdIfMIB=ModuleIdentity((1,3,6,1,4,1,3320,9,63))
_BdIfObjects_ObjectIdentity=ObjectIdentity
bdIfObjects=_BdIfObjects_ObjectIdentity((1,3,6,1,4,1,3320,9,63,1))
_VifTable_Object=MibTable
vifTable=_VifTable_Object((1,3,6,1,4,1,3320,9,63,1,1))
if mibBuilder.loadTexts:vifTable.setStatus(_A)
_VifEntry_Object=MibTableRow
vifEntry=_VifEntry_Object((1,3,6,1,4,1,3320,9,63,1,1,1))
vifEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:vifEntry.setStatus(_A)
_VifIndex_Type=Integer32
_VifIndex_Object=MibTableColumn
vifIndex=_VifIndex_Object((1,3,6,1,4,1,3320,9,63,1,1,1,1),_VifIndex_Type())
vifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vifIndex.setStatus(_A)
class _VifDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VifDescr_Type.__name__=_D
_VifDescr_Object=MibTableColumn
vifDescr=_VifDescr_Object((1,3,6,1,4,1,3320,9,63,1,1,1,2),_VifDescr_Type())
vifDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:vifDescr.setStatus(_A)
class _VifType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,100,101,102)));namedValues=NamedValues(*(('other',1),('voiceEM',100),('voiceFXO',101),('voiceFXS',102)))
_VifType_Type.__name__=_C
_VifType_Object=MibTableColumn
vifType=_VifType_Object((1,3,6,1,4,1,3320,9,63,1,1,1,3),_VifType_Type())
vifType.setMaxAccess(_B)
if mibBuilder.loadTexts:vifType.setStatus(_A)
_VifMtu_Type=Integer32
_VifMtu_Object=MibTableColumn
vifMtu=_VifMtu_Object((1,3,6,1,4,1,3320,9,63,1,1,1,4),_VifMtu_Type())
vifMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:vifMtu.setStatus(_A)
_VifSpeed_Type=Gauge32
_VifSpeed_Object=MibTableColumn
vifSpeed=_VifSpeed_Object((1,3,6,1,4,1,3320,9,63,1,1,1,5),_VifSpeed_Type())
vifSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:vifSpeed.setStatus(_A)
_VifPhysAddress_Type=PhysAddress
_VifPhysAddress_Object=MibTableColumn
vifPhysAddress=_VifPhysAddress_Object((1,3,6,1,4,1,3320,9,63,1,1,1,6),_VifPhysAddress_Type())
vifPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vifPhysAddress.setStatus(_A)
class _VifAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_G,3)))
_VifAdminStatus_Type.__name__=_C
_VifAdminStatus_Object=MibTableColumn
vifAdminStatus=_VifAdminStatus_Object((1,3,6,1,4,1,3320,9,63,1,1,1,7),_VifAdminStatus_Type())
vifAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:vifAdminStatus.setStatus(_A)
class _VifOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),('down',2),(_G,3),('unknown',4),('dormant',5)))
_VifOperStatus_Type.__name__=_C
_VifOperStatus_Object=MibTableColumn
vifOperStatus=_VifOperStatus_Object((1,3,6,1,4,1,3320,9,63,1,1,1,8),_VifOperStatus_Type())
vifOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vifOperStatus.setStatus(_A)
_VifLastChange_Type=TimeTicks
_VifLastChange_Object=MibTableColumn
vifLastChange=_VifLastChange_Object((1,3,6,1,4,1,3320,9,63,1,1,1,9),_VifLastChange_Type())
vifLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:vifLastChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bdIfMIB':bdIfMIB,'bdIfObjects':bdIfObjects,'vifTable':vifTable,'vifEntry':vifEntry,_F:vifIndex,'vifDescr':vifDescr,'vifType':vifType,'vifMtu':vifMtu,'vifSpeed':vifSpeed,'vifPhysAddress':vifPhysAddress,'vifAdminStatus':vifAdminStatus,'vifOperStatus':vifOperStatus,'vifLastChange':vifLastChange})