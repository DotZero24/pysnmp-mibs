_A6='rbnEspuSgiApnGroup'
_A5='rbnEpsuSgiGroup'
_A4='rbnEpsuPgwGtpGroup'
_A3='rbnEpsuSgwGtpGroup'
_A2='rbnEpsuS1uGtpGroup'
_A1='rbnEpsuSgiApnUlPktsDropped'
_A0='rbnEpsuSgiApnUlV6OctetsSent'
_z='rbnEpsuSgiApnUlV6PktsSent'
_y='rbnEpsuSgiApnUlOctetsSent'
_x='rbnEpsuSgiApnUlPktsSent'
_w='rbnEpsuSgiApnDlPktsDiscarded'
_v='rbnEpsuSgiApnDlV6OctetsRcvd'
_u='rbnEpsuSgiApnDlV6PktsRcvd'
_t='rbnEpsuSgiApnDlOctetsRcvd'
_s='rbnEpsuSgiApnDlPktsRcvd'
_r='rbnEpsuSgiApnName'
_q='rbnEpsuSgiUlV6OctetsSent'
_p='rbnEpsuSgiUlV6PktsSent'
_o='rbnEpsuSgiUlPktsDropped'
_n='rbnEpsuSgiUlOctetsSent'
_m='rbnEpsuSgiUlPktsSent'
_l='rbnEpsuSgiDlPktsDiscarded'
_k='rbnEpsuSgiDlV6OctetsRcvd'
_j='rbnEpsuSgiDlV6PktsRcvd'
_i='rbnEpsuSgiDlOctetsRcvd'
_h='rbnEpsuSgiDlPktsRcvd'
_g='rbnEpsuS5S8GtpUlPolicingPktsDiscarded'
_f='rbnEpsuS5S8GtpUlBearerPktsDiscarded'
_e='rbnEpsuS5S8GtpUlPktsDiscarded'
_d='rbnEpsuS5S8GtpUlOctetsRcvd'
_c='rbnEpsuS5S8GtpUlPktsRcvd'
_b='rbnEpsuS5S8GtpDlPolicingPktsDropped'
_a='rbnEpsuS5S8GtpDlPktsDropped'
_Z='rbnEpsuS5S8GtpDlOctetsSent'
_Y='rbnEpsuS5S8GtpDlPktsSent'
_X='rbnEpsuS5S8GtpUlPktsDropped'
_W='rbnEpsuS5S8GtpUlOctetsSent'
_V='rbnEpsuS5S8GtpUlPktsSent'
_U='rbnEpsuS5S8GtpDlPktsDiscarded'
_T='rbnEpsuS5S8GtpDlOctetsRcvd'
_S='rbnEpsuS5S8GtpDlPktsRcvd'
_R='rbnEpsuS1uUlPolicingPktsDiscarded'
_Q='rbnEpsuS1uUlBearerPktsDiscarded'
_P='rbnEpsuS1uUlPktsDiscarded'
_O='rbnEpsuS1uUlOctetsRcvd'
_N='rbnEpsuS1uUlPktsRcvd'
_M='rbnEpsuS1uDlUeIdlePktsDropped'
_L='rbnEpsuS1uDlPolicingPktsDropped'
_K='rbnEpsuS1uDlPktsDropped'
_J='rbnEpsuS1uDlOctetsSent'
_I='rbnEpsuS1uDlPktsSent'
_H='rbnEpsuSgiApnIndex'
_G='Unsigned32'
_F='SnmpAdminString'
_E='Octets'
_D='Packets'
_C='read-only'
_B='RBN-EPSU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnEpsuMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,47))
if mibBuilder.loadTexts:rbnEpsuMIB.setRevisions(('2009-09-23 12:00',))
_RbnEpsuNotifcationGroup_ObjectIdentity=ObjectIdentity
rbnEpsuNotifcationGroup=_RbnEpsuNotifcationGroup_ObjectIdentity((1,3,6,1,4,1,2352,2,47,0))
_RbnEpsuStatMIBObjects_ObjectIdentity=ObjectIdentity
rbnEpsuStatMIBObjects=_RbnEpsuStatMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,47,1))
_RbnEpsuS1uGtp_ObjectIdentity=ObjectIdentity
rbnEpsuS1uGtp=_RbnEpsuS1uGtp_ObjectIdentity((1,3,6,1,4,1,2352,2,47,1,1))
_RbnEpsuS1uDlPktsSent_Type=Counter64
_RbnEpsuS1uDlPktsSent_Object=MibScalar
rbnEpsuS1uDlPktsSent=_RbnEpsuS1uDlPktsSent_Object((1,3,6,1,4,1,2352,2,47,1,1,1),_RbnEpsuS1uDlPktsSent_Type())
rbnEpsuS1uDlPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS1uDlPktsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS1uDlPktsSent.setUnits(_D)
_RbnEpsuS1uDlOctetsSent_Type=Counter64
_RbnEpsuS1uDlOctetsSent_Object=MibScalar
rbnEpsuS1uDlOctetsSent=_RbnEpsuS1uDlOctetsSent_Object((1,3,6,1,4,1,2352,2,47,1,1,2),_RbnEpsuS1uDlOctetsSent_Type())
rbnEpsuS1uDlOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS1uDlOctetsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS1uDlOctetsSent.setUnits(_E)
_RbnEpsuS1uDlPktsDropped_Type=Counter64
_RbnEpsuS1uDlPktsDropped_Object=MibScalar
rbnEpsuS1uDlPktsDropped=_RbnEpsuS1uDlPktsDropped_Object((1,3,6,1,4,1,2352,2,47,1,1,3),_RbnEpsuS1uDlPktsDropped_Type())
rbnEpsuS1uDlPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS1uDlPktsDropped.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS1uDlPktsDropped.setUnits(_D)
_RbnEpsuS1uDlPolicingPktsDropped_Type=Counter64
_RbnEpsuS1uDlPolicingPktsDropped_Object=MibScalar
rbnEpsuS1uDlPolicingPktsDropped=_RbnEpsuS1uDlPolicingPktsDropped_Object((1,3,6,1,4,1,2352,2,47,1,1,4),_RbnEpsuS1uDlPolicingPktsDropped_Type())
rbnEpsuS1uDlPolicingPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS1uDlPolicingPktsDropped.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS1uDlPolicingPktsDropped.setUnits(_D)
_RbnEpsuS1uDlUeIdlePktsDropped_Type=Counter64
_RbnEpsuS1uDlUeIdlePktsDropped_Object=MibScalar
rbnEpsuS1uDlUeIdlePktsDropped=_RbnEpsuS1uDlUeIdlePktsDropped_Object((1,3,6,1,4,1,2352,2,47,1,1,5),_RbnEpsuS1uDlUeIdlePktsDropped_Type())
rbnEpsuS1uDlUeIdlePktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS1uDlUeIdlePktsDropped.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS1uDlUeIdlePktsDropped.setUnits(_D)
_RbnEpsuS1uUlPktsRcvd_Type=Counter64
_RbnEpsuS1uUlPktsRcvd_Object=MibScalar
rbnEpsuS1uUlPktsRcvd=_RbnEpsuS1uUlPktsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,1,6),_RbnEpsuS1uUlPktsRcvd_Type())
rbnEpsuS1uUlPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS1uUlPktsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS1uUlPktsRcvd.setUnits(_D)
_RbnEpsuS1uUlOctetsRcvd_Type=Counter64
_RbnEpsuS1uUlOctetsRcvd_Object=MibScalar
rbnEpsuS1uUlOctetsRcvd=_RbnEpsuS1uUlOctetsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,1,7),_RbnEpsuS1uUlOctetsRcvd_Type())
rbnEpsuS1uUlOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS1uUlOctetsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS1uUlOctetsRcvd.setUnits(_E)
_RbnEpsuS1uUlPktsDiscarded_Type=Counter64
_RbnEpsuS1uUlPktsDiscarded_Object=MibScalar
rbnEpsuS1uUlPktsDiscarded=_RbnEpsuS1uUlPktsDiscarded_Object((1,3,6,1,4,1,2352,2,47,1,1,8),_RbnEpsuS1uUlPktsDiscarded_Type())
rbnEpsuS1uUlPktsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS1uUlPktsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS1uUlPktsDiscarded.setUnits(_D)
_RbnEpsuS1uUlBearerPktsDiscarded_Type=Counter64
_RbnEpsuS1uUlBearerPktsDiscarded_Object=MibScalar
rbnEpsuS1uUlBearerPktsDiscarded=_RbnEpsuS1uUlBearerPktsDiscarded_Object((1,3,6,1,4,1,2352,2,47,1,1,9),_RbnEpsuS1uUlBearerPktsDiscarded_Type())
rbnEpsuS1uUlBearerPktsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS1uUlBearerPktsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS1uUlBearerPktsDiscarded.setUnits(_D)
_RbnEpsuS1uUlPolicingPktsDiscarded_Type=Counter64
_RbnEpsuS1uUlPolicingPktsDiscarded_Object=MibScalar
rbnEpsuS1uUlPolicingPktsDiscarded=_RbnEpsuS1uUlPolicingPktsDiscarded_Object((1,3,6,1,4,1,2352,2,47,1,1,10),_RbnEpsuS1uUlPolicingPktsDiscarded_Type())
rbnEpsuS1uUlPolicingPktsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS1uUlPolicingPktsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS1uUlPolicingPktsDiscarded.setUnits(_D)
_RbnEpsuSgwGtp_ObjectIdentity=ObjectIdentity
rbnEpsuSgwGtp=_RbnEpsuSgwGtp_ObjectIdentity((1,3,6,1,4,1,2352,2,47,1,2))
_RbnEpsuS5S8GtpDlPktsRcvd_Type=Counter64
_RbnEpsuS5S8GtpDlPktsRcvd_Object=MibScalar
rbnEpsuS5S8GtpDlPktsRcvd=_RbnEpsuS5S8GtpDlPktsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,2,1),_RbnEpsuS5S8GtpDlPktsRcvd_Type())
rbnEpsuS5S8GtpDlPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlPktsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlPktsRcvd.setUnits(_D)
_RbnEpsuS5S8GtpDlOctetsRcvd_Type=Counter64
_RbnEpsuS5S8GtpDlOctetsRcvd_Object=MibScalar
rbnEpsuS5S8GtpDlOctetsRcvd=_RbnEpsuS5S8GtpDlOctetsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,2,2),_RbnEpsuS5S8GtpDlOctetsRcvd_Type())
rbnEpsuS5S8GtpDlOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlOctetsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlOctetsRcvd.setUnits(_E)
_RbnEpsuS5S8GtpDlPktsDiscarded_Type=Counter64
_RbnEpsuS5S8GtpDlPktsDiscarded_Object=MibScalar
rbnEpsuS5S8GtpDlPktsDiscarded=_RbnEpsuS5S8GtpDlPktsDiscarded_Object((1,3,6,1,4,1,2352,2,47,1,2,3),_RbnEpsuS5S8GtpDlPktsDiscarded_Type())
rbnEpsuS5S8GtpDlPktsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlPktsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlPktsDiscarded.setUnits(_D)
_RbnEpsuS5S8GtpUlPktsSent_Type=Counter64
_RbnEpsuS5S8GtpUlPktsSent_Object=MibScalar
rbnEpsuS5S8GtpUlPktsSent=_RbnEpsuS5S8GtpUlPktsSent_Object((1,3,6,1,4,1,2352,2,47,1,2,4),_RbnEpsuS5S8GtpUlPktsSent_Type())
rbnEpsuS5S8GtpUlPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlPktsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlPktsSent.setUnits(_D)
_RbnEpsuS5S8GtpUlOctetsSent_Type=Counter64
_RbnEpsuS5S8GtpUlOctetsSent_Object=MibScalar
rbnEpsuS5S8GtpUlOctetsSent=_RbnEpsuS5S8GtpUlOctetsSent_Object((1,3,6,1,4,1,2352,2,47,1,2,5),_RbnEpsuS5S8GtpUlOctetsSent_Type())
rbnEpsuS5S8GtpUlOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlOctetsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlOctetsSent.setUnits(_E)
_RbnEpsuS5S8GtpUlPktsDropped_Type=Counter64
_RbnEpsuS5S8GtpUlPktsDropped_Object=MibScalar
rbnEpsuS5S8GtpUlPktsDropped=_RbnEpsuS5S8GtpUlPktsDropped_Object((1,3,6,1,4,1,2352,2,47,1,2,6),_RbnEpsuS5S8GtpUlPktsDropped_Type())
rbnEpsuS5S8GtpUlPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlPktsDropped.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlPktsDropped.setUnits(_D)
_RbnEpsuPgwGtp_ObjectIdentity=ObjectIdentity
rbnEpsuPgwGtp=_RbnEpsuPgwGtp_ObjectIdentity((1,3,6,1,4,1,2352,2,47,1,3))
_RbnEpsuS5S8GtpDlPktsSent_Type=Counter64
_RbnEpsuS5S8GtpDlPktsSent_Object=MibScalar
rbnEpsuS5S8GtpDlPktsSent=_RbnEpsuS5S8GtpDlPktsSent_Object((1,3,6,1,4,1,2352,2,47,1,3,1),_RbnEpsuS5S8GtpDlPktsSent_Type())
rbnEpsuS5S8GtpDlPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlPktsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlPktsSent.setUnits(_D)
_RbnEpsuS5S8GtpDlOctetsSent_Type=Counter64
_RbnEpsuS5S8GtpDlOctetsSent_Object=MibScalar
rbnEpsuS5S8GtpDlOctetsSent=_RbnEpsuS5S8GtpDlOctetsSent_Object((1,3,6,1,4,1,2352,2,47,1,3,2),_RbnEpsuS5S8GtpDlOctetsSent_Type())
rbnEpsuS5S8GtpDlOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlOctetsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlOctetsSent.setUnits(_E)
_RbnEpsuS5S8GtpDlPktsDropped_Type=Counter64
_RbnEpsuS5S8GtpDlPktsDropped_Object=MibScalar
rbnEpsuS5S8GtpDlPktsDropped=_RbnEpsuS5S8GtpDlPktsDropped_Object((1,3,6,1,4,1,2352,2,47,1,3,3),_RbnEpsuS5S8GtpDlPktsDropped_Type())
rbnEpsuS5S8GtpDlPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlPktsDropped.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlPktsDropped.setUnits(_D)
_RbnEpsuS5S8GtpDlPolicingPktsDropped_Type=Counter64
_RbnEpsuS5S8GtpDlPolicingPktsDropped_Object=MibScalar
rbnEpsuS5S8GtpDlPolicingPktsDropped=_RbnEpsuS5S8GtpDlPolicingPktsDropped_Object((1,3,6,1,4,1,2352,2,47,1,3,4),_RbnEpsuS5S8GtpDlPolicingPktsDropped_Type())
rbnEpsuS5S8GtpDlPolicingPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlPolicingPktsDropped.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpDlPolicingPktsDropped.setUnits(_D)
_RbnEpsuS5S8GtpUlPktsRcvd_Type=Counter64
_RbnEpsuS5S8GtpUlPktsRcvd_Object=MibScalar
rbnEpsuS5S8GtpUlPktsRcvd=_RbnEpsuS5S8GtpUlPktsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,3,5),_RbnEpsuS5S8GtpUlPktsRcvd_Type())
rbnEpsuS5S8GtpUlPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlPktsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlPktsRcvd.setUnits(_D)
_RbnEpsuS5S8GtpUlOctetsRcvd_Type=Counter64
_RbnEpsuS5S8GtpUlOctetsRcvd_Object=MibScalar
rbnEpsuS5S8GtpUlOctetsRcvd=_RbnEpsuS5S8GtpUlOctetsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,3,6),_RbnEpsuS5S8GtpUlOctetsRcvd_Type())
rbnEpsuS5S8GtpUlOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlOctetsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlOctetsRcvd.setUnits(_E)
_RbnEpsuS5S8GtpUlPktsDiscarded_Type=Counter64
_RbnEpsuS5S8GtpUlPktsDiscarded_Object=MibScalar
rbnEpsuS5S8GtpUlPktsDiscarded=_RbnEpsuS5S8GtpUlPktsDiscarded_Object((1,3,6,1,4,1,2352,2,47,1,3,7),_RbnEpsuS5S8GtpUlPktsDiscarded_Type())
rbnEpsuS5S8GtpUlPktsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlPktsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlPktsDiscarded.setUnits(_D)
_RbnEpsuS5S8GtpUlBearerPktsDiscarded_Type=Counter64
_RbnEpsuS5S8GtpUlBearerPktsDiscarded_Object=MibScalar
rbnEpsuS5S8GtpUlBearerPktsDiscarded=_RbnEpsuS5S8GtpUlBearerPktsDiscarded_Object((1,3,6,1,4,1,2352,2,47,1,3,8),_RbnEpsuS5S8GtpUlBearerPktsDiscarded_Type())
rbnEpsuS5S8GtpUlBearerPktsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlBearerPktsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlBearerPktsDiscarded.setUnits(_D)
_RbnEpsuS5S8GtpUlPolicingPktsDiscarded_Type=Counter64
_RbnEpsuS5S8GtpUlPolicingPktsDiscarded_Object=MibScalar
rbnEpsuS5S8GtpUlPolicingPktsDiscarded=_RbnEpsuS5S8GtpUlPolicingPktsDiscarded_Object((1,3,6,1,4,1,2352,2,47,1,3,9),_RbnEpsuS5S8GtpUlPolicingPktsDiscarded_Type())
rbnEpsuS5S8GtpUlPolicingPktsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlPolicingPktsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuS5S8GtpUlPolicingPktsDiscarded.setUnits(_D)
_RbnEpsuSgi_ObjectIdentity=ObjectIdentity
rbnEpsuSgi=_RbnEpsuSgi_ObjectIdentity((1,3,6,1,4,1,2352,2,47,1,4))
_RbnEpsuSgiDlPktsRcvd_Type=Counter64
_RbnEpsuSgiDlPktsRcvd_Object=MibScalar
rbnEpsuSgiDlPktsRcvd=_RbnEpsuSgiDlPktsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,4,1),_RbnEpsuSgiDlPktsRcvd_Type())
rbnEpsuSgiDlPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiDlPktsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiDlPktsRcvd.setUnits(_D)
_RbnEpsuSgiDlOctetsRcvd_Type=Counter64
_RbnEpsuSgiDlOctetsRcvd_Object=MibScalar
rbnEpsuSgiDlOctetsRcvd=_RbnEpsuSgiDlOctetsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,4,2),_RbnEpsuSgiDlOctetsRcvd_Type())
rbnEpsuSgiDlOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiDlOctetsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiDlOctetsRcvd.setUnits(_E)
_RbnEpsuSgiDlV6PktsRcvd_Type=Counter64
_RbnEpsuSgiDlV6PktsRcvd_Object=MibScalar
rbnEpsuSgiDlV6PktsRcvd=_RbnEpsuSgiDlV6PktsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,4,3),_RbnEpsuSgiDlV6PktsRcvd_Type())
rbnEpsuSgiDlV6PktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiDlV6PktsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiDlV6PktsRcvd.setUnits(_D)
_RbnEpsuSgiDlV6OctetsRcvd_Type=Counter64
_RbnEpsuSgiDlV6OctetsRcvd_Object=MibScalar
rbnEpsuSgiDlV6OctetsRcvd=_RbnEpsuSgiDlV6OctetsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,4,4),_RbnEpsuSgiDlV6OctetsRcvd_Type())
rbnEpsuSgiDlV6OctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiDlV6OctetsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiDlV6OctetsRcvd.setUnits(_E)
_RbnEpsuSgiDlPktsDiscarded_Type=Counter64
_RbnEpsuSgiDlPktsDiscarded_Object=MibScalar
rbnEpsuSgiDlPktsDiscarded=_RbnEpsuSgiDlPktsDiscarded_Object((1,3,6,1,4,1,2352,2,47,1,4,5),_RbnEpsuSgiDlPktsDiscarded_Type())
rbnEpsuSgiDlPktsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiDlPktsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiDlPktsDiscarded.setUnits(_D)
_RbnEpsuSgiUlPktsSent_Type=Counter64
_RbnEpsuSgiUlPktsSent_Object=MibScalar
rbnEpsuSgiUlPktsSent=_RbnEpsuSgiUlPktsSent_Object((1,3,6,1,4,1,2352,2,47,1,4,6),_RbnEpsuSgiUlPktsSent_Type())
rbnEpsuSgiUlPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiUlPktsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiUlPktsSent.setUnits(_D)
_RbnEpsuSgiUlOctetsSent_Type=Counter64
_RbnEpsuSgiUlOctetsSent_Object=MibScalar
rbnEpsuSgiUlOctetsSent=_RbnEpsuSgiUlOctetsSent_Object((1,3,6,1,4,1,2352,2,47,1,4,7),_RbnEpsuSgiUlOctetsSent_Type())
rbnEpsuSgiUlOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiUlOctetsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiUlOctetsSent.setUnits(_E)
_RbnEpsuSgiUlV6PktsSent_Type=Counter64
_RbnEpsuSgiUlV6PktsSent_Object=MibScalar
rbnEpsuSgiUlV6PktsSent=_RbnEpsuSgiUlV6PktsSent_Object((1,3,6,1,4,1,2352,2,47,1,4,8),_RbnEpsuSgiUlV6PktsSent_Type())
rbnEpsuSgiUlV6PktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiUlV6PktsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiUlV6PktsSent.setUnits(_D)
_RbnEpsuSgiUlV6OctetsSent_Type=Counter64
_RbnEpsuSgiUlV6OctetsSent_Object=MibScalar
rbnEpsuSgiUlV6OctetsSent=_RbnEpsuSgiUlV6OctetsSent_Object((1,3,6,1,4,1,2352,2,47,1,4,9),_RbnEpsuSgiUlV6OctetsSent_Type())
rbnEpsuSgiUlV6OctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiUlV6OctetsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiUlV6OctetsSent.setUnits(_E)
_RbnEpsuSgiUlPktsDropped_Type=Counter64
_RbnEpsuSgiUlPktsDropped_Object=MibScalar
rbnEpsuSgiUlPktsDropped=_RbnEpsuSgiUlPktsDropped_Object((1,3,6,1,4,1,2352,2,47,1,4,10),_RbnEpsuSgiUlPktsDropped_Type())
rbnEpsuSgiUlPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiUlPktsDropped.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiUlPktsDropped.setUnits(_D)
_RbnEpsuSgiApn_ObjectIdentity=ObjectIdentity
rbnEpsuSgiApn=_RbnEpsuSgiApn_ObjectIdentity((1,3,6,1,4,1,2352,2,47,1,5))
_RbnEpsuSgiApnStatsTable_Object=MibTable
rbnEpsuSgiApnStatsTable=_RbnEpsuSgiApnStatsTable_Object((1,3,6,1,4,1,2352,2,47,1,5,1))
if mibBuilder.loadTexts:rbnEpsuSgiApnStatsTable.setStatus(_A)
_RbnEpsuSgiApnStatsEntry_Object=MibTableRow
rbnEpsuSgiApnStatsEntry=_RbnEpsuSgiApnStatsEntry_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1))
rbnEpsuSgiApnStatsEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:rbnEpsuSgiApnStatsEntry.setStatus(_A)
class _RbnEpsuSgiApnIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RbnEpsuSgiApnIndex_Type.__name__=_G
_RbnEpsuSgiApnIndex_Object=MibTableColumn
rbnEpsuSgiApnIndex=_RbnEpsuSgiApnIndex_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,1),_RbnEpsuSgiApnIndex_Type())
rbnEpsuSgiApnIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnEpsuSgiApnIndex.setStatus(_A)
class _RbnEpsuSgiApnName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_RbnEpsuSgiApnName_Type.__name__=_F
_RbnEpsuSgiApnName_Object=MibTableColumn
rbnEpsuSgiApnName=_RbnEpsuSgiApnName_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,2),_RbnEpsuSgiApnName_Type())
rbnEpsuSgiApnName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnName.setStatus(_A)
_RbnEpsuSgiApnDlPktsRcvd_Type=Counter64
_RbnEpsuSgiApnDlPktsRcvd_Object=MibTableColumn
rbnEpsuSgiApnDlPktsRcvd=_RbnEpsuSgiApnDlPktsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,3),_RbnEpsuSgiApnDlPktsRcvd_Type())
rbnEpsuSgiApnDlPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnDlPktsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiApnDlPktsRcvd.setUnits(_D)
_RbnEpsuSgiApnDlOctetsRcvd_Type=Counter64
_RbnEpsuSgiApnDlOctetsRcvd_Object=MibTableColumn
rbnEpsuSgiApnDlOctetsRcvd=_RbnEpsuSgiApnDlOctetsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,4),_RbnEpsuSgiApnDlOctetsRcvd_Type())
rbnEpsuSgiApnDlOctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnDlOctetsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiApnDlOctetsRcvd.setUnits(_E)
_RbnEpsuSgiApnDlPktsDiscarded_Type=Counter64
_RbnEpsuSgiApnDlPktsDiscarded_Object=MibTableColumn
rbnEpsuSgiApnDlPktsDiscarded=_RbnEpsuSgiApnDlPktsDiscarded_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,5),_RbnEpsuSgiApnDlPktsDiscarded_Type())
rbnEpsuSgiApnDlPktsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnDlPktsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiApnDlPktsDiscarded.setUnits(_D)
_RbnEpsuSgiApnUlPktsSent_Type=Counter64
_RbnEpsuSgiApnUlPktsSent_Object=MibTableColumn
rbnEpsuSgiApnUlPktsSent=_RbnEpsuSgiApnUlPktsSent_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,6),_RbnEpsuSgiApnUlPktsSent_Type())
rbnEpsuSgiApnUlPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnUlPktsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiApnUlPktsSent.setUnits(_D)
_RbnEpsuSgiApnUlOctetsSent_Type=Counter64
_RbnEpsuSgiApnUlOctetsSent_Object=MibTableColumn
rbnEpsuSgiApnUlOctetsSent=_RbnEpsuSgiApnUlOctetsSent_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,7),_RbnEpsuSgiApnUlOctetsSent_Type())
rbnEpsuSgiApnUlOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnUlOctetsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiApnUlOctetsSent.setUnits(_E)
_RbnEpsuSgiApnUlPktsDropped_Type=Counter64
_RbnEpsuSgiApnUlPktsDropped_Object=MibTableColumn
rbnEpsuSgiApnUlPktsDropped=_RbnEpsuSgiApnUlPktsDropped_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,8),_RbnEpsuSgiApnUlPktsDropped_Type())
rbnEpsuSgiApnUlPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnUlPktsDropped.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiApnUlPktsDropped.setUnits(_D)
_RbnEpsuSgiApnDlV6PktsRcvd_Type=Counter64
_RbnEpsuSgiApnDlV6PktsRcvd_Object=MibTableColumn
rbnEpsuSgiApnDlV6PktsRcvd=_RbnEpsuSgiApnDlV6PktsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,9),_RbnEpsuSgiApnDlV6PktsRcvd_Type())
rbnEpsuSgiApnDlV6PktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnDlV6PktsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiApnDlV6PktsRcvd.setUnits(_D)
_RbnEpsuSgiApnDlV6OctetsRcvd_Type=Counter64
_RbnEpsuSgiApnDlV6OctetsRcvd_Object=MibTableColumn
rbnEpsuSgiApnDlV6OctetsRcvd=_RbnEpsuSgiApnDlV6OctetsRcvd_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,10),_RbnEpsuSgiApnDlV6OctetsRcvd_Type())
rbnEpsuSgiApnDlV6OctetsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnDlV6OctetsRcvd.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiApnDlV6OctetsRcvd.setUnits(_E)
_RbnEpsuSgiApnUlV6PktsSent_Type=Counter64
_RbnEpsuSgiApnUlV6PktsSent_Object=MibTableColumn
rbnEpsuSgiApnUlV6PktsSent=_RbnEpsuSgiApnUlV6PktsSent_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,11),_RbnEpsuSgiApnUlV6PktsSent_Type())
rbnEpsuSgiApnUlV6PktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnUlV6PktsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiApnUlV6PktsSent.setUnits(_D)
_RbnEpsuSgiApnUlV6OctetsSent_Type=Counter64
_RbnEpsuSgiApnUlV6OctetsSent_Object=MibTableColumn
rbnEpsuSgiApnUlV6OctetsSent=_RbnEpsuSgiApnUlV6OctetsSent_Object((1,3,6,1,4,1,2352,2,47,1,5,1,1,12),_RbnEpsuSgiApnUlV6OctetsSent_Type())
rbnEpsuSgiApnUlV6OctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEpsuSgiApnUlV6OctetsSent.setStatus(_A)
if mibBuilder.loadTexts:rbnEpsuSgiApnUlV6OctetsSent.setUnits(_E)
_RbnEpsuMIBConformance_ObjectIdentity=ObjectIdentity
rbnEpsuMIBConformance=_RbnEpsuMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,47,2))
_RbnEpsuMIBGroups_ObjectIdentity=ObjectIdentity
rbnEpsuMIBGroups=_RbnEpsuMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,47,2,1))
_RbnEpsuMIBCompliances_ObjectIdentity=ObjectIdentity
rbnEpsuMIBCompliances=_RbnEpsuMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,47,2,2))
rbnEpsuS1uGtpGroup=ObjectGroup((1,3,6,1,4,1,2352,2,47,2,1,1))
rbnEpsuS1uGtpGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:rbnEpsuS1uGtpGroup.setStatus(_A)
rbnEpsuSgwGtpGroup=ObjectGroup((1,3,6,1,4,1,2352,2,47,2,1,2))
rbnEpsuSgwGtpGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:rbnEpsuSgwGtpGroup.setStatus(_A)
rbnEpsuPgwGtpGroup=ObjectGroup((1,3,6,1,4,1,2352,2,47,2,1,3))
rbnEpsuPgwGtpGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:rbnEpsuPgwGtpGroup.setStatus(_A)
rbnEpsuSgiGroup=ObjectGroup((1,3,6,1,4,1,2352,2,47,2,1,4))
rbnEpsuSgiGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:rbnEpsuSgiGroup.setStatus(_A)
rbnEspuSgiApnGroup=ObjectGroup((1,3,6,1,4,1,2352,2,47,2,1,5))
rbnEspuSgiApnGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:rbnEspuSgiApnGroup.setStatus(_A)
rbnEpsuMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,47,2,2,1))
rbnEpsuMIBCompliance.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:rbnEpsuMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnEpsuMIB':rbnEpsuMIB,'rbnEpsuNotifcationGroup':rbnEpsuNotifcationGroup,'rbnEpsuStatMIBObjects':rbnEpsuStatMIBObjects,'rbnEpsuS1uGtp':rbnEpsuS1uGtp,_I:rbnEpsuS1uDlPktsSent,_J:rbnEpsuS1uDlOctetsSent,_K:rbnEpsuS1uDlPktsDropped,_L:rbnEpsuS1uDlPolicingPktsDropped,_M:rbnEpsuS1uDlUeIdlePktsDropped,_N:rbnEpsuS1uUlPktsRcvd,_O:rbnEpsuS1uUlOctetsRcvd,_P:rbnEpsuS1uUlPktsDiscarded,_Q:rbnEpsuS1uUlBearerPktsDiscarded,_R:rbnEpsuS1uUlPolicingPktsDiscarded,'rbnEpsuSgwGtp':rbnEpsuSgwGtp,_S:rbnEpsuS5S8GtpDlPktsRcvd,_T:rbnEpsuS5S8GtpDlOctetsRcvd,_U:rbnEpsuS5S8GtpDlPktsDiscarded,_V:rbnEpsuS5S8GtpUlPktsSent,_W:rbnEpsuS5S8GtpUlOctetsSent,_X:rbnEpsuS5S8GtpUlPktsDropped,'rbnEpsuPgwGtp':rbnEpsuPgwGtp,_Y:rbnEpsuS5S8GtpDlPktsSent,_Z:rbnEpsuS5S8GtpDlOctetsSent,_a:rbnEpsuS5S8GtpDlPktsDropped,_b:rbnEpsuS5S8GtpDlPolicingPktsDropped,_c:rbnEpsuS5S8GtpUlPktsRcvd,_d:rbnEpsuS5S8GtpUlOctetsRcvd,_e:rbnEpsuS5S8GtpUlPktsDiscarded,_f:rbnEpsuS5S8GtpUlBearerPktsDiscarded,_g:rbnEpsuS5S8GtpUlPolicingPktsDiscarded,'rbnEpsuSgi':rbnEpsuSgi,_h:rbnEpsuSgiDlPktsRcvd,_i:rbnEpsuSgiDlOctetsRcvd,_j:rbnEpsuSgiDlV6PktsRcvd,_k:rbnEpsuSgiDlV6OctetsRcvd,_l:rbnEpsuSgiDlPktsDiscarded,_m:rbnEpsuSgiUlPktsSent,_n:rbnEpsuSgiUlOctetsSent,_p:rbnEpsuSgiUlV6PktsSent,_q:rbnEpsuSgiUlV6OctetsSent,_o:rbnEpsuSgiUlPktsDropped,'rbnEpsuSgiApn':rbnEpsuSgiApn,'rbnEpsuSgiApnStatsTable':rbnEpsuSgiApnStatsTable,'rbnEpsuSgiApnStatsEntry':rbnEpsuSgiApnStatsEntry,_H:rbnEpsuSgiApnIndex,_r:rbnEpsuSgiApnName,_s:rbnEpsuSgiApnDlPktsRcvd,_t:rbnEpsuSgiApnDlOctetsRcvd,_w:rbnEpsuSgiApnDlPktsDiscarded,_x:rbnEpsuSgiApnUlPktsSent,_y:rbnEpsuSgiApnUlOctetsSent,_A1:rbnEpsuSgiApnUlPktsDropped,_u:rbnEpsuSgiApnDlV6PktsRcvd,_v:rbnEpsuSgiApnDlV6OctetsRcvd,_z:rbnEpsuSgiApnUlV6PktsSent,_A0:rbnEpsuSgiApnUlV6OctetsSent,'rbnEpsuMIBConformance':rbnEpsuMIBConformance,'rbnEpsuMIBGroups':rbnEpsuMIBGroups,_A2:rbnEpsuS1uGtpGroup,_A3:rbnEpsuSgwGtpGroup,_A4:rbnEpsuPgwGtpGroup,_A5:rbnEpsuSgiGroup,_A6:rbnEspuSgiApnGroup,'rbnEpsuMIBCompliances':rbnEpsuMIBCompliances,'rbnEpsuMIBCompliance':rbnEpsuMIBCompliance})