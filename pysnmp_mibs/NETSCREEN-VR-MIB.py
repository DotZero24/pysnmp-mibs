_D='NETSCREEN-VR-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVR,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVR')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
netscreenVRMibModule=ModuleIdentity((1,3,6,1,4,1,3224,18,0))
if mibBuilder.loadTexts:netscreenVRMibModule.setRevisions(('2004-05-03 00:00','2001-09-01 00:00'))
_VrTable_Object=MibTable
vrTable=_VrTable_Object((1,3,6,1,4,1,3224,18,1))
if mibBuilder.loadTexts:vrTable.setStatus(_A)
_VrEntry_Object=MibTableRow
vrEntry=_VrEntry_Object((1,3,6,1,4,1,3224,18,1,1))
vrEntry.setIndexNames((0,_D,'vrId'))
if mibBuilder.loadTexts:vrEntry.setStatus(_A)
_VrName_Type=OctetString
_VrName_Object=MibTableColumn
vrName=_VrName_Object((1,3,6,1,4,1,3224,18,1,1,1),_VrName_Type())
vrName.setMaxAccess(_B)
if mibBuilder.loadTexts:vrName.setStatus(_A)
class _VrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VrId_Type.__name__=_C
_VrId_Object=MibTableColumn
vrId=_VrId_Object((1,3,6,1,4,1,3224,18,1,1,2),_VrId_Type())
vrId.setMaxAccess(_B)
if mibBuilder.loadTexts:vrId.setStatus(_A)
_VrVsysName_Type=OctetString
_VrVsysName_Object=MibTableColumn
vrVsysName=_VrVsysName_Object((1,3,6,1,4,1,3224,18,1,1,3),_VrVsysName_Type())
vrVsysName.setMaxAccess(_B)
if mibBuilder.loadTexts:vrVsysName.setStatus(_A)
_VrRouteId_Type=Integer32
_VrRouteId_Object=MibTableColumn
vrRouteId=_VrRouteId_Object((1,3,6,1,4,1,3224,18,1,1,4),_VrRouteId_Type())
vrRouteId.setMaxAccess(_B)
if mibBuilder.loadTexts:vrRouteId.setStatus(_A)
_VrMaxRoutes_Type=Integer32
_VrMaxRoutes_Object=MibTableColumn
vrMaxRoutes=_VrMaxRoutes_Object((1,3,6,1,4,1,3224,18,1,1,5),_VrMaxRoutes_Type())
vrMaxRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vrMaxRoutes.setStatus(_A)
_VrNumRoutes_Type=Integer32
_VrNumRoutes_Object=MibTableColumn
vrNumRoutes=_VrNumRoutes_Object((1,3,6,1,4,1,3224,18,1,1,6),_VrNumRoutes_Type())
vrNumRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vrNumRoutes.setStatus(_A)
_VrSharable_Type=Integer32
_VrSharable_Object=MibTableColumn
vrSharable=_VrSharable_Object((1,3,6,1,4,1,3224,18,1,1,7),_VrSharable_Type())
vrSharable.setMaxAccess(_B)
if mibBuilder.loadTexts:vrSharable.setStatus(_A)
_VrOspfRipBgpEnabled_Type=Integer32
_VrOspfRipBgpEnabled_Object=MibTableColumn
vrOspfRipBgpEnabled=_VrOspfRipBgpEnabled_Object((1,3,6,1,4,1,3224,18,1,1,8),_VrOspfRipBgpEnabled_Type())
vrOspfRipBgpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:vrOspfRipBgpEnabled.setStatus(_A)
_VrTrapPrivate_Type=Integer32
_VrTrapPrivate_Object=MibTableColumn
vrTrapPrivate=_VrTrapPrivate_Object((1,3,6,1,4,1,3224,18,1,1,9),_VrTrapPrivate_Type())
vrTrapPrivate.setMaxAccess(_B)
if mibBuilder.loadTexts:vrTrapPrivate.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'netscreenVRMibModule':netscreenVRMibModule,'vrTable':vrTable,'vrEntry':vrEntry,'vrName':vrName,'vrId':vrId,'vrVsysName':vrVsysName,'vrRouteId':vrRouteId,'vrMaxRoutes':vrMaxRoutes,'vrNumRoutes':vrNumRoutes,'vrSharable':vrSharable,'vrOspfRipBgpEnabled':vrOspfRipBgpEnabled,'vrTrapPrivate':vrTrapPrivate})